import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

#url = "http://www.rfevb.com/primera-division-femenina-grupo-a-clasificacion"
# utils url : https://intranet.rfevb.com/rfevbcom/includes-html/competiciones/clasificacion321-conEncuentros-datos.php?IdCampeonato=4059&Jornada=3
# Make a GET request to fetch the raw HTML content
#html_content = requests.get(url).text

# Parse the html content
#soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify()) # print the parsed data of html
from volleyScraper import volleyScraper

scraper = volleyScraper()
scraper.scrape()



