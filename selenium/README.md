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


## Navigace

Pomocí metody `driver.get()` můžeme v prohlížeči otevřít danou URL.
Zda se nacházíme na správné adrese, anebo pro kontrolu, kam nás klikání našeho skriptu zavedlo, můžeme použít proměnnou `driver.current_url`.
Nadpis (title) aktuální stránky můžeme získat pomocí proměnné `driver.title`.

Příklad:

```python
from selenium import webdriver
import time


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


driver.get("https://www.idnes.cz")
time.sleep(1)

current_url = driver.current_url
title = driver.title
print(f"We are on URL '{current_url}' and title of this page is: {title}.")

driver.get("https://www.favu.vut.cz")
time.sleep(1)

current_url = driver.current_url
title = driver.title

print(f"We are on URL '{current_url}' and title of this page is: {title}.")


driver.close()
```

## Waits - čekání na načtení prvku

### time.sleep()

Může nám pomoci počkat na donačtení některého z elementů.
Také je praktický pro to, aby náš skript před stránkou vypadal pomaleji a tedy více jako reálná osoba (tomu můžeme pomoci také randomizací časů).
Pokud nám však jde o efektivní čekání na načtení prvků, je Sleep spíš relativně primitivní řešení, Selenium nám nabízí řadu propracovanějších, které si ukážeme níže.

### Implicit wait

Pomocí metody `driver.implicitly_wait()` můžeme nastavit dobu, po kterou budou na načtení prvku čekat všechny funkce lokalizující elementy.
Pozor: není dobré kombinovat Implicit a Explicit wait.

```python
driver = Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
```
### Explicit wait

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

driver.get("https://seznam.cz")

wait = WebDriverWait(driver, timeout=30) #nastavime timeout
element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p"))) #cekame na lokalizaci prvku
print("ELEMENT BY TAG NAME:", element)

wait = WebDriverWait(driver, timeout=60)
element = wait.until(EC.presence_of_element_located((By.ID, "non-existing-id"))) #zde si pockame... az nakonec bude error - element na strance neexistuje
print("ELEMENT BY ID:", element)

driver.close()
```

### Fluent Wait

```python
driver = Firefox()
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
```

## Hledání prvků

Elementy nejčastěji vyhledáváme pomocí metody `driver.find_element(by: str, value: str)`.
Jako první argument specifikujeme lokátor, jakým chceme vyhledávat, jako druhý pak hodnotu, kterou hledáme.
Dostupné lokátory jsou:

```
"class name" -	Locates elements whose class name contains the search value (compound class names are not permitted)
"css selector" -	Locates elements matching a CSS selector
"id"	- Locates elements whose ID attribute matches the search value
"name" -	Locates elements whose NAME attribute matches the search value
"link text"	- Locates anchor elements whose visible text matches the search value
"partial link text"	- Locates anchor elements whose visible text contains the search value. If multiple elements "are matching" - only the first one will be selected.
"tag name" - Locates elements whose tag name matches the search value
"xpath"	- Locates elements matching an XPath expression
```

Všechny lokátory jsou dostupné také jako konstanty v `selenium.webdriver.common.by.By`, který můžeme naimportovat a používat tímto způsobem:

```python
from selenium.webdriver.common.by import By

elem = driver.find_element(By.CLASS_NAME, "small")
elem = driver.find_element(By.ID, "password")
elem = driver.find_element(By.XPATH, "small")

# vrchni tri volani funkci jsou to stejne jako:
elem = driver.find_element("class name", "small")
elem = driver.find_element("id", "password")
elem = driver.find_element("xpath", "small")
```

### Jak zjistit XPATH / ID / NAME prvku

Efektivní způsob pro zjištění xpath, id, name či jiné hodnoty hledaného prvku na stránce je v prohlížeči otevřít developerskou konzoli (CTRL+SHIFT+C) a následně najet na prvek na stránce myší.
V konzoli se nám poté zvýrazní část kódu, která odpovídá označeného prvku-tagu.
Z něj můžeme vyčíst ID, name, class či jiné prvku.
Případně (asi nejjednodušší způsob) můžeme na tento kód tagu kliknout pravým tlačítkem myši a dát "copy full xpath" a xpath následně překopírovat do našeho skriptu.

### Relativní lokátory

Dalším způsobem je v Seleniu 4 použít tzv. relativní lokátory, pomocí kterých můžeme specifikovat pozici hledaného prvku vůči některému jinému prvku, který se lépe vyhledává.
Typickým použitím je situace, kdy například některý prvek má dané ID, které se velmi dobře vyhledává.
Pod tímto prvkem je poté jiný prvek, který ID nemá a máme problém k němu najít vhodnout xpath či podobně.
Pomocí relativních lokátorů můžeme najít prvek s ID a poté hledat prvek, který je pod ním, čímž se dostaneme k prvku, který jsme chtěly*i najít.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
passwordField = driver.find_element(By.ID, "password")
emailAddressField = driver.find_element(locate_with(By.TAG_NAME,  "input").above(passwordField))
```

Dokumentace relativních lokátorů je dostupná na: https://www.selenium.dev/documentation/webdriver/elements/locators/#relative-locators.

## Interakce s prvky

### Click

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

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


# Navigate to url
driver.get("http://www.google.com")

# Enter "umeni" text and do nothing
text_field = driver.find_element(By.NAME, "q")
text_field.send_keys("umeni" + Keys.ENTER)

# Click on search button
search_button = driver.find_element(By.NAME, "btnK")
search_button.click()

driver.close()
```

### Send keys

Pomocí metody `send_keys()` můžeme do prvky zadávat text:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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


# Navigate to url
driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action
text_field = driver.find_element(By.NAME, "q")
text_field.send_keys("webdriver" + Keys.ENTER)

driver.close()
```

### Clear

Metodou clear můžeme mazat zadaný text v textovém, případně jiné uživatelem*kou editovatelném poli:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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


# Navigate to url
driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action
text_field = driver.find_element(By.NAME, "q")
text_field.send_keys("webdriver" + Keys.ENTER)
text_field.clear()

driver.close()
```

## Informace z elementu

Plná dokumentace dostupná na: https://www.selenium.dev/documentation/webdriver/elements/information/

### Text

```python
text = driver.find_element(By.CSS_SELECTOR, "h1").text
```

### HTML Atribut

Pomocí metody `getAttribute()` můžeme získat hodnoty HTML atributu daného elementu, například atributu `href`, který drží HTML odkaz, na který prvek odkazuje:

```python
link_url = driver.findElement(By.ID, "muj-link").getAttribute('href')
```

## Low-level interakce

Velmi podrobná a jemná interakce je možná skrze Actions API, jejíž dokumentace je dostupná na: https://www.selenium.dev/documentation/webdriver/actions_api/
