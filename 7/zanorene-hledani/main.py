import requests
from bs4 import BeautifulSoup

r = requests.get("https://onemocneni-aktualne.mzcr.cz/covid-19")
soup = BeautifulSoup(r.text, 'html.parser')

parent = soup.find("div", class_="background--purple") #najdeme fialovy div, ktery obsahuje par textu a cislo poctu hospitalizovanych
cislo = parent.find("p", class_="mt-5") # v ramci divu hledame odstavec tridy mt-5, ktery obsahuje nami kyzene cislo poctu hospitalizovanych

print("Počet hospitalizovaných:", cislo.text)
