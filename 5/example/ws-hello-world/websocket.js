// přes `new WebSocket()` vytváříme novou instanci třídy WebSocket (nový objekt z třídy WebSocket)
// jako parametr předáváme adresu, na kterou se má websocket připojit.
// Objekt uložíme do proměnné `ws`.
var ws = new WebSocket("ws://localhost:8080/websocket");

// definujeme (v základu je prázdná) metodu `ws.onopen`, kterou JavaScript volá při úspěšném otevření Websocketu
ws.onopen = function() {
  // zde určujeme, co se má stát
   ws.send("Hello, world"); //nechceme toho moc: prostě jen odešleme serveru pozdrav
};

// definujeme metodu `ws.onmessage`, kterou JS volá při obdržení zprávy
ws.onmessage = function(event) { //aby zpráva byla dostupná ve funkci, tak definujeme parametr event - pod tímto jménem poté bude dostupná přijatá zpráva
   alert(event.data); // prostě data zprávy zobrazíme v alert window
};
