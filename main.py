"""
Ander Elkoroaristizabal Peleteiro, March 2021

This file executes the routine retrieving the info from a given Infojobs job post url,
in its simplest version, and from several, in a bright future.
"""

from OnePageScraper import scrap_this_page
from SearchPageScraper import scrape_search_results
import pandas as pd
from time import sleep
from datetime import datetime


def get_link_info(list_with_urls):
    # df = pd.DataFrame(columns=['url', "puesto", "empresa", "valoracion_empresa",
    #                            "ciudad", "pais", "tipo_contrato", "salario", "exp_minima"]
    # df['url'] = url_list
    dict_list = []
    for url in list_with_urls:
        sleep(2)
        job_info = scrap_this_page(url)
        job_info['url'] = url
        dict_list.append(job_info)
    return pd.DataFrame(dict_list)


if __name__ == '__main__':
    keywords = str(input("EN: enter keywords: ")) or \
        "Data Scientist"
    print()
    url_list = scrape_search_results(keywords)
    print()
    print("Number of offers for analyzing:", len(url_list))
    print()
    res = get_link_info(url_list)
    now = datetime.now()
    filename = keywords.replace(" ", "_") + "_" + now.strftime("%d-%m-%Y_%H_%M_%S") + ".csv"
    res.to_csv("Examples/" + filename, index = False)
    print(res)
