# Infojobs Scraper

### Descripción: 

Este módulo Python tiene como objetivo poder hacer una búsqueda concreta en *Infojobs* 
y devolver un conjunto de datos con las características más relevantes de las ofertas resultado.
Es capaz de buscar unas palabras clave en Infojobs.net 
y devolver una lista con las urls respuesta, además de cierta información relevante. 
Esto último no siempre funciona, caso en el cual sólo devuelve la url.

Este módulo ha sido desarrollado con fines educativos,
no comerciales. 

### Description: 

The purpose of this Python module is to, 
given some search parameters, 
retrieve the most relevant information of the answer *Infojobs* job offers.
It is now able to search some keywords in Infojobs.net and get the resulting urls and some info, 
although it sometimes fails when getting the info and just returns the url. 

This module has been developed for educative (non-comercial) purposes.

## Used libraries:

```
urllib
selenium
BeautifulSoup
re
```

### Files: 

+ **main.py**: contains the main routine. 
+ **OnePageScraper.py**: contains the code for scraping just one *Infojobs* offer.
+ **SearchPageScraper.py**: contains the code for scraping the search results pages in order to get the links to the offers. 
+ **robots.txt**: *robots.txt* file from *Infojobs.net* at the beginning of the development of this module.
