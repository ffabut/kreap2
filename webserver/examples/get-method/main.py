import tornado.ioloop
import tornado.web

#jednoducha ukazka toho, jak prijimat data skrze GET request diky query stringum v URL adrese
#na index page se zobrazuje index.html soubor, ktery obsahuje html <form> pro zadani dat
#zadana data se posilaji jako GET request na adresu /enterdata
#kde je zpracuje EnterDataHandler pomoci metody get()

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
        # v GET requestu pocitame s tim, ze skrze query string prichazi data
        # URL bude vypadat napriklad takto: /enterdata?name=Jane&mail=person%40mail.com
        #v query string jsou nektere specialni znaky prevedeny do zakodovanych retezcu,
        #napriklad @ je %40, ale tornado to za nas zase rozsifruje, takze to nemusime resit

        # jmeno argumentu (zde "name" a "mail") se musi shodovat s tim,
        # jak je pojmenovane pole ve formulari <form>
        jmeno = self.get_argument("name") #pokud nezadame pojmenovany parametr "default", pak dojde k chybe pri nedodani dat
        email = self.get_argument("mail", default="email") #pokud zadame default, pak pri nedodani dat se pouzije hodnota v default
        
        self.write(jmeno + " " + email) #nakonec vratime stranku s jednoduchym echem vlozenych dat
        #pripadne taky muze byt render() nebo redirect()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), #hlavni handler pro index page
        (r"/enterdata", EnterDataHandler), #handler pro adresu, kam se odesilaji data skrze GET request
                                           # jako tzv. query string skrze URL adresu
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()