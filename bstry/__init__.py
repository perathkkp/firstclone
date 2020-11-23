import azure.functions as func
import numpy as np
import Helpers
from lxml import etree, html
import requests
import pandas as pd
from bs4 import BeautifulSoup


def main(req: func.HttpRequest) -> func.HttpResponse:

    url = 'https://tide.pier.or.th/chart/FICBDLPBSMM00303'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    htmll = html.tostring(tree)
    soup = BeautifulSoup(htmll)
    print(soup.prettify())
    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.", 
        status_code=200
    )
