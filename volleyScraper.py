import requests
from bs4 import BeautifulSoup


class volleyScraper():

    def __init__(self):
        print ("init")

    def __procesa_resultado(self, item):
        print("estoy procesando el resultado ")
        print(item)


    def scrape(self):
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
                self.__procesa_resultado(item)

            elif es_clasificacion:
                print("ahora estamos en clasificacion")
            elif es_proximos_encuentros:
                print ("ahora estamos en proximos encuentros")