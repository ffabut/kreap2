# Úvod do Tornado

## Instalace

1. vytvořit virtuální prostředí, pokud již nemáme: `python -m venv .venv`
2. aktivovat virtuální prostředí: `source .venv/bin/activate`
3. instalace Tornado

```
pip install tornado
```

## Hello World v Tornado

Hello World v Tornado vypadá relativně jednoduše:

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```
O co přesně jde?
V začátku z tornada importujeme dva submoduly: tornado.ioloop, který řeší konkurentní vyřizování requestů, a tornado.web, což je kód obstarávající samotný webový server.

Dále následuje definice třídy MainHandler - všimněme si, že tato třída dědí ze třídy tornado.web.RequestHandler.
Jde o Reqeust Handler, tedy kód, který řeší příchozí HTTP requesty.
V této třídě MainHandler poté definujeme metodu (funkci) `get`, která říká, co má tato třída dělat v případě, když přijde HTTP request GET.
A to co se v tomto případě stane je to, že se pomocí zděděné metody `write()` pošle odpověď "Hello, world".
Namísto write bychom mohli použít nějakou jinou metodu zděděnou z třídy tornado.web.RequestHandler - například `render()`, která umožňuje generovat komplexnější odpověď z HTML templatu.
Také bychom mohli definovat další funkce pro ostatní HTTP metody jako POST, či PUT.

Dále definujeme funkci make_app(), která vrací výsledek funkce tornado.web.Application() - vrací z dodaných parametrů defacto plně nastavený a připravený webový server.
Parametry, které předáváme této funkci je seznam tuplů, které označují, jaké handlery používáme.
V tomto případě máme pouze jeden handler: `(r"/", MainHandler)`.
První hodnota v tomto tuple je regulérním výrazem, jde o vyjádření toho, jaké adresy na našem serveru zapadnou do tohoto výrazu a na základě toho bude volána funkce MainHandler.
Tento náš handler odpovídá pouze na `"/"`, tedy na index page našeho webu.
Pokud bychom chtěli, aby reagoval třeba na `/users`, pak bychom jej zapsali takto: `(r"/users", MainHandler)`.

Poslední částí tohoto kódu je podmínka `if __name__ == "__main__"`.
Tato podmínka je platná pouze v případě, když kód není importován, ale je přímo spuštěn - práve v tomto případě je totiž speciální proměnná `__name__` nastavena na hodnotu `"__main__"`.
Pokud bychom tento kód někam importovali jako modul, bylo by obsahem proměnné `__name__` název tohoto modulu.

V podmínce dále voláme funkci `make_app()`, která připraví web server a uložíme výsledek do proměnné `app`.
Poté pomocí `app.listen(8888)` nastavíme, aby server poslouchal na portu 8080.
Zavoláním `tornado.ioloop.IOLoop.current().start()` spustíme IOLoop, což je tornadový kód, který začne řešit přicházející requesty a konkurentně je odbavovat - zde defacto skutečně startujeme náš webový server.

Teď můžeme nasměrovat náš browser na `http://localhost:8080` a uvidíme vzkaz `Hello, world`.
Gratulace, právě jste spustili váš první webový server! :)

## V čem je to jiné než HTML soubor?

Narozdíl od prostého HTML souboru, který zprostředkovává server jako statický web, můžeme v Tornadu ve funkci `get()` napsat libovolný kód a unikátně tak generovat výstupu, které se na stránce objeví.
Zkusme nyní třeba místo textu `"Hello world"`, generovat náhodná čísla:

```python
import tornado.ioloop
import tornado.web
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        x = random.randint(0,30)
        self.write("HI! Your lucky number for today is: " + str(x) + "!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

Server nyní bude při každé návštěvě generovat unikátní odpověď.
Podobné chování by šlo udělat pomocí JavaScriptu na straně uživatelky, ale tam bychom si mohli otevřít v prohlížeči kód stránky a podívat se, jak se to generuje a v jakém rozmezí.
V případě generování na straně serveru takovou možnost nemáme - vidíme pouze výsledek.
A nikdy se nemůžeme být jistí, zda se generují čísla mezi 10 a 20, 0 a 30 nebo třeba -30000 a 30000 a my jen máme štěstí na ty čísla mezi 0 a 30.
