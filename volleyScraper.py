import requests
from bs4 import BeautifulSoup
import csv

class volleyScraper():

    def __init__(self):
        self.dataResultados = []
        self.dataClasificacion = []

    def __clean_resultados(self, equipos, fecha_hora,sets_resultados):

        #limpiamos y clasificamos bien los datos de la variable equipos en numero, equipo1 y equipo2
        numero = equipos[0:equipos.find('.')]
        equipos = equipos[equipos.find('.')+2:equipos.__len__()]
        equipo1 = equipos[0: equipos.find('-')-1]
        equipo2 = equipos[equipos.find('-') + 2:equipos.__len__()]

        #limpiamos y clasificamos los datos fecha y hora por separado
        fecha = fecha_hora[0:fecha_hora.find(' ')]
        hora = fecha_hora[fecha_hora.find('(')+1: fecha_hora.__len__()-2]

        #limpiamos y clasificamos los resultados finales de cada equipo y de cada set
        sets_ganados_equipo1 = sets_resultados[0:1]
        sets_ganados_equipo2 = sets_resultados[4:5]
        sets_resultados = sets_resultados[sets_resultados.find('(') + 1:sets_resultados.__len__() - 1]
        resultado_set1 = sets_resultados[0:sets_resultados.find('/')]
        sets_resultados = sets_resultados[sets_resultados.find('/')+1: sets_resultados.__len__()]
        resultado_set2 = sets_resultados[0:sets_resultados.find('/')]
        sets_resultados = sets_resultados[sets_resultados.find('/')+1: sets_resultados.__len__()]
        resultado_set3 = sets_resultados[0:sets_resultados.find('/')]
        sets_resultados = sets_resultados[sets_resultados.find('/')+1: sets_resultados.__len__()]
        resultado_set4 = sets_resultados[0:sets_resultados.find('/')]
        sets_resultados = sets_resultados[sets_resultados.find('/')+1: sets_resultados.__len__()]
        resultado_set5 = sets_resultados

        #añadimos los datos limpios al array dataRresultados
        self.dataResultados.append(numero)
        self.dataResultados.append(equipo1)
        self.dataResultados.append(equipo2)
        self.dataResultados.append(fecha)
        self.dataResultados.append(hora)
        self.dataResultados.append(sets_ganados_equipo1)
        self.dataResultados.append(sets_ganados_equipo2)
        self.dataResultados.append(resultado_set1)
        self.dataResultados.append(resultado_set2)
        self.dataResultados.append(resultado_set3)
        self.dataResultados.append(resultado_set4)
        self.dataResultados.append(resultado_set5)





    def __procesa_resultado(self, item):

        equipos = item.find_all('td')[0].get_text()
        fecha_hora = item.find_all('td')[1].get_text()
        sets_resultados = item.find_all('td')[2].get_text()

        self.__clean_resultados(equipos,fecha_hora,sets_resultados)

    def __procesa_clasificacion(self, item, jornada):

       # posicion equipo ptos j g3 g2 p1 p0 sf sc pf pc sanciones
       self.dataClasificacion.append(jornada)

       for itemTd in item.find_all('td'):
           self.dataClasificacion.append(itemTd.get_text())

    def scrape(self):
        i = 1
        while i != 6:
            #content = requests.get("https://intranet.rfevb.com/rfevbcom/includes-html/competiciones/clasificacion321-conEncuentros-datos.php?IdCampeonato="+'4059'+"&Jornada="+str(i)).content
            # bucle en la jornada del 1- 23 (interessants del 1- 5)
            all_trs = BeautifulSoup(requests.get("https://intranet.rfevb.com/rfevbcom/includes-html/competiciones/clasificacion321-conEncuentros-datos.php?IdCampeonato="+'4059'+"&Jornada="+str(i)).content).findAll('tr')

            i = i+1
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
                    self.__procesa_resultado(item)

                elif es_clasificacion:
                    self.__procesa_clasificacion(item, i-1)
                elif es_proximos_encuentros:
                    continue

    def resultadosToCSV(self, filename):

        file = open( filename, "w+")


        fieldnames = ['Numero', 'Equipo1', 'Equipo2','Fecha', 'Hora', 'Sets_ganados_equipo1', 'Sets_ganados_equipo2', 'Resultado_set1','Resultado_set2','Resultado_set3','Resultado_set4','Resultado_set5']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        contador = 0

        while contador < self.dataResultados.__len__():
            writer.writerow({'Numero': self.dataResultados[contador], 'Equipo1': self.dataResultados[contador + 1], 'Equipo2': self.dataResultados[contador + 2],
                             'Fecha': self.dataResultados[contador+3],  'Hora': self.dataResultados[contador+4], 'Sets_ganados_equipo1': self.dataResultados[contador+5],
                             'Sets_ganados_equipo2': self.dataResultados[contador+6], 'Resultado_set1': self.dataResultados[contador+7],'Resultado_set2': self.dataResultados[contador+8],
                             'Resultado_set3':self.dataResultados[contador+9],'Resultado_set4': self.dataResultados[contador+10],'Resultado_set5':self.dataResultados[contador+11]})
            contador = contador + 12


    def clasificacionToCSV(self, filename):

        file = open(filename, "w+")

        fieldnames = ['jornada', 'posicion_equipo', 'ptos', 'j', 'g3', 'g2', 'p1', 'p0', 'sf', 'sc', 'pf', 'pc', 'sanciones']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        contador = 0

        while contador < self.dataResultados.__len__():
            writer.writerow({'jornada': self.dataClasificacion[contador], 'posicion_equipo': self.dataClasificacion[contador + 1], 'ptos': self.dataClasificacion[contador + 2],
                             'j': self.dataClasificacion[contador+3],  'g3': self.dataClasificacion[contador+4], 'g2': self.dataClasificacion[contador+5],
                             'p1': self.dataClasificacion[contador+6], 'p0': self.dataClasificacion[contador+7],'sf': self.dataClasificacion[contador+8],
                             'sc':self.dataClasificacion[contador+9],'pf': self.dataClasificacion[contador+10],'pc':self.dataClasificacion[contador+11],'sanciones':self.dataClasificacion[contador+12]})
            contador = contador + 13