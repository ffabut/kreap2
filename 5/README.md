# Lekce 5: Interakce skrze websockets v Tornadu

Websocket je protokol pro komunikaci mezi serverem a prohlížečem.
Jeho hlavní výhodou je to, že je komunikace navázáná dlouhodobě - nové zprávy či požadavky tak může iniciovat jak prohlížeč (podobně jako při GET a POST requestech), ale především také server. 
Při použití Websocketů má server přehled o všech připojených uživatelích a může jim kdykoliv odeslat novou zprávu.

Protokol Websocket je uznaný konsorciem W3C a je podporovaný ve všech velkých současných prohlížečích, jde tedy o naprosto rozšířenou mainstreamovou technologii.

Protokol websocket (zkratka WS) může být také provozován skrze zabezpečenöu SSL komunikaci (podobně jako HTTPS), potom o něm hovoříme jako o `websocket secure` (zkratka WSS). 

## Websocket - klíčové pojmy

Websocketová komunikace je navazována ze strany prohlížeče, tedy od klienta k serveru.
Důvodem je to, že prohlížeč (aka zařízení, na kterém běží) nemusí mít pevně danou adresu, zatímco server pevně danou adresu má.

Samotná komunikace přes Websocket se potom odehrává ve třech fázích:
- otevření komunikace
- odesílání zprávy (může se opakovat)
- uzavření komunikace

### Adresa, na níž se otevírá WS komunikace

Websocket můžeme otevřít jak na indexu serveru (`/`), tak na libovolném dalším místě, třeba `/websocket` nebo `/ws/chat` atd.
Adresa serveru je stejná jako jeho běžná adresa zobrazená v prohlížeči.
Dejme se ale pozor, že prohlížeč zobrazuje adresu včetně HTTP nebo HTTPS protokolu.
Ty musíme změnit na protokol WS nebo zabezpečený WSS, změna bude vypadat například takto:

```
http://mujeserver.cz/websocket -> ws://mujserver.cz/websocket
https://myserver.com/ws/chat -> wss://myserver.com/ws/chat
```

Adresa může být samozřejmě i přímo IP adresa nebo localhost, případně může probíhat i na jiném portu než na základním 80 (HTTP) či 443 (HTTPS).
Tedy například takto:

```
http://114.21.20.120/ws -> ws://114.21.20.120/ws
http://localhost:8080/websocket -> ws://localhost:8080/websocket
```

## Začínáme s Websockets

Chceme-li začít používat websockety musíme připravit jak náš server, tak prohlížeč (donutit jej skrze JavaScript navázat spojení se serverem).

### Websocket na straně prohlížeče: JavaScript

K navázání Websocketové potřebujeme do HTML souboru vložit JavaScriptový skript a v něm definovat otevření komunikace a pak už jen odeslat zprávu.
Skript můžeme vložit buď přímo do HTML souboru mezi tagy `<script></script>`, anebo jej vložit do externího `.js` souboru a ten poté importovat: `<script src="skript.js"></script>`.

Základní skript pro otevření a odesílání zpráv skrz websocket může vypadat takto:

```javascript
// přes `new WebSocket()` vytváříme novou instanci třídy WebSocket (nový objekt z třídy WebSocket)
// jako parametr předáváme adresu, na kterou se má websocket připojit.
// Objekt uložíme do proměnné `ws`.
var ws = new WebSocket("ws://localhost:8888/websocket");

// definujeme (v základu je prázdná) metodu `ws.onopen`, kterou JavaScript volá při úspěšném otevření Websocketu
ws.onopen = function() {
  // zde určujeme, co se má stát
   ws.send("Hello, world"); //nechceme toho moc: prostě jen odešleme serveru pozdrav
};

// definujeme metodu `ws.onmessage`, kterou JS volá při obdržení zprávy
ws.onmessage = function(event) { //aby zpráva byla dostupná ve funkci, tak definujeme parametr event - pod tímto jménem poté bude dostupná přijatá zpráva
   alert(event.data); // prostě data zprávy zobrazíme v alert window
};
```

### Websocket na straně serveru: Tornado

Zprovoznění Websocketů v Tornadu je relativně dost podobné běžnému Handleru pro HTTP připojení (definování cesty, vytvoření handleru z třídy, metoda GET, případně POST).
Abychom nastavili server pro přijímání Websockets, budeme potřebovat:

