# Lekce 7: Jdeme online

Jednou z výhod webu běžícího na serveru, kterou jsme zatím neprobrali, je možnost získávat data z jiných míst na internetu, zpracovávat je, ukládat je a nakonec či rovnou je zobrazovat.
Se statickým webem a JavaScriptem něco takového přitom ve většině případů nemůžeme udělat.
Prohlížeče z bezpečnostních důvodů blokují přístup JavaScriptu k jiným doménám než k té, na které JavaScript běží (pokud připojení odkudkoliv domény vyloženě nepovolí).

Stáhnout tak pomocí JavaScriptu články z idnes.cz nebo webu armády ČR nelze, povolí nám to tak leda určité části wikipedie.
Náš webový server ale takovým problémům vystaven není a můžeme tak z něj stahovat libovolný obsah (dokud nebudeme úplně mega nápadní - 100 tis. stáhnutí z jednoho webu za hodinu není úplně dobrý nápad).

## Stažení souboru z webu - modul Requests

Pro stahování souborů z webu můžeme použít externí modul Requests, který je velmi oblíbený a to zejména pro svoji jednoduchost.

Jelikož jde o externí modul, který není v základu dostupný v Pythonu, musím modul prvně nainstalovat:

```
pip3 install --user requests
```

### Hello Downloads

Stažení souboru je relativně jednoduché:

```python
import requests

#adresa z ktere chceme stahovat, vcetne protokolu http/https
url = "https://www.favu.vut.cz/fakulta/historie-soucasnost"

# zde vytváříme HTTP GET request na danou adresu
r = requests.get(url) # vysledek stazeni je objekt tridy Response

# Response.status_code obsahuje kod odpovedi - 200 OK, 404 Not Found atd... 
print(r.status_code)

# Response.text je samotny text odpovedi
print(r.text)

# Muze jit o HTML, JSON, ale i binarni kod (kdyz stahujeme obrazek)
# r.text můžeme klidně hned vrátit v RequestHandler jako "naši" stránku
```

### Řídit stahování jako prohlížeč

HTTP GET požadavky obsahují řadu hlaviček (headers).
Ty "vyplňuje" program, který jsme k vykonání GET requestu použili.
Klasických příkladem parametru v hlavičce je tzv. `User-Agent`, který udává jaký operační systém a jaký prohlížeč GET request posílá.
Na základě této informace potom weby zobrazují například mobilní nebo klasické verze stránek.

Problém je v tom, že Python a Requests se v rámci headeru přiznají k tomu, že jsou Python a Requests a některé weby je mohou na základě toho blokovat - přece nechtějí, aby jim někdo těžil data ze stránky!

To můžeme obejít tím, že nastavíme `User-Agent` header na to, co ukazuje například náš běžný prohlížeč.
Informace o `User-Agent` a dalších headerech můžete zobrazit například na tomto webu: `http://myhttpheader.com/`.

V mém případě je to: `Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0`.
Používám operační systém Fedora, tedy Linux v 64 bitové podobě a prohlížeč Mozilla Firefox.
Pojďme teď stáhnout stránku a vydávat se za prohlížeč:

```python
#requests berou headers jako slovník název-headru a hodnota-headru
#vložíme tam tedy jeden záznam pro user-agent
headry={"User-Agent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0"}

# nyní zavoláme funkci get() s pojmenovaným parametrem headers
r = requests.get(url, headers=headry)
```

Server obsluhující dané URL si nyní bude myslet, že požadavek došel z prohlížeče a nikoliv z Pythonu.

## Vyhledávání ve staženém HTML souboru

