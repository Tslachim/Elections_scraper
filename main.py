"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Michal Stuchlík 
email: tslachim@gmail.com
discord: Mišakus#1763
"""

import sys
import csv
import html

from requests import get
from bs4 import BeautifulSoup as bs


# Scraper pro informace -->> vypíše mi to ze zvolené stránky kódy a města 
def scraper_city_info(web: str,) -> dict: 
    """ Get city Id and names """
    response = get(web)
    soup = bs(response.text, features="html.parser")
    selection_code = soup.find_all(name= "td", class_= "cislo")
    codes = [code.getText() for code in selection_code]
    selection_city = soup.find_all(name= "td", class_= "overflow_name")
    if selection_city == []:                                                # Ošetření kvůli Brnu :D
        selection_city = soup.find_all(name= "td", headers="t1sa1 t1sb2") 
    cities = [code.getText() for code in selection_city]
    return codes, cities

codes = scraper_city_info(sys.argv[1])[0] 
cities = scraper_city_info(sys.argv[1])[1]                                  # změnit na sys.argv[1]

# Spojení odkazů webů 
def conection_links(new_web_pages):
    web_main = "https://www.volby.cz/pls/ps2017nss/"
    city_web = [(web_main+web) for web in new_web_pages]
    return city_web

# Získám odkazy k městům 
def next_web():
    web = sys.argv[1]                                                        # taky potřeba změnit na sys.argv[1]
    response = get(web)
    soup = bs(response.content, "html.parser")
    adress_endings = [one_td.find('a')['href'] for one_td in soup.find_all('td', class_='cislo') if one_td.find('a')]
    return conection_links(adress_endings)

city_web = next_web()

# Hlavní popisky Id, město .... pro hlavičku .csv souboru 
def get_title():  
    """ Get names for Title in .csv """
    titles = ["Code", "Location", "Registred", "Envelopes", "Valid"]
    response = get(city_web[0])                                              # libovolná stránka z těcho stranek, chci jen názvy stran
    soup = bs(response.text, features="html.parser")
    selection = soup.find_all(name= "td", class_= "overflow_name")
    groups = [group.getText() for group in selection]
    headers = titles + groups
    return headers

headers = get_title()                                                         # nadpisy pro soubor csv

# Pro každý odkaz potřebuji udělat scraper informací k danému městu
def all_city_info():
    all_city_information = []
    for index in range(len(city_web)):
        response = get(city_web[index -1])                                     # tady místo odkazu přiřadit city_web (získané stránky)
        soup = bs(response.content, "html.parser")
        information_city = []

        # získání prvního čísla počet voličů
        number = (soup.find("td", headers="sa2" )).getText()
        number = html.unescape(number)
        information_city.append(number)

        # získání počtu obálek 
        number_1 = (soup.find("td", headers="sa3" )).getText()
        number_1= html.unescape(number_1)
        information_city.append(number_1)

        # získání neplatných hlasů 
        number_2 = (soup.find("td", headers="sa6" )).getText()
        number_2 = html.unescape(number_2)
        information_city.append(number_2)

        # print(information_city[0], information_city[1], information_city[2])
        for num in soup.find_all("td", headers="t1sa2 t1sb3"):
            information_city.append(html.unescape(num.getText()))

        for num in soup.find_all("td", headers="t2sa2 t2sb3"):
            information_city.append(html.unescape(num.getText()))
        all_city_information.append(information_city)
    return all_city_information

all_city_information = all_city_info()

# přidání codes a cities do daného listu 
if len(all_city_information) > 1:
    for index in range(len(all_city_information)):   
        all_city_information[index - 1].insert(0, codes[index - 1])             # napsat pokud je len(all_city_information pro Brno (zatím nefunguje)!! myslím si že je malý index nebo tak něco)
        all_city_information[index - 1].insert(1, cities[index - 1])
else: 
    all_city_information[0].insert(0, codes[0])
    all_city_information[0].insert(1, cities[0])

with open(sys.argv[2], mode="w", encoding='utf-8', newline='') as new:
    writer = csv.writer(new, delimiter=';')
    writer.writerow(headers)
    for line in all_city_information:
        writer.writerow(line)

    
# Zapisuj přes argv stránku z výběru X a jméno souboru.csv