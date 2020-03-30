# Lekce 2: Úvod do problematiky programování webového serveru

## Co je webový server?

Z praktického hlediska je `webový server` libovolný počítač s veřejnou IP adresou, který má otevřený port 80 (http) či 433 (https) a při požadavcích na tento port vrací webovou stránku - že něco vrací, co a jak přesně je otázkou softwaru, který můžeme na tento stroj nainstalovat, nebo si jej sami napsat.
Tento software se často také označuje za `webový server`.
S termínem `webový server` se tak můžeme setkat ve 2 různých kontextech:
- webový server jako hardware (s otevřenými porty, umístený v síti, nastavený, běží na něm software webového serveru)
- webový server jako software (právě to, co běží na hardwaru, obstarává to, že jsou uživatelkám vraceny HTML či jiné soubory)

## Jak to celé funguje v síti?

### URL -> DNS -> IP

Když zadáme do prohlížeče `URL` adresu webové stránky - například `favu.vut.cz` - tak se náš prohlížeč dotáže, jaká IP adresa odpovídá této URL.
K zjištění této informace použije místní DNS záznamy v počítači a případně DNS záznamy na serverech na internetu.
Jde vlastně o určitý překlad z dobře čitelné a zapamatovatelné adresy `URL` do těžce zapamatovatelné formy `IP` adresy.

### HTTP metoda GET 

Když prohlížeč konečně zjistí `IP` adresy, pak vyšle na tuto IP adresu vyšle HTTP request `GET` - informaci o tom, že chce získat stránku.
(Existují ještě požadavky POST, PUT, HEAD, DELETE, PATCH, OPTIONS - ty většinou slouží k manipulaci s daty na webovém serveru.)


### Porty 80 (HTTP) a 433 (HTTPS)

Požadavek `GET` poté směřuje na port 80 (http) či 433 (https) počítače s danou IP adresou - port se mění podle toho, zda jsme zadali url s protokolem `http://` nebo protokolem `https://`.
Počítač, jelikož je nastaven tak, aby byl webovým serverem, je připraven na tyto požadavky a proto má otevřené porty 80 a 433.

### Zpracování požadavku
Software-webový server zjistí tyto požadavky a pošle zpět danou webovou stránku - většinou jde o kombinaci HTML + CSS + JavaScript, ale může to být třeba jen obrázek nebo jiný soubor.
Prohlížeč dostane odpověď a zobrazí ji - nám se to potom prostě zdá jako `webová stránka`.
Způsob, jakým software zpracuje požadavek můžeme rozdělit do dvou skupin: statický a dynamický web.

### Statický web
V případě statického webu má server několik fixních HTML souborů a ty zprostředkovává návštěvnicím - každý pro danou `URL` dostane stejný soubor, stejnou stránku.
Soubory představující jednotlivé stránky se mění pouze jednou za čas - když se rozhodneme web aktualizovat, poté opět zůstávají stejné.

Statický web můžeme rozpohybovat/variovat/personalizovat pomocí JavaScriptu - ale rozhodně platí, že HTML, JavaScript a CSS soubory jsou pořád stejné - změny se dějí na straně prohlížeče, až na počítači nebo mobilu uživatelky.
Pomocí JavaScriptu není bezpečné modifikovat databáze, takže je prakticky skoro nemožné třeba udělat systém na vkládání komentářů nebo příspěvků - na to je dynamický web.

Statický web je ale levnější hostovat, spotřebovává méně elektřiny a je tedy ekologičtější.

### Dynamický web
Dynamický web označuje situaci, kdy webový server vrací v různých situacích různé varianty HTML souborů.
Často tak nejsou součástí takového webu jednotlivé HTML souboru, ale spíše jen HTML templaty, do kterých webový server vepisuje konkrétní data.
Webové stránky v tomto případě jsou tvořeny on-the-go, v momentě kdy přijde požadavek a pro každý požadavek zvlášť a různé.
V KREAP2 se zaměříme především na dynamické weby.

Nevýhodou dynamického webu je dražší hosting, větší spotřeba elektrické energie a větší uhlíková stopa.
Někdy je to ale potřeba. 

### Poznámky

1. server může vracet pro každou uživatelku naprosto jiné výsledky - klasicky `Facebook` vrátí každému z nás na adrese `facebook.com` naprosto jinou stránku - u Facebooku to očekáváme, ale pokud by to udělal například `idnes.cz` v článcích a městům a vesnicích zobrazoval jiné varianty článků, mohli bychom být lehce překvapené
2. software-webový server může běžet i na jiných portech než 80 nebo 433: pro lokální vývoj a testování se často používá port 8080, 8888, 8000 či jiné vyšší číslo, jejichž otevření nevyžaduje "administrátorská" práva a je bezpečnější. Pak do prohlížeče zadáváme adresu a uvádíme daný port: `htpp://localhost:8080`.
3. jiné porty než 80 a 433 se ale používají i v produkci - často je před webovým serverem ještě nastavená přesměrovací proxy, která požadavky na 80 a 433 přesměrovává na jiné porty, klidně 8080, a klidně i na několik různých strojů - pak jde o load balancing proxy, která zajišťuje distribuci náporu návštěvníků na více strojů zaráz.

## Začínáme programovat webový server (software)

### Webové frameworky v Python
Pro Python vznikla velká řada webových frameworků, která se liší tím, na co cílí a v čem jsou nejlepš.
Jedním z nejoblíbenějších frameworků je Django.
Dále potom například Flask, Pyramid nebo CherryPy.
Výkonným, ale složitějším je Twisted.

V kurzu KREAP2 se zaměříme na framework Tornado, který vyniká asynchronicitou (umožňuje současně obsluhovat velké množství uživatelů) a také nabízí podporu WebSockets - ty umožňují napojení webu například na Unity, PureData, Processing, nebo na komunikaci s jinými uživateli téže stránky.
Zároveň je Tornado relativně jednoduché a přitom umožňuje napsat si web podle svého - nevede tolik k šablonovitému uvažování jako Django, ale snad právě proto není tak efektivní pro komerční vyvíjení webů - v tom dominuje Django.

### Hello World v Tornado

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

### V čem je to jiné než HTML soubor?

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
