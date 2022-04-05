# Selenium: data-mining a automatizace prohlížeče

Selenium je externí modul určený pro interakce s prohlížeči (podporované jsou: Chrome - a varianty jako Chromium, Brave, dále Firefox, Edge, Safari).
Pomocí Selenia můžeme řídit prohlížeč - navigovat na různá URL, získávat informace o zobrazených HTML tags a také s nimi interagovat.
Jelikož HTML není pouze staženo jako v případě Requests+BeautifulSoup4, ale přímo zobrazeno v prohlížeči, má Selenium několik výhod:

1. na stránkách funguje JavaScript
2. před webovým serverem vypadáme více jako "běžný\*á uživatel\*ka"
3. můžeme interagovat s prvky - klikat na tlačítka, vyplňovat formuláře atd.
   
Selenium se obecně využívá pro testování webových stránek, pro naše účely nás však může zajímat též využití pro data-mining (např. login a projíždění timelines) či automatizování interakcí (boti, intervence do webů a platforem).

## Instalace

Selenium je externí modul, je tedy třeba jej nejprve nainstalovat pomocí pipu: `pip install --user selenium`.
V této lekci budeme používat nejnovější verzi Selenia, tedy Selenium 4.
Dejte pozor, abyste nainstaloval*a Selenium 4, některé názvy funkcí a další detaily v příkladech se můžou u Selenia 3 dost výrazně odlišovat.

Po instalaci Selenia je potřeba ještě nainstalovat `driver` pro prohlížeč, který chceme používat (více informací k procesu je možné získat v oficiální [dokumentaci Selenia](https://selenium-python.readthedocs.io/installation.html#drivers)).
Pro zjednodušení procesu však můžeme též využít automatizované řešení skrze externí modul `webdriver_manager`, který za nás nainstaluje aktuální verzi driveru úplně automaticky (podporuje Chrome, Chromium, Brave, Firefox, Internet Explorer, Edge, Opera).
Pro instalaci `webdriver_manager` stačí zavolat pip: `pip install --user webdriver_manager`.
V těchto materiálech budeme využívat `webdriver_manager`.

Posledním krokem je ověření, že náš prohlížeč je v PATH našeho systému, v terminálu můžeme např. zavolat:

```
firefox.exe
```

a ověřit, že spustitelný soubor byl nalezen (mělo by se otevřít okno prohlížeče).
Pokud se otevřelo, můžeme začít se Seleniem!

## Hello world

```python
from selenium import webdriver #ridi vytvoreni okna, ustredni modul
import time #pro sleep


#CHROME
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #vytvorime okno prohlizece, instalaci driveru resi webdriver_manager

#FIREFOX:
#from selenium.webdriver.firefox.service import Service
#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

#EDGE:
#from selenium.webdriver.edge.service import Service
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
#driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))


driver.get("https://www.artalk.cz") #nacteme URL
time.sleep(1) #spanek pro lepsi citelnost procesu (ci maskovani se za realneho cloveka)

elem = driver.find_element(by="id", value="search-text") #vyhledame element podle ID, kterou ma search field na artalku nastaveny na "search-text"

elem.send_keys("Miloš Zeman") #do elementu posleme text - jako by uzivatel*ka skutecne psal*a
time.sleep(1) 
elem.send_keys("\n") #posilame enter pro odeslani hledani

time.sleep(10) #zde cekame, abychom si mohly*i prohlednout vysledky
driver.close()

```

Pro návod, jak skrze `webdriver_manager` spustit jiné prohlížeče, shlédněte [oficiální dokumentaci](https://github.com/SergeyPirogov/webdriver_manager) `webdriver_manager`. 