Stažený HTML soubor je sice pěkný, ale často z něj potřebujeme jen něco - ne úplně všechno.
Buď v něm můžeme vyhledávat textově, anebo chytřeji - zkusit vyhledávat v rámci pravidel a logiky HTML.
K tomu slouží tzv. parsery HTML, které HTML soubor projdou a vytvoří nám z něj vnořený seznam HTML elementů, v rámci kterého můžeme vyhledávat podle ID, typu elementy, třídy elementu a dělat další pokročilé operace.
Je to podobné jako v případě JSON parseru, který převádí text ve formátu JSON do objektu použitelného v Pythonu.

Oblíbený modul pro HTML parsing v Pythonu je modul `BeautifulSoup4`.

### Instalace BeautifulSoup4

Pro instalaci BS4 použijeme pip3: `pip3 install --user beautifulsoup4`.

### Hello Soup

```python
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
# k vyhledavani elementu pouzivame metodu find() - vrati 1. vyhovujici element
# prvni parametr rika, jaky typ elementu chceme (p=<p>, a=<a>, div=<div>, span=<span>, img=<img> atd...)
# v pojmenovaném parametry ID muzeme specifikovat ID hledanych prvku
# v pojmenovanem parametru class muzeme specifikovat class hledanych prvku
match = soup.find("p", id="count-dead")


# v elementu se dostaneme k textovemu obsahu pres promennou/atribut .text
print("Mrtvých na COVID-19 v ČR je aktuálně dle MZČR:", match.text)
```

### Vyhledávání všech prvků: find_all()

Alternativou funkce `find()` je funkce `find_all()`, která nevrací pouze jeden nalezený element (první), ale vrací seznam všech vyhovujících elementů.
Použití je následující:

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://onemocneni-aktualne.mzcr.cz/covid-19")
soup = BeautifulSoup(r.text, 'html.parser')

matches = soup.find_all("p") #vyhledáme všechny odstavce na stránce
# matches je seznam prvků: [ element1, element2, element3 ]

print(matches) #vypis vsech nalezenych elementu
print("Prvni odstavec na strance obsahuje text:", matches[0].text)

print("celkem je na stránce:", len(matches), "odstavců.")
```

### Vychytávky s find() a find_all()

#### Vyhledávání podle třídy

`class` je v Pythonu klíčovým slovem, nemůžeme jej proto použít jako název parametru ve funkci:

```python
purple = soup.find("div", class="background--purple") # toto napise chybu
```

BeautifulSoup proto namísto `class` používá jako jméno parametru `class_`.
Vyhledávání podle třídy tedy bude vypadat takto:

```python
purple = soup.find("div", class_="background--purple")
```

#### Vyhledávání podle ostatních atributů

Můžeme vyhledávat i podle ostatních HTML atributů - jako jméno parametru zkrátka použijeme jméno hledaného atributu, například: 

```python
odkaz = soup.find("a", href="/") # odkaz na home - index page
obrazek = soup.find("img", src="1.jpeg")
```

##### Atributy můžeme kombinovat

```python
div = soup.find("div", class_="main", href="/")
```

### Zanořené vyhledávání

Někdy není možné se k prvku, který potřebujeme, dostat na první dobrou pomocí typu elementu, id, class a dalších parametrů.
V takovém případě musíme vyhledat rodiče kýženého prvku - a v něm poté vyhledávat dál (ovšem už hledáme pouze v rodičovi - nevyhledáme nechtěné matche jinde na stránce).

V elementech vyhledaných skrze `find()` a `find_all()` můžeme dále vyhledávat - zavoláme na nich opět funkci `find()` jako ji voláme na objektu `soup`, který představuje celé HTML.

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://onemocneni-aktualne.mzcr.cz/covid-19")
soup = BeautifulSoup(r.text, 'html.parser')

parent = soup.find("div", class_="background--purple") #najdeme fialovy div, ktery obsahuje par textu a cislo poctu hospitalizovanych
cislo = parent.find("p", class_="mt-5") # v ramci divu hledame odstavec tridy mt-5, ktery obsahuje nami kyzene cislo poctu hospitalizovanych

print("Počet hospitalizovaných:", cislo.text)
```
