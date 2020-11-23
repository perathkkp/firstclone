import logging
import Helpers

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = 'https://www.bot.or.th/English/Statistics/FinancialInstitutions/Pages/StatDepositsAndLoans.aspx'

    xpath = '//*[@id="ctl00_ctl73_g_17a2a365_df74_4044_abf1_b8af0ad3dd29_ctl00_UpdatePanel1"]//tr[position() >= 24 and not(position() > 27)]//td[3]//a'

    download_path = './download/FI_CB_015/'

    download_links = Helpers.get_download_link(url, xpath)

    logging.info(download_links)

    upload_file_paths = []
    for link in download_links:
        if Helpers.is_downloadable(link):
            download_filepath = Helpers.download(link, download_path)
            upload_file_paths.append(download_filepath)
    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )
