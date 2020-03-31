var ws = new WebSocket("ws://localhost:8888/websocket");

ws.onopen = function() {
   ws.send("Hello, world");
};

ws.onmessage = function(event) {
   var obj = JSON.parse(event.data);

   alert("uživatel(ka) " + obj["name"] + " napsal(a) v " + obj["time"] + ": " + obj["message"])
};
