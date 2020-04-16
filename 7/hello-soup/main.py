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
# k vyhledavani elementu pouzijeme metodu find() - ta vrati prvni vyhovujici element
match = soup.find("p", id="count-dead")

# k textovemu obsahu elementu se dostaneme pres promennou/atribut text
print("Mrtvých na COVID-19 v ČR je aktuálně dle MZČR:", match.text)
