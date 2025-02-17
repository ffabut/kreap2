import tornado.ioloop
import tornado.web

#jednoducha ukazka toho, jak prijimat data skrze POST request
#na index page se zobrazuje index.html soubor, ktery obsahuje html <form> pro zadani dat
#zadana data se posilaji jako POST request na adresu /enterdata
#kde je zpracuje EnterDataHandler pomoci metody post()

class MainHandler(tornado.web.RequestHandler):
    """
    MainHandler obstarava index page na adrese "/"
    """
    def get(self):
        self.render("index.html")

class EnterDataHandler(tornado.web.RequestHandler):
    """
    EnterDataHandler obstarava adresu "/enterdata"
    """
    def get(self):
        # o GET request na adrese /enterdata nestojime
        # kdyby nahodou GET request dosel, tak presmerujeme na "/", kde je stranka pro zadani dat
        self.redirect("/") 

    def post(self):
        # u POST requestu zpracujeme prichozi data

        # jmeno argumentu se musi shodovat s tim, jak je pojmenovane pole ve formulari <form>
        jmeno = self.get_argument("name") #pokud nezadame pojmenovany parametr "default", pak dojde k chybe pri nedodani dat
        email = self.get_argument("mail", default="email") #pokud zadame default, pak pri nedodani dat se pouzije hodnota v default
        
        self.write(jmeno + " " + email) #nakonec vratime stranku s jednoduchym echem vlozenych dat
        #pripadne taky muze byt render() nebo redirect()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), #hlavni handler pro index page
        (r"/enterdata", EnterDataHandler), #handler pro adresu, kam se POSTuji data
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()