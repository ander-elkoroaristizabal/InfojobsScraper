# This file has the functions needed to scrap one given Infojobs offer url.

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
    # Definimos un user-agent de navegador para poder cargar la página:
    headers = {
        "User-Agent": '''Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36
         (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'''
    }
    return BeautifulSoup(urlopen(Request(url, headers=headers)), 'html.parser', from_encoding="windows-1252")


def scrap_title_panel(soup):
    """
    This function analyzes the title panel and retrieves the useful information as a dict.
    :param soup: BeautifulSoup object with the title panel.
    :return info_dict: dictionary with the interesting characteristics we have found in the given title panel.
    """
    title_panel = soup.body.find("div", {"class": "panel-canvas panel-rounded"})
    # Obtenemos los campos en el panel principal:
    position = str(title_panel.find(id="prefijoPuesto").string)
    company = str(title_panel.find("a", {"class": "link", "data-track": "Company Detail Clicked"}).string)
    # Evitamos que la búsqueda del campo valoracion_empresa
    # de error en caso de no estar presente:
    company_valuation = title_panel.find("li", id="reviewStars")
    if company_valuation:
        company_valuation = int(company_valuation.meter['value'])
    else:
        company_valuation = None
    city = str(title_panel.find(id="prefijoPoblacion").string).strip(' ,')
    country = str(title_panel.find(id="prefijoPais").string).strip(' ()')
    contract_type = str(title_panel.find(id="prefijoJornada").string)[18:].capitalize()
    # Para encontrar de manera más segura los contenidos interesantes sin id
    # reducimos el espacio de búsqueda a la lista de puntos:
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


def scrap_this_page(url):
    """
    General routine scraping one given Infojobs url.
    :param url: the url of the Infojobs offer.
    :return title_info: dictionary with the interesting characteristics we have found in the given url.
    """
    soup = get_the_info(url)
    sleep(1)
    title_info = scrap_title_panel(soup)
    return title_info
