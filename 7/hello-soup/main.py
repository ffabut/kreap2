import requests
from bs4 import BeautifulSoup
# pozor: beautifulsoup4 se nainstaluje jako bs4 a z nej potom importujeme podmodul BeautifulSoup

url = "https://onemocneni-aktualne.mzcr.cz/covid-19"
r = requests.get(url)

# zavolame funkci BeautifulSoup s prvnim parametrem retezcem HTML a v druhem specifikujeme parser - v zaklade se drzme dostupneho `html.parser`, ale lze nainstalovat i rychlejsi/blbuvzdornejsi atd...
soup = BeautifulSoup(r.text, 'html.parser')

# chceme pocet mrtvych
# to je element typy p (paragraph)
# a s id="count-dead"
# k vyhledavani elementu pouzivame metodu find_all()
matches = soup.find_all("p", id="count-dead")

#vezmeme prvni nalez (muze jich byt vic)
pocet = matches[0]

#v tomto jednom elementu se dostaneme k textovemu obsahu pres promennou/atribut text
dead = pocet.text
print("Mrtvých na COVID-19 v ČR je aktuálně dle MZČR:", dead)