1. zvolíme si cestu, na které chceme přijímat websockety (například `/ws`, `/websocket/chat` atd.) a přidáme ji do `make_app()`, například: `(r"/websocket",WebSocketHandler)`,
2. vytvoříme patřičně pojmenovanou třídu (v našem případě třeba `WebSocketHandler`), která bude dědit z `tornado.websocket.WebSocketHandler` (pozor: nikoliv z `tornado.web.RequestHandler`), tedy například: `class WebSocketHandler(tornado.websocket.WebSocketHandler)`
3. v této třídě popíšeme potřebné chování v metodách `open()` (volá se při otevření nového websocket spojení s každým novým klientem), `on_message()` (volá se při doručení zprávy) a `on_close()` (volá se při zavření websocketu s každým klientem).
4. zprávy můžeme odesílat pomocí metody `write_message()`, která je součástí třídy `tornado.websocket.WebSocketHandler`, z níž dědí náš objekt `WebSocketHandler`.

Jednoduchá implementace handleru pro websocket může vypadat například takto:

```python
#v make_app máme nastaveno: (r"/websocket", WebSocketHandler) 
class WebSocketHandler(tornado.websocket.WebSocketHandler): #pozor: dedime z tornado.websocket.WebSocketHandler, ne z bezneho tornado.web.RequestHandler
   def open(self): #vola se pri otevreni noveho websocket spojeni z prohlizece
         print("WebSocket opened") #proste jen vypisem, ze mame nove spojeni

   def on_message(self, message): #vola se pri nove zprave
         self.write_message(u"You said: " + message) #posleme zpravu pekne hned zpatky, takove echo

   def on_close(self): #vola se pri zavreni spojeni
         print("WebSocket closed") #proste jen vypisem, ze se to zavrelo
```

## Websocket: Hello World

Zde se podíváme na jednoduchý Hello World užívající Websocket (vlastně jde o echo server a zdravící prohlížeč).
Většinu kódu přebíráme z předchozích částí - `Websocket na straně prohlížeče: JavaScript` a `Websocket na straně serveru: Tornado`.
Celý příklad je dostupný ve složce `example/ws-hello-world`.

Jak tedy na Hello World?

1. jednoduchá HTML stránka importující JavaScript, který bude řídit Websocket komunikaci

```html
<!DOCTYPE HTML>
<html>

<head>
  <script src="src/websocket.js"></script>
</head>

<body>
  Tato stránka komunikuje přes websockety se serverem.
</body>

</html>
```

2. JavaScript kód řídící komunikaci skrze Websocket na straně prohlížeče:

```javascript
var ws = new WebSocket("ws://localhost:8888/websocket");

ws.onopen = function() {
   ws.send("Hello, world");
};

ws.onmessage = function(event) {
   alert(event.data);
};
```

3. Náš Tornado server bude vypadat takto:
```python
import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler):
   """
   MainHandler obstarava index page na adrese "/"
   """
   def get(self):
      self.render("index.html")
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
   def open(self):
      print("WebSocket opened")

   def on_message(self, message):
      self.write_message(u"You said: " + message)

   def on_close(self):
      print("WebSocket closed")

def make_app():
   return tornado.web.Application([
      (r"/", MainHandler),
      (r"/websocket", WebSocketHandler),
      (r"/src/(.*)", web.StaticFileHandler, {"path": "src"}),
      # pouzivame primo bez uprav tornado.web.StaticFileHandler
      # ten slouzi k zobrazovani statickych souboru (.js, .css, .jpeg atd...)
      # zde ho mame kvuli souboru websocket.js - jinak by se nedal nacist
   ])

if __name__ == "__main__":
   app = make_app()
   app.listen(8888)
   tornado.ioloop.IOLoop.current().start()
```

### Jak to celé funguje
1. prohlížeč si vyžádá index page na adrese `/`, Tornado odešle index.html, který importuje skript `src/websocket.js`
2. skript na adrese `src/websocket.js` zprostředkuje `web.StaticFileHandler`, takže se úzpěšně načte
3. načtený skript otevře Websocket připojení na adresu `ws://localhost:8888/websocket`, tedy zpět k serveru
4. Tornado na `/websocket` ma nastaveny WebSocketHandler zděděný z tornado.websocket.WebSocketHandler, který přijme komunikaci
5. při otevření komunikace JavaScript v metodě `onopen()` odešle zprávu `Hello World`
6. Tornado ji přijme v metodě `on_message()`, přidá před zprávu `You said: ` a pošle zprávu zpět
7. JavaScript při obdržení zprávy volá metody `onmessage()` v níž otevíráme alert okno a zobrazíme zprávu

