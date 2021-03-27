"""
This file contains the code neeeded to scrape a given search page from Infojobs.net.
"""

from urllib.request import Request, urlopen
from urllib.parse import quote
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def scrape_search_result_page(url, driver, i):
    # Scroll the page to get the info:
    try:
        SCROLL_PAUSE_TIME = 0.5
        driver.get(url)
        if i == 1:
            input("Resolve the captcha and press enter when done.\n")
        sleep(5)

        page = driver.find_element_by_tag_name('body')

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            page.send_keys(Keys.PAGE_DOWN)
            sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        soup = BeautifulSoup(driver.page_source, "html.parser")
    finally:
        print(f"Page {i} concluded!")

    # Get the urls:
    items_panel = soup.find("ul", {"class": "ij-ComponentList"})
    offer_urls = ["https://" + item['href'][2:] for item in
                  items_panel.findAll("a", {"class": "ij-OfferCardContent-description-title-link"})]
    return offer_urls


def scrape_search_results(search_key):
    base_url = 'https://www.infojobs.net/ofertas-trabajo'
    search_url = base_url + '?keyword=' + quote(str(search_key))
    headers = {
        "User-Agent": '''Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36
         (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'''
    }
    # Getting number of results:
    soup = BeautifulSoup(urlopen(Request(search_url, headers=headers)),
                         "html.parser", from_encoding="windows-1252")
    num_results = int(soup.find("h1", {"class": "ij-ResultsOverview"}).text[:2])
    num_pages = int(num_results/20) + 1
    # Defining the driver
    # # Defining the options
    options = webdriver.ChromeOptions()
    userAgent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    options.add_argument(f'user-agent={userAgent}')
    # # The driver itself
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
    driver.implicitly_wait(10)
    #
    all_offer_urls = []
    for i in range(1, num_pages+1):
        page_url = str(f"&page={i}")
        new_urls = scrape_search_result_page(search_url+page_url, driver, i)
        all_offer_urls = all_offer_urls + new_urls
        sleep(2)
    driver.quit()
    return all_offer_urls
