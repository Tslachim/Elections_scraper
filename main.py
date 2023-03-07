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

if len(sys.argv) != 3:
    print("Program musí být spuštěn s dvěma argumenty, adresou webové stránky a názvem výstupního souboru.")
    sys.exit()
else:
    print("Kontroluji zadané argumenty...")

if not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
    print("První argument musí být platnou adresou webové stránky.")
    sys.exit()

if not sys.argv[2].endswith(".csv"):
    print("Druhý argument musí být název souboru s příponou .csv.")
    sys.exit()
else:
    print("Byl zadán správný typ pro vytvoření souboru...")

response = get(sys.argv[1])
soup = bs(response.text, features="html.parser")

if response.status_code < 200 or response.status_code > 299:  # kontrola kódu HTTP odpovědi
    print(f"Chyba při načítání stránky: {response.status_code}, pravděpodobně je zadána nesprávná adresa")
    sys.exit()
else: 
    print("Webová stránka se zdá být v pořádku...")

def scraper_city_info(soup) -> dict:                                       # Scraper pro informace -->> vypíše mi to ze zvolené stránky kódy a města 
    """ Get city Id and names """
    selection_code = soup.find_all(name= "td", class_= "cislo")
    codes = [code.getText() for code in selection_code]
    selection_city = soup.find_all(name= "td", class_= "overflow_name")
    if selection_city == []:                                                    # Ošetření kvůli Brnu :D
        selection_city = soup.find_all(name= "td", headers="t1sa1 t1sb2") 
    cities = [code.getText() for code in selection_city]
    return codes, cities

codes = scraper_city_info(soup)[0] 
cities = scraper_city_info(soup)[1]

def conection_links(new_web_pages):                                             # Spojení odkazů webů
    web_main = "https://www.volby.cz/pls/ps2017nss/"
    city_web = [(web_main+web) for web in new_web_pages]
    return city_web

def next_web():                                                                 # Získám odkazy k městům
    web = sys.argv[1]
    soup = bs(response.content, "html.parser")
    adress_endings = [one_td.find('a')['href'] for one_td in soup.find_all('td', class_='cislo') if one_td.find('a')]
    return conection_links(adress_endings)

city_web = next_web()

def get_title():                                                                # Hlavní popisky Id, město .... pro hlavičku .csv souboru
    """ Get names for Title in .csv """
    titles = ["Code", "Location", "Registred", "Envelopes", "Valid"]
    response = get(city_web[0])                                                 # libovolná stránka z těcho stranek, chci jen názvy stran
    soup = bs(response.text, features="html.parser")
    selection = soup.find_all(name= "td", class_= "overflow_name")
    groups = [group.getText() for group in selection]
    headers = titles + groups
    return headers

headers = get_title()

def all_city_info():                                                            # Pro každý odkaz potřebuji udělat scraper informací k danému městu
    all_city_information = []
    for index in range(len(city_web)):
        response = get(city_web[index -1])
        soup = bs(response.content, "html.parser")
        information_city = []

        
        number = (soup.find("td", headers="sa2" )).getText()                    # získání prvního čísla počet voličů
        number = html.unescape(number)
        information_city.append(number)

        
        number_1 = (soup.find("td", headers="sa3" )).getText()                  # získání počtu obálek 
        number_1= html.unescape(number_1)
        information_city.append(number_1)

        
        number_2 = (soup.find("td", headers="sa6" )).getText()                   # získání neplatných hlasů 
        number_2 = html.unescape(number_2)
        information_city.append(number_2)

        for num in soup.find_all("td", headers="t1sa2 t1sb3"):
            information_city.append(html.unescape(num.getText()))

        for num in soup.find_all("td", headers="t2sa2 t2sb3"):
            information_city.append(html.unescape(num.getText()))
        all_city_information.append(information_city)
    return all_city_information

all_city_information = all_city_info()

if len(all_city_information) > 1:                                                # přidání codes a cities do daného listu
    for index in range(len(all_city_information)):   
        all_city_information[index - 1].insert(0, codes[index - 1])
        all_city_information[index - 1].insert(1, cities[index - 1])
else: 
    all_city_information[0].insert(0, codes[0])
    all_city_information[0].insert(1, cities[0])

with open(sys.argv[2], mode="w", encoding='utf-8', newline='') as new:
    writer = csv.writer(new, delimiter=';')
    print(f"Vytvářím soubor {sys.argv[2]} a zapisuji do něj data")
    writer.writerow(headers)
    for line in all_city_information:
        writer.writerow(line)
    
print(f"Váš nový soubor {sys.argv[2]} je vytvořen, program je ukonce.")
