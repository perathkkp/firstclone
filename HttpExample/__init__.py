import logging
import azure.functions as func
import os
import Helpers


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = 'https://www.bot.or.th/English/Statistics/FinancialInstitutions/Pages/StatDepositsAndLoans.aspx'

    xpath = '//div[@id="ctl00_ctl73_g_17a2a365_df74_4044_abf1_b8af0ad3dd29_ctl00_plhContentDisplay"]//table//tr//td[3]//a'

    download_path = './download'

    download_links = Helpers.get_download_link(url, xpath)

    logging.info(download_links)

    upload_file_paths = []

    for link in download_links:
        if Helpers.is_downloadable(link):
            download_filepath = Helpers.download(link, download_path)
            upload_file_paths.append(download_filepath)
        break

    for upload_file_path in upload_file_paths:
        Helpers.upload_to_blob('kk1', upload_file_path)

    logging.info('Python HTTP trigger function completed.')

    return func.HttpResponse("Completed", status_code=200)
