import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.escape import json_encode
# importujeme funkci json_encode, kterou nabizi tornado v modulu escape

# toto je ukázka jak přes Websocket pomocí json_encode() posílat slovník
# a v JS jej poté dekódovat zpět na slovník a použít

class MainHandler(tornado.web.RequestHandler):
    """
    MainHandler obstarava index page na adrese "/"
    """
    def get(self):
        self.render("index.html")
 
class WebSocketHandler(tornado.websocket.WebSocketHandler): # pozor neimportujeme bezny tornado.web.RequestHandler
    """
    WebSocketHandler obstarava Websocket komunikaci na adrese /websocket
    """
    def open(self): #vola se pri otevreni komunikace / pripojeni prohlizece
        zprava = {u"name": u"server", u"message": u"Vítáme vás na chatu!", u"time": u"nyní"}
        #prevedeme slovnik zprava do json pomoci funkce json_encode(), kterou jsme importovali z tornado.escape
        encoded_zprava = json_encode(zprava)
        self.write_message(encoded_zprava) # odesleme zpravu/slovnik zakodovanou jako JSON pres websocket

    def on_message(self, message): #pri prichodu nove zpravy
        zprava = {u"name": u"Ondřej", u"message": u"Ahoj lidi!", u"time": u"9:18"}
        #prevedeme slovnik zprava do json pomoci funkce json_encode(), kterou jsme importovali z tornado.escape
        encoded_zprava = json_encode(zprava)
        self.write_message(encoded_zprava) # odesleme zpravu/slovnik zakodovanou jako JSON pres websocket

    def on_close(self): #pri uzavreni komunikace / odpojeni prohlizece
        print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSocketHandler),
        (r"/src/(.*)", tornado.web.StaticFileHandler, {"path": "src/"}),
        # pouzivame primo bez uprav tornado.web.StaticFileHandler
        # ten slouzi k zobrazovani statickych souboru (.js, .css, .jpeg atd...)
        # zde ho mame kvuli souboru websocket.js - jinak by se nedal nacist
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
