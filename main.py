"""
Ander Elkoroaristizabal Peleteiro, March 2021

This file executes the routine retrieving the info from a given Infojobs job post url,
in its simplest version, and from several, in a bright future.
"""

from OnePageScraper import scrap_this_page

if __name__ == '__main__':
    onepage2 = "https://www.infojobs.net/barcelona/un-data-analyst/of-i210e2eec1e472aa83876b587065bc4?applicationOrigin=mahout-view-offer%7Celement%7Ef47cb3da-521d-4780-8098-af950424c10b%7Cversion%7EITEM_BASED%7Cscoring%7E2.5365782"
    print(scrap_this_page(onepage2))
