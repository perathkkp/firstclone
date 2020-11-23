import logging
import os
import cgi
import requests
from azure.storage.blob import BlobServiceClient, BlobClient
import subprocess
from urllib.request import urlopen
from lxml import etree,html


def is_downloadable(url: str):
    # Does the url contain a downloadable resource
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def download(url: str, download_path: str, filename=None) -> str:
    logging.info('Downloading:\t' + url)

    r = requests.get(url, allow_redirects=True)
    if not filename:
        filename = cgi.parse_header(
            r.headers['Content-Disposition'])[-1]['filename']
    download_filepath = os.path.join(download_path, filename)
    open(download_filepath, 'wb').write(r.content)
    return download_filepath


def upload_to_blob(container_name: str, filepath: str):
    blob_service_client = BlobServiceClient.from_connection_string(
        os.environ['AZURE_STORAGE_CONNECTION_STRING'])
    filename = os.path.basename(filepath)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=filename)

    # Upload the file to blob
    logging.info("Uploading to Azure Storage as blob:\t" + filename)
    with open(filepath, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        logging.info('Upload:\t' + str(filepath) + '\tComplete!!')


def get_download_link(url, xpath):
    logging.info(
        "python ./Util/get_download_link.py '{0}' '{1}'".format(url, xpath))
    result = subprocess.check_output(
        "python ./Util/get_download_link.py '{0}' '{1}'".format(url, xpath), shell=True, encoding='utf-8')
    return list(result.replace('\n', '').split('|'))


def capture_pdf(url, outputFilePath):
    logging.info(
        "python ./Util/capture_pdf.py '{0}' '{1}'".format(url, outputFilePath))

    os.system(
        "python ./Util/capture_pdf.py '{0}' '{1}'".format(url, outputFilePath))
    # result = subprocess.check_output(
    #     "python ./Util/capture_pdf.py '{0}' '{1}'".format(url, outputFilePath), shell=True, encoding='utf-8')
    # return list(result.replace('\n', '').split('|'))

def extract_element(url, xpath):
    page = requests.get(url)
    tree = html.fromstring(page.content) 
    root = html.tostring(tree)
    items = tree.xpath(xpath)
    return items

