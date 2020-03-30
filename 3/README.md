# Lekce 3: Templaty v Tornado Webserver

## Templates - jak generovat "pěknou" stránku

V minulé hodině jsme v RequestHandleru ke generování odpovědi-stránky používali metodu `write()` zděděnou z třídy `tornado.web.RequestHandler`.
Tato metoda je spíš jen základní a hodí se jen v začátku, případně pro debugování - výpis jednoduchých hodnot.
Pokud ale chceme generovat plnohodnotnější koukatelnou stránku, pak je lepší použít spíše metodu `render()`.

### Metoda render() - renderování templatů

Metoda `render()` umožňuje vložit proměnné do předlohového templatu a ten poté vrátit jako výslednou stránku.
Template je přitom defacto hotová HTML stránka, v níž se však vyskytují pasáže označující místa, do kterých se mají vkládat proměnné.
Jméno templatu předáváme jako atribut metodě render(), tedy například: `render("myTemplate.html")`
Tyto označující pasáže mají formát názvu proměnné ohraničené z obou stran dvě složenými závorkami, například: `{{jmeno}}` nebo `{{pozdrav}}`.
Předáme-li poté metodě `render()` atributy pojmenované jako `jmeno` a `pozdrav`, například takto: `render("myTemplate.html", jmeno="Nikola", pozdrav=osloveni)`, pak metoda `render()` nahradí `{{jmeno}}` a `{{pozdrav}}` námi dodanými řetězci.

#### Vytvoření templatu

Před tím než začneme používat metodu render(), musíme připravit template.
Jeho umístění je defaultně ve stejné složce jako je náš soubor `main.py`.
Samotným templatem může být libovolný HTML soubor, do kterého můžeme umístit značky pro nahrazení proměnnými: `{{jmenoPromenne}}`.

Příklad (HTML template `helloPage.html`):


```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{{customTitle}}</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
  </head>
  <body>
    Dobrý den {{jmeno}}, vítejte na těchto stránkách. 
  </body>
</html>
```

### Renderování templatu

Pro vyrenderování templatu stačí v některém z RequestHandlerů nahradit používanou metodu `write()` za `render()` a jako parametry této metody dodat název templatu a všechny proměné používané v tomto templatu. 
Pro výše uvedený příklad templatu `helloPage.html` by to vypadalo takto:

```python
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("helloPage.html", customTitle="coolpage.cz: Vítejte!", jmeno="Nikola Janů")
```

Při požadavku na stránku IndexHandler zavolá metodu `render()`, která do templatu `helloPage.html` dosadí dodané proměnné `customTitle` a `jmeno` a vrátí výslednou stránku, která bude vypadat takto:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>coolpage.cz: Vítejte!</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
  </head>
  <body>
    Dobrý den Nikola Janů, vítejte na těchto stránkách. 
  </body>
</html>
```

#### Jiné umístění templates

V praxi se můžeme dostat k tomu, že budeme používat více než jeden template - může jich být řádově desítky.
Jejich umístění vedle `main.py` by v takové situaci mohlo být poněkud zmatečné - Tornado proto umožňuje zvolit jiné umístění templatů.
Ideální volbou je umístit templaty například do složky `templates`.

Specifické umístění templatů můžeme vyjádřit pomocí pojmenoveného parametru `template_path` ve funkci `tornado.web.Application()`, kterou používáme k vytvoření Tornado aplikace/serveru.

Například:

```python
def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/hello", HelloHandler),
        (r"/bye", ByeHandler),
    ],
    template_path = "templates"
    )
```

Templaty bude Tornado potom hledat ve složce `templates`, která je ve stejné složce jako `main.py`.
Templaty tak elegantně uklidíme do vlastní složky a udržíme náš projekt více přehledný.


### Programování v templatu - control statements

Template nám v Tornadu neumožňuje pouze nahrazování značek `{{znacka}}` za hodnoty proměnných, ale i vykonávání python kódu přímo v HTML templatu.
V templatech můžeme používat if, for, while, and try.
Všechny tyto statementy přitom musíme ukončit značkou `{% end %}` - aby bylo zřejmé, kde cyklus/podmínka končí.

Příklad (template: shop.html):

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>blackmarket.cz: Zachraňte se!</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
  </head>
  <body>
    <ul>
        {% for item in items %}
            <li>{{ escape(item) }}</li>
        {% end %}
    </ul>
  </body>
</html>
```

V handleru poté předáme nikoliv textový řetězec, ale seznam:

```python
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("shop.html", items=["rouška", "dezinfekce", "respirátor", "brokovnice"])
```
