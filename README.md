Elections_scraper

Třetí a závěrečný projekt Engeto academie - Elections_scraper

Jedná se o projekt, který z stránek https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ vytáhne výsledky voleb pro danou oblast, podle vašeho výběru. Například Ostrava-město. Projekt stáhne výsledky voleb a uloží je do souboru .csv. 


Instalace potřebných knihoven

Je potřeba nainstalovat tyto knihovny, pokud ještě nemáte, knihovny bs4 (BeautifulSoup) a knihovnu requests. Nicméně knihovny použité v kódu jsou uloženy v souboru requirements.txt.
Po vytvoření Virtuálního prostředí a aktivaci stáhněte knihovny pomocí příkazové řádky a to zadáním "pip install bs4" a "pip install requests" (bez uvozovek). 


Spouštění souboru

Soubort se spouští přes příkazovou řádku, kdy je potřeba zadat dva argumenty. 
První argument je URL adresa daného města, které chcete vyscrapovat. 
Druhý argument je název souboru .csv, který se vám následně vytvoří. 

Příklad spouštění souboru main.py vyžaduje dva povinné argumenty (je potřeba argument 1 a 2 zapsat do uvozovek):

Příklad spouštění souboru main.py vyžaduje dva povinné argumenty (je potřeba argument 1 a 2 zapsat do uvozovek):
PS C:\Projekty Engeto\Elections_scraper> python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3203" "vysledky_Plzeň.csv"

Výstupem následně bude vámi pojmenovaný soubor "výsledky_Plzeň_.csv", který zobrazí tabulku s výsledky daného města.


Code;Location;Registred;Envelopes;Valid;Občanská demokratická strana;Řád národa - Vlastenecká unie ..........
558851;Dýšina;740;499;492;54;3;0;37;0;31;28;4;1;5;0;1;56;0;0;26;172;1;19;0;5;3;0;41;5;-
558966;Chrást;1 349;860;853;114;0;0;48;0;52;41;10;5;16;1;2;119;0;3;45;269;5;34;0;3;2;1;80;3;-
557846;Chválenice;1 429;1 002;999;151;1;1;51;1;31;63;8;4;15;1;2;111;1;1;45;354;1;24;0;11;5;2;114;1;-
559130;Kyšice;561;369;369;50;3;0;21;0;13;21;7;7;7;1;1;52;0;0;38;104;0;8;0;3;2;0;29;2;-
540561;Letkov;734;508;506;87;1;0;39;0;23;32;5;3;12;0;0;52;2;0;22;153;0;24;0;8;2;1;38;2;
