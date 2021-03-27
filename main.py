"""
Ander Elkoroaristizabal Peleteiro, March 2021

This file executes the routine retrieving the info from a given Infojobs job post url,
in its simplest version, and from several, in a bright future.
"""

from OnePageScraper import scrap_this_page
from SearchPageScraper import scrape_search_results
import pandas as pd
from time import sleep


def get_link_info(list_with_urls):
    # df = pd.DataFrame(columns=['url', "puesto", "empresa", "valoracion_empresa",
    #                            "ciudad", "pais", "tipo_contrato", "salario", "exp_minima"]
    # df['url'] = url_list
    dict_list = []
    for url in list_with_urls:
        sleep(2.5)
        job_info = scrap_this_page(url)
        print(url)
        print(job_info)
        job_info['url'] = url
        dict_list.append(job_info)
    return pd.DataFrame(dict_list)


if __name__ == '__main__':
    keywords = str(input("EN: enter keywords: ")) or \
        "Data Scientist"
    print()
    url_list = scrape_search_results(keywords)
    res = get_link_info(url_list)
    print(res)