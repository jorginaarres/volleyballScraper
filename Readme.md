<h1>Pràctica 1: Web scraping </h1>
<h2>Descripció de VolleyScraper </h2>
Aquest repositori conté un web scraper fet la realizació de la Pràctica 1 de l'assignatura Tipologia i cicle de vida de les dades del Màster en Ciència de Dades de la UOC.

El volleyScraper extreu dades dels resultats i de les classificacions de la Real Federación Española de Voleibol, en concret els resultats de la Primera Divisió Femenina Grup A Classificació. Tenint en compte les diferents jornades.

Web de la federació: http://www.rfevb.com/primera-division-femenina-grupo-a-clasificacion
<h2>Autors de la pràctica</h2>

Aquesta pràctica l'he desenvolupat, de forma individual.

Autora: <b>Jorgina Arrés Cardona</b>

<h2>Descripció dels fitxers</h2>

- <b>main.py:</b> Encarregat d'iniciar l'scrapping i cridar-lo per guardar les dades en els csv
- <b>volleyScraper.py:</b> Implementació de l'scraper dels resultats de voleibol

Per poder executar l'script s'han de seguir els següents passos: 
1. Instal·lar dependències/llibreries amb la seguent comanda: 
    
    pip install requirements.txt
2. Executar:

    python main.py