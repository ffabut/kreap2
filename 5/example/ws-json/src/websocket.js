var ws = new WebSocket("ws://localhost:8888/websocket");

ws.onopen = function() {
   //vytvorime slovnik predstavujici zpravu (kdo, co)
   hello = {"message": "Hello Server!", "name": "client (browser)", "time": "16:15"}
   
   //slovnik prevadime do JSON retezce pomoci funkce JSON.stringify()
   message = JSON.stringify(hello)
   ws.send(message); //odesleme retezec ve formatu JSON
};

ws.onmessage = function(event) {
   var obj = JSON.parse(event.data); //prichozi zpravu dekodujeme pomoci funkce JSON.parse()

   //k prvkum dekodovaneho objektu obj jiz muzeme pristupovat jako k prvkum klasickeho slovniku
   alert("uživatel(ka) " + obj["name"] + " napsal(a) v " + obj["time"] + ": " + obj["message"])
};