## Websocket: posílání složitějších dat

Websocket umožňuje přenášet buď textové řetězce, anebo binární data (vhodné pro přenos opravdu větších objemů dat).
To je ale poněkud limitující, přecijen ke zprávě by bylo dobré dodat třeba kdo ji poslal, kdy, atd.
Na to se ideálně hodí slovník. Takže co budeme dělat, pokud chceme přenést slovník, anebo třeba seznam?
V takové situaci je ideální slovník nebo seznam zakódovat do JSONu (JavaScriptový formát pro strukturování dat v řetězcích), tento JSON odeslat jako text a později jej v JavaScriptu dekódovat a získat tak hodnoty obsažené ve slovníku anebo seznamu.

### Co je JSON

JSON neboli JavaScript Object Notation (JavaScriptový objektový zápis) je formát zápisu dat ve formě textu, který je nezávislý na platformě.
Umí tedy pracovat jak v nativním JavaScriptu, tak má podporu v Pythonu (i přímo v Tornadu), ale taky napříkla v jazyce Go, C++ a mnoha dalších.
Je to takový švýcarský nůž pro přenos datových objektů mezi různými jazyky.
Má i své alternativy jako třeba `YAML` (v něm jde vkládat komentáře).

Slovník v JSON může vypadat třeba takto:

```json
{
"name":"John",
"age":30,
"city": "London"
} 
```

A slovník obsahující seznam (prázdný i plný) třeba takto:

```json
{
"name":"John",
"age":30,
"city": "London",
"cars":[],
"bikes": ["Favorit", "Whyte", "SubRosa"]
} 
```

Stejně tak může být JSON zkrácen na jeden řádek, je to jedno zda obsahuje entery a odsazení nebo nikoliv:

```json
{"name":"John","age":30,"city": "London","cars":[],"bikes":["Favorit","Whyte","SubRosa"]} 
```

JSON je relativně komplexní téma samo o sobě, tyto příklady jsou spíše pro představu o tom, do jakého formátu zhruba budeme kódovat a dekódovat.
Nemusí nás to ale moc zajímat - do JSONu zakóduje Tornado a zpět dekóduje JavaScript, JSONu si tedy vlastně ani nemáme jak všimnout...


### Použití JSON v Tornadu

Tornado pro práci s JSONem nabízí modul `tornado.encode`, v němž je obsažená funkce `json_encode` pro zakódování do JSONu.
Prvně naimportujeme tuto funkci do Tornada: `from tornado.escape import json_encode`.
A poté můžeme odesílat slovníky nebo seznamy jako JSON následujícím způsobem:

```python
def open(self): #vola se pri otevreni komunikace / pripojeni prohlizece
   zprava = {u"name": u"server", u"message": u"Vítáme vás na chatu!", u"time": u"nyní"}
   #prevedeme slovnik zprava do json pomoci funkce json_encode(), kterou jsme importovali z tornado.escape
   encoded_zprava = json_encode(zprava)
   self.write_message(encoded_zprava) # odesleme zpravu/slovnik zakodovanou jako JSON pres websocket
```

Dekódování: TODO

### JSON v JavaScriptu

JSON je v JavaScriptu jako doma - je to formát spjatý s JavaScriptem, jeho použití je tedy velmi jednoduché.
Stačí přijatou zprávu ve formátu JSON dekódovat do objektu, z něhož potom můžeme dostat jednotlivé hodnoty, například takto:

```javascript
ws.onmessage = function(event) {
   var obj = JSON.parse(event.data); //dekodujeme JSON data do promene obj

   //potom jiz můžeme pristupovat k jednotlivým hodnotám v tomto objektu jako by to byl slovnik nebo seznam - dle toho, co jsme odeslali
   alert("uživatel(ka) " + obj["name"] + " napsal(a) v " + obj["time"] + ": " + obj["message"])
};
```


