# This file has the functions needed to scrap one given Infojobs offer url.

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def get_the_info(url):
    """
    :param url: The url to be scraped.
    :return: The BeautifulSoup object created with the requested connection.
    """
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
    puesto = str(title_panel.find(id="prefijoPuesto").string)
    empresa = str(title_panel.find("a", {"class": "link", "data-track": "Company Detail Clicked"}).string)
    valoracion_empresa = int(title_panel.find("li", id="reviewStars").meter['value'])
    ciudad = str(title_panel.find(id="prefijoPoblacion").string).strip(' ,')
    pais = str(title_panel.find(id="prefijoPais").string).strip(' ()')
    tipo_contrato = str(title_panel.find(id="prefijoJornada").string)[18:].capitalize()
    # Para encontrar de manera más segura los contenidos interesantes sin id
    # reducimos el espacio de búsqueda a la lista de puntos:
    bullet_list = title_panel.find("div", {"class": "col-child inner"})
    salario = str(bullet_list.find(text=lambda t: "Salario" in t))[9:]
    exp_minima = str(bullet_list.find(text=lambda t: "Experiencia mínima" in t))[20:].capitalize()
    info_dict = {"puesto": puesto,
                 "empresa": empresa,
                 "valoracion_empresa": valoracion_empresa,
                 "ciudad": ciudad,
                 "pais": pais,
                 "tipo_contrato": tipo_contrato,
                 "salario": salario,
                 "exp_minima": exp_minima}
    return info_dict


def scrap_this_page(url):
    """
    General routine scraping one given Infojobs url.
    :param url: the url of the Infojobs offer.
    :return title_info: dictionary with the interesting characteristics we have found in the given url.
    """
    soup = get_the_info(url)
    title_info = scrap_title_panel(soup)
    return title_info
