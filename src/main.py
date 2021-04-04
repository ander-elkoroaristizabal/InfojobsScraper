"""
Ander Elkoroaristizabal Peleteiro, March 2021

This file executes the routine retrieving the info from a given Infojobs job post url,
in its simplest version, and from several, in a bright future.
"""

from OnePageScraper import scrape_this_page
from SearchPageScraper import scrape_search_results
import pandas as pd
from time import sleep
from datetime import datetime
from os import path
from tqdm import tqdm
from sys import stdout


def get_link_info(list_with_urls):
    """
    This functions takes the scraped list of job offer urls and
    returns a dataframe with the information retrieved of each.
    :param list_with_urls: list of the job offers found when scraping search pages.
    :return: DataDrame with job offer info.
    """
    dict_list = []
    for url in tqdm(list_with_urls, desc="Progress scraping the offers", file=stdout):
        sleep(2)
        # Scrape the given url:
        job_info = scrape_this_page(url)
        job_info['url'] = url
        # Save the resulting dict
        dict_list.append(job_info)
    # Return a DataFrame with all the scraped information
    return pd.DataFrame(dict_list)


if __name__ == '__main__':
    """
    Main routine.
    """
    print()
    # Input: palabras clave
    keywords = str(input("EN: enter keywords: ")) or "Data Scientist"
    # Obtención de la lista de urls analizando las páginas resultado de la búsqueda:
    url_list = scrape_search_results(keywords)
    print()
    print("Number of offer ulrs fetched for analyzing:", len(url_list))
    print()
    # Obtención de la información guardada en cada una de las urls:
    res = get_link_info(url_list)
    # Definición del nombre del fichero y del path
    now = datetime.now()
    filename = keywords.replace(" ", "_") + "_" + now.strftime("%d-%m-%Y_%H_%M_%S") + ".csv"
    dirname = path.dirname(__file__)
    path = path.join(dirname, "../examples/" + filename)
    # Guardado y output del dataframe
    res.to_csv(path, index=False)
    print()
    print(res)
