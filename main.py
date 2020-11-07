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

content = requests.get("https://intranet.rfevb.com/rfevbcom/includes-html/competiciones/clasificacion321-conEncuentros-datos.php?IdCampeonato="+'4059'+"&Jornada="+'4').content


# bucle en la jornada del 1- 23 (interessants del 1- 5)
all_trs = BeautifulSoup(requests.get("https://intranet.rfevb.com/rfevbcom/includes-html/competiciones/clasificacion321-conEncuentros-datos.php?IdCampeonato="+'4059'+"&Jornada="+'4').content).findAll('tr')


resultados = 'RESULTADOS'
clasificacion = 'CLASIFICACIÓN'
proximos_encuentros = 'PRÓXIMOS ENCUENTROS'

es_resultado = False
es_clasificacion = False
es_proximos_encuentros = False


for item in all_trs:
    titulo = item.get_text()

    #búsqueda de títulos, si encuentra titulo se va a la siguiente iteracion del bucle
    if resultados in titulo:
        es_proximos_encuentros = False
        es_resultado = True
        continue
    elif clasificacion in titulo:
        es_resultado = False
        es_clasificacion = True
        continue
    elif proximos_encuentros in titulo:
        es_clasificacion = False
        es_proximos_encuentros = True
        continue

    if es_resultado:
        print ("ahora estamos en resultados")
    elif es_clasificacion:
        print("ahora estamos en clasificacion")
    elif es_proximos_encuentros:
        print ("ahora estamos en proximos encuentros")


    print(item)