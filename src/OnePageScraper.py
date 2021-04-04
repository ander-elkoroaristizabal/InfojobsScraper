"""
This file has the functions needed to scrap one given Infojobs offer url.
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from re import sub
from time import sleep


def get_the_info(url):
    """
    This function returns a BeautifulSoup object created from the given url without getting blocked.
    :param url: The url to be scraped.
    :return: The BeautifulSoup object created from the given url.
    """
    # We define a browser-like user-agent in order to get the page
    headers = {
        "User-Agent": '''Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36
         (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'''
    }
    return BeautifulSoup(urlopen(Request(url, headers=headers)), 'html.parser', from_encoding="windows-1252")


def scrape_title_panel(soup):
    """
    This function analyzes the title panel and retrieves the useful information as a dict.
    :param soup: BeautifulSoup object with the title panel.
    :return info_dict: dictionary with the interesting characteristics we have found in the given title panel.
    """
    title_panel = soup.body.find("div", {"class": "panel-canvas panel-rounded"})
    # We get the info in the main panel:
    position = str(title_panel.find(id="prefijoPuesto").string)
    company = str(title_panel.find("a", {"class": "link", "data-track": "Company Detail Clicked"}).string)
    # We make sure the non-existence of company_valuation
    # does not arise an error:
    company_valuation = title_panel.find("li", id="reviewStars")
    if company_valuation:
        company_valuation = int(company_valuation.meter['value'])
    else:
        company_valuation = None
    city = str(title_panel.find(id="prefijoPoblacion").string).strip(' ,')
    country = str(title_panel.find(id="prefijoPais").string).strip(' ()')
    contract_type = str(title_panel.find(id="prefijoJornada").string)[18:].capitalize()
    # In order to find the contents without id more securely
    # we restrict the search space to the dotted list
    bullet_list = title_panel.find("div", {"class": "col-child inner"})
    salary = sub(r"Salario:?", "", str(bullet_list.find(text=lambda t: "Salario" in t))).strip().capitalize()
    min_exp = str(bullet_list.find(text=lambda t: "Experiencia mínima" in t))[20:].capitalize()
    info_dict = {"position": position,
                 "company": company,
                 "valoracion_empresa": company_valuation,
                 "city": city,
                 "country": country,
                 "contract_type": contract_type,
                 "salary": salary,
                 "min_exp": min_exp}
    return info_dict


def scrape_this_page(url):
    """
    General routine scraping one given Infojobs url.
    :param url: the url of the Infojobs offer.
    :return title_info: dictionary with the interesting characteristics we have found in the given url.
    """
    soup = get_the_info(url)
    sleep(1)
    title_info = scrape_title_panel(soup)
    return title_info
