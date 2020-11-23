# import logging
# import Helpers

import azure.functions as func
import numpy as np
import Helpers
from lxml import etree, html
import requests
import pandas as pd
# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     url = 'https://tide.pier.or.th/chart/displaydata/04bf4568-a2d7-4352-bdec-80db21f46b07'

#     xpath = '//*[@id="data-section"]//div//div//div//div//div[2]//div//div[2]//div[1]//table//tbody//tr[position() >= 2]//text()'

#     download_path = './download/FI_CB_015/'

#     download_links = Helpers.get_download_link(url, xpath)

#     logging.info(download_links)

#     upload_file_paths = []

#     for link in download_links:
#         print(link)
#     return func.HttpResponse(
#             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#             status_code=200
    # )
    # for link in download_links:
    #     if Helpers.is_downloadable(link):
    #         download_filepath = Helpers.download(link, download_path)
    #         upload_file_paths.append(download_filepath)
    # return func.HttpResponse(
    #         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #         status_code=200
    # )
def main(req: func.HttpRequest) -> func.HttpResponse:


    url = 'https://tide.pier.or.th/chart/FICBDLPBSMM00303'
    url2 = ['https://tide.pier.or.th/chart/FICBDLPBSMM00303','https://tide.pier.or.th/chart/FIPGRTQ00564','https://tide.pier.or.th/chart/FICBDLPBSMM01382','https://tide.pier.or.th/chart/FICBDLPTCSQ00128']
    xpath = '//*[@id="list-data"]/ul/li[position()>=2]/text()'
    bruh = Helpers.extract_element(url, xpath)
    page = requests.get(url)
    tree = html.fromstring(page.content) 
    items = tree.xpath(xpath)
    htmll = etree.Element("html")
    np.array(bruh)
    #print('hi', htmll.xpath("string()"))
    #print('tree', html.tostring(tree))
    #print('items',items)
    # for result in sorted(
    #     Helpers.extract_element(url,xpath).items(), key=lambda x:x[1],reverse=True):
    #     print( 'test: ', result)
    #print('len: ', bruh)
    changed_out = np.array_split(bruh,2)
    print(changed_out)

    f = open("./Tide Listing/Grand Total of No. of Branches of Commercial Banks.csv", 'a')
    # for i in bruh:
    #     j = i
    #     with f as fd:
    #         fd.write(changed_out[0][j],',',changed_out[1][j])
    # f.close()
    df = pd.DataFrame(index=changed_out[0:][0:])
    df.to_csv(path_or_buf = "./Tide Listing/No. of Branches of Commercial Banks in Bangkok.csv", header=False)
    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.", 
        status_code=200



    # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    # tree = html.fromstring(page.content)
    # #This will create a list of buyers:
    # buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    # print(html.tostring(tree))
    # #This will create a list of prices
    # prices = tree.xpath('//section[@id = "home-tabs-wrapper"]/div[@id="data-section"]/div/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[position() >= 2]/td/text()')
    # print('tree: ', tree)
    # print ('Buyers: ', buyers)
    # print ('Prices: ', prices)


    # return func.HttpResponse(
    #     "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.", 
    #     status_code=200
    )