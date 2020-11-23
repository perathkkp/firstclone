import azure.functions as func
import numpy as np
import Helpers
from lxml import etree, html
import requests
import pandas as pd

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    url2 = ['https://tide.pier.or.th/chart/FICBDLPBSMM00303','https://tide.pier.or.th/chart/FIPGRTQ00564','https://tide.pier.or.th/chart/FICBDLPBSMM01382','https://tide.pier.or.th/chart/FICBDLPTCSQ00128']
    xpath = '//*[@id="list-data"]/ul/li[position()>=2]/text()'
    nameXpath = '//*[@id="chart-section"]/div/div/div[1]/div/div[1]/div/div/div/div[1]/span/text()'
    
    for i in range(len(url2)):7
        bruh = Helpers.extract_element(url2[i], xpath)
        autoName = Helpers.extract_element(url2[i],nameXpath)
        np.array(bruh)
        changed_out = np.array_split(bruh,2)
        #reName = autoName[0].replace("","")
        reName = autoName[0].strip()
        
        print(changed_out)
        name = "./Tide Listing/"+autoName[0]+".csv"
        print(name)
        df = pd.DataFrame(index=changed_out[0:][0:])
        

    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.", 
        status_code=200
    )