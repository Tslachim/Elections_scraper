Elections_scraper

Třetí a závěrečný projekt Engeto academie - Elections_scraper

Jedná se o projekt, který z stránek https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ vytáhne výsledky voleb pro danou oblast, podle vašeho výběru. Například Ostrava-město. Projekt stáhne výsledky voleb a uloží je do souboru .csv. 


Instalace potřebných knihoven
Je potřeba nainstalovat, pokud ještě nemáte, knihovny bs4 (BeautifulSoup) a knihovnu requests. Nicméně knihovny použité v kódu jsou uloženy v souboru requirements.txt.
Po vytvoření Virtuálního prostředí a aktivaci stáhněte knihovny pomocí příkazové řádky a to zadáním "pip install bs4" a "pip install requests" (bez uvozovek). 


Spouštění souboru
Soubort se spouští přes příkazovou řádku, kdy je potřeba zadat dva argumenty. 
První argument je URL adresa daného města, které chcete vyscrapovat. 
Druhý argument je název souboru .csv, který se vám následně vytvoří. 

Příklad spouštění souboru main.py vyžaduje dva povinné argumenty (je potřeba argument 1 a 2 zapsat do uvozovek):
PS C:\Projekty Engeto\Elections_scraper> Python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6202" "výsledky_voleb_Brno.csv"

