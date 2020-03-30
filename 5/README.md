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



