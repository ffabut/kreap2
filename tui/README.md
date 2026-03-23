# Terminal User Interface

Pro inspiraci: https://github.com/rothgar/awesome-tuis

https://docs.python.org/3/library/curses.html - volitelná součást standardní knihovny Python
https://github.com/peterbrittain/asciimatics 
https://github.com/ceccopierangiolieugenio/pyTermTk
https://github.com/urwid/urwid
https://github.com/bczsalba/pytermgui - už zastarává, support myši

## Textual

### Instalace
Pozor, pro používání stačí nainstalovat textual, ale pro vývoj appek i textual-dev, takže instalujeme 2 package:
```
pip install textual textual-dev
```

### Demo

Jakmile máme nainstalováno, můžeme se pro inspiraci podívat na textual demo pomocí příkazu: `python -m textual`.

### Hello Textual!

```python
from textual.app import App
from textual.widgets import Static

class HelloTextualApp(App):
    def compose(self):
        yield Static("Hello, Textual!")

if __name__ == "__main__":
    app = HelloTextualApp()
    app.run()
```

### TCSS neboli Textual CSS

Textual používá vlastní omezenou podmnožinu CSS, takové pseudo CSS, skrze které nám ale umožňuje velmi jednoduše a srozumitelně stylovat widgety.

V příkladu níže přidáváme objektu static argument 'id', který odpovídá id v HTML, který poté můžeme v CSS označit skrze #id.
CSS pro jednoduchost načítáme přímo v HelloTextualApp() v proměnné CSS.

```python
from textual.app import App
from textual.widgets import Static

class HelloTextualApp(App):
  def compose(self):
    yield Static(
        "Hello, Textual!",
        id="hello" # objekt Static bude mit id=hello, pak v CSS stylujeme skrz #hello
        #classes="small blue" - muzeme take vytvaret tridy
        )
  
  CSS = """
  Screen {
    align: center middle;
  }

  #hello {
    background: blue 50%;
    border: wide white;
    width: auto;
  }
  """

if __name__ == "__main__":
  app = HelloTextualApp()
  app.run()
```

CSS můžeme také realizovat přes atribut .styles na jednotlivém widgetu.
V příkladu níže uložíme

```python
from textual.app import App
from textual.widgets import Label, Static

class SimpleApp(App):
  def compose(self):
    """Compose urcuje kompozici elementu v aplikaci.
    Pod povrchem je to generator, jednotlive widgety tedy "vracime" pres yield.
    """
    self.static = Static("I am a [bold red]Static[/bold red] widget!") # ukládáme referenci, abysme se k widgetu později dostali v on_mount
    yield self.static # widgety umistime skrze yield
    self.label = Label("I am a [yellow italic]Label[/yellow italic] widget!",)
    yield self.label

  def on_mount(self):
    """on_mount je volano po tom, co jsou widgety vytvoreny a umisteny,
    ale pred tim, nez je vykresleno... Nyni je idealni aplikovat styly.
    """
    # Stylovat nemusime jen pres CSS="", ale taky pres atribut .styles widgetu
    self.static.styles.background = "blue"
    self.static.styles.border = ("solid", "white")
    self.static.styles.text_align = "center"
    self.static.styles.padding = 1, 1
    self.static.styles.margin = 4, 4
    # Styling the label
    self.label.styles.background = "darkgreen"
    self.label.styles.border = ("double", "red")
    self.label.styles.padding = 1, 1
    self.label.styles.margin = 2, 4

if __name__ == "__main__":
  app = SimpleApp()
  app.run()
```

Styly ale můžeme také přidat v separátním souboru .tcss.
Výhodou tohoto řešení je, že můžeme naši aplikaci spustit v dev módu a vidět výsledky změn v .tcss file v reálném čase za běhu programu.
To nám hodně ulehčí život při psaní TCSS a stylování naší aplikace, protože ji nemusíme neustále restartovat.

Pro použití TCSS file stačí v třídě naší aplikace použít proměnnou CSS_PATH:

```python
class MyApp(App):
    CSS_PATH = "main.tcss" 
    # CSS_PATH = ["main.tcss", "another.tcss"] - muzeme taky pouzit seznam nekolika tcss souboru
    def compose(self):
        yield Header()
```

### Compound Widget

Obcas muzeme chtit opakovat urcitou skupiny widgetu spolecne - napriklad label a pod nim input field.
Textual nam to umoznuje skrze tzv. Compound Widget, slozeny widget, nebo bysme taky mohliy rict group, skupinu widgetu.
Realizujeme jej jako nasi vlastni tridu, ktera dedi z obecne tridy textual.widgets.Widget.
V nasi nove tride muzeme pridat widgety, jak potrebujeme, upravit konstruktor `__init__()`, pridat defaultni CSS apod.:

```python
from textual.app import App
from textual.widget import Widget
from textual.widgets import Button, Header, Input, Label

class LabelledInput(Widget):
    """LabelledInput je nas custom Widget slozeny z nekolika jinych widgetu.
    V terminologii Textual je to Compound Widget, taky si to muzeme predstavit jako group.
    """
    DEFAULT_CSS = """
    LabelledInput {
        height: 4;
    }
    """
    def __init__(self, label):
        """Potrebujeme, aby nas widget prijimimal atribut label pri sve iniciaci.
        Takze overridujeme funkci __init__() a pridavame do ni parametr label.
        Ale to prinasi problem - tim prepiseme puvodni medotu Widget.__init__(),
        ktera na pozadi dela spoustu magie. Toto je casty problem pri dedeni z tridy
        a prepisovani __init__(). Reseni je ziskat rodicovskou tridu pres super()
        a na ni pak volat .__init__(). Nacez pokracujeme custom codem...
        """
        super().__init__() # funkce super() vraci rodice tj. tridu Widget. Na ni volame puvodni konstruktor __init__()
        self.label = label # a tady pokracujeme vlastnim kodem

    def compose(self):
        yield Label(f"{self.label}:")
        yield Input(placeholder=self.label.lower())


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True, icon="👻")
        yield LabelledInput("Name")
        yield LabelledInput("Surname")
        yield LabelledInput("Email")
        yield Button("Click me!")

MyApp().run()
```


https://textual.textualize.io/how-to/center-things/