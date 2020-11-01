from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.rfevb.com/primera-division-femenina-grupo-a-clasificacion"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup)
