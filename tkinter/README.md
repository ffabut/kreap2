# Tkinter

Tkinter je modul určený pro tvorbu grafického uživatelského rozhraní.
Jelikož je Tkinter součástí standardní knihovny Pythonu, není třeba jej instalovat, neobsahuje žádné další dependencies (závislosti na dalších modulech) a dá se tak snadno bundlovat pomocí pyinstaller.

Alternativ k modulu Tkinter je celá řada, jejich přehled můžete najít na: https://wiki.python.org/moin/GuiProgramming.
Za zmínku ale rozhodně stojí [modul PyQT5](https://pythonspot.com/pyqt5/), který již v základu obsahuje velmi hezky (pro dané OS nativně) vypadající GUI prvky a je často používaný - je to docela průmyslový standard.
Nevýhodou PyQT5 ale je, že je potřeba instalovat, obsahuje řadu dependencies a může být těžší jej bundlovat do spustitelné aplikace.
Další nevýhodou je, že pokud bychom s ním vytvořili aplikaci, kterou bychom chtěli prodávat, museli bychom platit licenční poplatky organizaci, která PyQT5 vyvíjí.
Zaměříme se proto raději na Tkinter.

## Tkinter: Hello World!

Jelikož je Tkinter built-in modulem v Pythonu, nemusíme jej instalovat a můžeme ho rovnou importovat do našeho skriptu.
Pro vytvoření okna, voláme funkci `tkinter.Tk()` a jí navrácený objekt uložíme do proměnné `window`.
Na objektu window poté budeme tvořit naše GUI, v tomto případě nastavujeme title okna a velikost okna.
Vykreslování GUI spustíme zavoláním metody `mainloop()` na objektu `window`:

```python
import tkinter

window = tkinter.Tk()
window.title("My First App: Hello World!")
window.geometry('800x600')

window.mainloop()
```

Pozn: takto napsaný skript se na funkci `mainloop()` "zasekne" - bude se totiž čekat na návratovou hodnotu funkce mainloop(), ale tato funkce bude ukončena až se zavřením okna, do té doby v ní bude probíhat nekonečný loop (proto taky název mainLOOP).
Někdy se podobným funkcím říká také, že jde o tzv. blocking functions / blokující funkce, jelikož "zablokují" pokračování skriptu na další řádky.

Alternativně můžeme vytvořit nekonečný loop sami a namísto metody `mainloop()` volat pravidelně metodu `update()`:

```python
import tkinter

window = tkinter.Tk()
window.title("My First App: Hello World!")
window.geometry('800x600')

while True:
  window.update() #neblokuje
  #zde muzeme provadet dalsi vypocty/cokoliv
```

## Grafické prvky: Widgety

Prázdné okno není nic moc užitečného, Tkinter nám proto samozřejmě umožňuje přidat do okna grafické prvky, kterým se v Tkinter lingo/hantýrce říká `widgety`.
Tkinter obsahuje následující widgety:

- Label - zobrazuje uživatelce kratší text
- Text - zobrazuje uživatelce pole s delším textem
- Entry - textový vstup od uživatelky
- Button - klikatelné tlačítko spouštějící nějaký event
- Radiobutton - volba jedné možnosti z několika možností
- Checkbutton - volba více možností z několika možností
- OptionMenu - volba z několika textových možností
- Scale - posuvník, vhodné pro volbu čísla z nějakého rozsahu možností
- Canvas - umožňuje na sebe vykreslovat grafické prvky
- LabelFrame - textem pojmenovaná zóna, slouží jako parent object pro další prvky, může ohraničovat skupinu souvisejících prvků 
- Menu - skrze Menu widget můžeme přidat meníčko a podmeníčka do horní lišty našeho okna, jak známe z běžných programů, například: File | Edit | View | Help

Pojďme se nyní na widgety podívat podrobněji:

### Label Widget

Label widget zobrazuje krátký text (jeden řádek) uživatelce.
Text můžeme updatovat programaticky

```python
import tkinter

window = tkinter.Tk()
label_widget = tkinter.Label(
  window,
  text="Toto je text label")
label_widget.pack() #funkce pack() umístí widget do okna
#pozice bude určena automaticky, pro přesné umístění můžeme použít metodu grid()

window.mainloop()
```

### Text Widget

Text widget zobrazuje plochu většího textu (více řádků).
Text widget může uživateli umožnit text vyhledávat, editovat a označovat.

```python
import tkinter

window = tkinter.Tk()
text_widget = tkinter.Text(
  window,
  width=20,
  height=3)
text_widget.insert(tkinter.END,
    "Text Widgetn20 characters widen3 lines high")
text_widget.pack()

window.mainloop()
```

### Entry Widget

Entry widget je pole, do kterého může uživatelka napsat text, je to tedy textový vstup od uživatelky:

```python
import tkinter

window = tkinter.Tk()
entry_widget = tkinter.Entry(window)
entry_widget.insert(0, "Type your text here")
entry_widget.pack()

while True:
  window.update()
  text = entry_widget.get() #získáme zadaný text
  print(text)
```

### Button Widget

Klikatelný button widget.
Button může být ve stavu on/off, při stisknutí může spustit event - námi specifikovanou funkci.
Na buttonu můžeme zobrazit obrázek.

V tomto příkladu vytváříme button, který při kliknutí zavolá námi definovanou funkci `eventFunction()`, která vypíše text do konzole:

```python
import tkinter

def eventFunction():
  print("Button clicked!")

window = tkinter.Tk()
button_widget = tkinter.Button(
    window,
    text="Button",
    command = eventFunction)
button_widget.pack()

window.mainloop()
```

### Radiobutton Widget

Radio button umožňuje vytvořit skupinu několika buttonů a zaručit, aby byl pouze jeden z nich zmáčknutý (v ON pozici).
Informace o tom, jaké tlačítko je označené získáváme pomocí definování proměnné typu `tkinter.IntVar`.

```python
import tkinter

window = tkinter.Tk()

v = tkinter.IntVar() #vytvorime tkinter promennou, do ktere ulozime stav zmacknutych tlacitek
v.set(0) #POZOR! Hodnoty do objektu IntVar musime nastavit skrze funkci set(), nikoliv jako v=1

radiobutton_widget1 = tkinter.Radiobutton(
  window,
  text="Radiobutton 1",
  variable=v,
  value=1)
radiobutton_widget2 = tkinter.Radiobutton(
  window,                                 
  text="Radiobutton 2",
  variable=v,
  value=2)
radiobutton_widget1.pack()
radiobutton_widget2.pack()

while True:
  window.update()
  selected = v.get() #POZOR: hodnoty z tkinter.IntVar ziskame pomoci v.get(), ne primo jako: selected = v
  print(selected)
```

### Checkbutton Widget

Checkbutton widget umožňuje vytvořit označitelná tlačítka, ale narozdíl od radiobutton můžeme u checkbutton označit několik z nich, ne pouze jedno.

```python
import tkinter

window = tkinter.Tk()

cb1 = tkinter.IntVar()
cb2 = tkinter.IntVar()

checkbutton_widget1 = tkinter.Checkbutton(
  window,
  text="Checkbutton1",
  variable=cb1)
checkbutton_widget2 = tkinter.Checkbutton(
  window,
  text="Checkbutton2",
  variable=cb2)

checkbutton_widget1.pack()
checkbutton_widget2.pack()

while True:
  window.update()
  print(cb1.get(), cb2.get())
```

### Listbox Widget

Listbox umožňuje uživatelce vybrat některou z možností, případně zobrazit seznam položek.

```python
import tkinter

window = tkinter.Tk()

listbox_entries = ["Entry 1", "Entry 2",
                   "Entry 3", "Entry 4"]
listbox_widget = tkinter.Listbox(
  window,
  selectmode=tkinter.MULTIPLE)

for entry in listbox_entries:
    listbox_widget.insert(tkinter.END, entry)

listbox_widget.pack()


while True:
  window.update()
  items = []
  
  selected = listbox_widget.curselection() #tuple obsahujici indexy oznacenych prvku
  for i in selected:
    item = listbox_widget.get(i) #pomoci metody get(index) ziskame hodnotu prvku pod danym indexem
    items.append(item)

  print(items)
```

### Scale Widget

Scale widget vytvoří slider, kterým uživatelka může zvolit číslo v definovaném rozsahu.
Hodnoty ze scale widget můžeme dostat pomocí metody `.Get()`, případně definovat proměnnou typu `tkinter.IntVar` a dosadit ji do parametru `variable=`.

```python
import tkinter

window = tkinter.Tk()
scale_widget = tkinter.Scale(
  window,
  from_=0,
  to=100,
  orient=tkinter.HORIZONTAL) #muzeme zvolit i tkinter.VERTICAL

scale_widget.set(25) #nastavime pocatecni hodnotu
scale_widget.pack()

while True:
  window.update()
  print(scale_widget.get())
```

### Canvas Widget

Na canvas widget je možné kreslit, podporuje několik kreslících metod.
Jednoduchá ukázka:

```python
import tkinter
window = tkinter.Tk()
canvas_widget = tkinter.Canvas(
  window,
  bg="blue",
  width=100,
  height= 50)
canvas_widget.pack()

tkinter.mainloop()
```

### LabelFrame Widget

LabelFrame widget se chová jako parent/rodič dalších prvků.
S jeho pomocí tak můžeme vytvořit zónu souvisejících prvků, která bude ohraničena linkou a nadepsána nějakým textem.
LabelFrame musí mít nějaké children/potomky, aby byl zobrazený.

```python
import tkinter

window = tkinter.Tk()

labelframe_widget = tkinter.LabelFrame(
  window,
  text="LabelFrame")

label_widget=tkinter.Label(
  labelframe_widget, #POZOR! Zde není rodičem window, ale právě labelframe_widget
  text="Child widget of the LabelFrame")

labelframe_widget.pack(padx=10, pady=10)
label_widget.pack()

tkinter.mainloop()
```

### Menu Widget

The Menu widget can create a menu bar. Creating menus can be hard, especially if you want drop-down menus. To do that, you use a separate Menu widget for each drop-down menu you’re creating.

```python
import tkinter

def menu_callback():
    print("I'm in the menu callback!")
def submenu_callback():
    print("I'm in the submenu callback!")

window = tkinter.Tk()
menu_widget = tkinter.Menu(window)

#vytvarime submenu
submenu_widget = tkinter.Menu(window, tearoff=False) #tearoff=False odstrani prepazku na zacatku submenu
submenu_widget.add_command(label="Submenu Item1",
                           command=submenu_callback)
submenu_widget.add_command(label="Submenu Item2",
                           command=submenu_callback)

menu_widget.add_cascade(label="Item1", menu=submenu_widget) #pridavame submenu
menu_widget.add_command(  #pridavame menu
  label="Item2",
  command=menu_callback)
menu_widget.add_command( #pridavame menu
  label="Item3",
  command=menu_callback)

window.config(menu=menu_widget)

window.mainloop()
```

## Kompozice widgetů - geometry managers: .pack(), place(), grid()

Pro určení umístění jednotlivých widgetů slouží v tkinteru tzv. geometry managers, jsou jimi: `pack()`, `place()` a `grid()`.
Nyní se na ně podíváme podrobněji.

### Pack()

V našich ukázkách jsme zatím používali package manager `pack()`, který je schopný do jisté míry určovat umístění automaticky za nás.
Manager `pack()` v základu umisťuje widgety pod sebe, dává jim co nejmenší výšku i šířku a automaticky je centruje:

```python
import tkinter as tk

window = tk.Tk()
window.geometry('800x600')

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

window.mainloop()
```

#### Fill: Roztáhnutí widgetu

Občas se nám ale může hodit, aby se prvky roztáhnuly po celé výšce nebo šířce okna.
K tomu slouží parametr `fill` metody `pack()`, pomocí kterého můžeme specifikovat, aby se daný widget roztáhnul na šířku, výšku nebo v obou směrech.
Parametr fill můžeme specifikovat se třemi různými konstantami:
- tk.X - roztažení dle osy x, tedy horizontálně
- tk.Y - roztažení dle osy y, tedy vertikálně
- tk.BOTH - pro roztažení v obou osách

```python
import tkinter as tk

window = tk.Tk()
window.geometry('800x600')

# width nehraje roli, jelikoz tuto hodnotu prepise pack() diky fill=tk.X
frame1 = tk.Frame(master=window, height=100, bg="red") 
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()
```

#### Side: směr řazení widgetů

V základu `pack()` řadí widgety shora dolů.
Tento směr můžeme přepsat pomocí parametru `side` a následujících konstant:
- `tk.TOP` - defaultní, shora dolů
- `tk.BOTTOM` - odpoda nahoru
- `tk.LEFT` - zleva doprava
- `tk.RIGHT` - zprava doleva

```python
import tkinter as tk

window = tk.Tk()
window.geometry('800x600')

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT) #radime zleva doprava, prvek se roztahne vertikalne

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()
```

#### Expand: roztažení prvků při zvětšení okna

V `pack()` můžeme specifikovat parametr `expand` (by default: expand=False), který zajistí, že se prvky roztáhnout při zvětšení okna.
Můžeme tak zajistit to, že prvky vždy zaplní celé okno, že se přizpůsobí:

```python
import tkinter as tk

window = tk.Tk()
window.geometry('800x600')

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
```

### Place()

Geometry manager `place()` umožňuje umístit widget na konkrétní souřadnici X a Y.
Souřadnicový systém začíná v levém horním rohu - souřadnice x=0,y=0.
Osa x je horizontální, tedy doprava roste číslo/souřadnice x.
Osa y je vertikální, tedy směrem dolů roste číslo/souřadnice y.
Hodnota x a y souřadnic představuje pixely (nejde třeba o milimetry, a není odvozena od velikosti písma).

Geometry managery můžeme kombinovat:
Použití je jednoduché:

```python
import tkinter as tk

window = tk.Tk()
window.geometry("800x600")

frame = tk.Frame(window, width=150, height=150, bg="green")
frame.pack()

label1 = tk.Label(window, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(window, text="I'm at (400, 75)", bg="yellow")
label2.place(x=400, y=75)

window.mainloop()
```

### Grid()

Třetí možností je geometry manager `grid()`, který je častou volbou, jelikož nám pomůže se vyvarovat nedostatků `pack()` (záleží na pořadí, v jakém widgety přidáme) a `place()` (nedokáže reagovat na změnu velikosti okna).
Grid nám nabízí lepší kontrolu nad umístěním a její lepší škálovatelnost, lehčí upravování.

Pomocí metody `grid()` umísťujeme prvky do gridu/mřížky - do konkrétního sloupce a řádku.
Máme tedy představu o kompozici prvků a přitom nejsme vázáni na pořadí, v jakém prvky vkládáme, ani na naprosto přesné souřadnice.
Jde o obecnější, ale čitelný popis toho, jak prvky umístit, například:

```python
import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="okay", bg="green")
button2 = tk.Button(window, text="okay", bg="red")
button3 = tk.Button(window, text="okay", bg="yellow")
button4 = tk.Button(window, text="okay", bg="blue")

button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=1, row=1)
button4.grid(column=2, row=2)

window.mainloop()
```

#### Více řádků/sloupců: rowspan, columnspan

Může se nám stát, že budeme chtít nějaký prvek umístit přes více řádků či sloupců gridu, pak můžeme v metodě `grid()` použít parametry `rowspan=` a `columnspan=`:

```python
import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="okay", bg="green")
button2 = tk.Button(window, text="okay", bg="red")
button3 = tk.Button(window, text="okay", bg="yellow")
button4 = tk.Button(window, text="okay", bg="blue")

button1.grid(column=0, row=0, rowspan=2)
button2.grid(column=1, row=0)
button3.grid(column=1, row=1, columnspan=2)
button4.grid(column=2, row=2)

window.mainloop()
```

Větší ukázku použití můžeme vidět zde:

```python
import tkinter
from tkinter import ttk

window = tkinter.Tk()

#TEXT INPUT
text_widget = tkinter.Text(
  window,
  width=40,
  height=5,
  )
text_widget.insert(tkinter.END, "Text Widget \n20 characters widen\n5 lines high")

#RADIO BUTTONS
one = tkinter.Checkbutton(window, text="One")
two = tkinter.Checkbutton(window, text="Two")
three = tkinter.Checkbutton(window, text="Three")

#LABEL and ENTRY
namelbl = tkinter.Label(window, text="Name")
name = tkinter.Entry(window)

#BUTTONS ok and cancel
ok = tkinter.Button(window, text="Okay")
cancel = tkinter.Button(window, text="Cancel")

#adding widgets into the grid
text_widget.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

window.mainloop()
```

#### Odsazení/padding: parametry padx, pady

Pokud bychom chtěli dát prvkům nějaký prostor kolem nich, můžeme k tomu využít parametry `padx` a `pady` metody `grid()`.
S jejich pomocí můžeme nadefinovat, kolik pixelů horizontálně a vertikálně má být kolem widgetu prázdných - aby se na něj nelepily další widgety.
Použití je následující:

```python
import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="okay", bg="green")
button2 = tk.Button(window, text="okay", bg="red")
button3 = tk.Button(window, text="okay", bg="yellow")
button4 = tk.Button(window, text="okay", bg="blue")

button1.grid(column=0, row=0, padx=20, pady=20)
button2.grid(column=1, row=0, padx=20, pady=20)
button3.grid(column=1, row=1, padx=20, pady=20)
button4.grid(column=2, row=2, padx=20, pady=20)

window.mainloop()
```

#### Přizpůsobení gridu zvětšenému oknu

Aby se grid přizpůsobil změnám velikosti okna, musíme na objektu window zavolat metodu `columnconfigure()` a `rowconfigure()`, pomocí kterých nastavíme chování sloupců a řádků při zvětšení okna.
První parametr metod určuje index řádku či sloupce, který chceme konfigurovat.
Pojmenovaným parametrem `weight` určujeme, jak moc daný řádek/sloupec bude růst (relativně k ostatním řádkům/sloupcům) při zvětšení okna (defaultní hodnota = 0, tj. neroste).
Pojmenovaným parametrem `minsize` můžeme určit minimální výšku řádku či šířku sloupce.
Příklad:

```python
import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="okay", bg="green")
button2 = tk.Button(window, text="okay", bg="red")
button3 = tk.Button(window, text="okay", bg="yellow")
button4 = tk.Button(window, text="okay", bg="blue")

window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=2, minsize=75) #poroste 2x rychleji než ostatní sloupce
window.columnconfigure(2, weight=1, minsize=75)

window.rowconfigure(0, weight=1, minsize=50)
window.rowconfigure(1, weight=2, minsize=50) #poroste 2x rychleji nez prvni radek, a 3x pomaleji nez treti radek
window.rowconfigure(2, weight=6, minsize=50) #poroste 3x rychleji než druhy radek, a 6x rychleji nez prvni radek

button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=1, row=1)
button4.grid(column=2, row=2)

window.mainloop()
```

Metody `columnconfigure()` a `rowconfigure()` můžeme volat nejen s jedním indexem, ale také se seznamem indexů sloupců/řádků, které konfigurujeme, například:

```python
window.columnconfigure([0,1,2], weight=1, minsize=75)
window.rowconfigure([0,1,2], weight=1, minsize=50)
```

#### Usazení widgetu v buňce gridu: parametr sticky

Zejména při zvětšení okna, ale i jindy se může stát, že bude widget menší než buňka, v níž je usazen.
Geometry manager `grid` v takovém případě umístí widget do středu buňky.
Toto chování ale můžeme pozměnit pomocí parametru `sticky` (podobný parametru `fill` u metody `pack()`), který přijímá následující možnosti:
- sticky="n" - widget bude umístěn severně - nahoru buňky
- sticky="e" - widget bude umístěn východně - doprava buňky
- sticky="s" - widget bude umístěn jižně - ve spodek buňky
- sticky="w" - widget bude umístěn západně - nalevo buňky

Tyto orientace můžeme také kombinovat, například:
- sticky="ne" - widget bude umístěn severovýchodně, tedy do pravého horního rohu buňky
- sticky="sw" - widget bude umístěn jihozápadně, tedy do levého spodního rohu buňky

Speciálním případem je umístění do protichůdných směrů - toto umístění prvek roztáhne na ploše buňky:
- sticky="ns" - prvek bude roztažen od jihu na sever, tedy vertikálně, na výšku buňky
- sticky="we" - prvek bude roztažen od západu na východ, tedy horizontálně, na šířku buňky
- sticky="nswe" - prvek bude roztažen do všech směrů, tedy na celou plochu buňky

Ukázka:

```python
import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="okay", bg="green")
button2 = tk.Button(window, text="okay", bg="red")
button3 = tk.Button(window, text="okay", bg="yellow")
button4 = tk.Button(window, text="okay", bg="blue")

window.columnconfigure([0,1,2], weight=1, minsize=75)
window.rowconfigure([0,1,2], weight=1, minsize=50)

button1.grid(column=0, row=0, padx=20, pady=20, sticky="nsew")
button2.grid(column=1, row=0, padx=20, pady=20, sticky="we")
button3.grid(column=1, row=1, padx=20, pady=20, sticky="w")
button4.grid(column=2, row=2, padx=20, pady=20, sticky="nw")

window.mainloop()
```

## Interakce

### Metoda bind()

Metoda `bind()` umožňuje svázat zmáčknutí klávesy, či kliknutí na widget (např. button) s námi definovanou funkcí.

#### Reakce na zmáčknutí klávesy na klávesnici

Chceme-li reagovat na zmáčknutí tlačítka, použijeme metodu `bind()` na objektu okna naší aplikace.
Prvním parametrem metody je event, na který chceme reagovat, dostupné například jsou:
- `<Key>` - libovolná klávesa na klávesnici
- `<Button-1>` - levé tlačítko myši
- `<Button-2>` - prostřední tlačítko myši
- `<Button-3>` - pravé tlačítko myši
- `<ButtonRelease-1>` - tlačítko 1 bylo uvolněno (můžeme použít i tlašítko 2 a 3). Aktuální pozice myši je poskytována v atributech x a y v události zaslaného volané funkci.
- `<Double-Button-1>` - na Tlačítko 1 bylo dvojkliknuto (můžeme použít i tlačítko 2 a 3). Jako prefixy můžete použít Double nebo Triple.
- `<Enter>` - ukazatel myši vstoupil na widget (tato událost neznamená, že uživatelka stiskla Enter !).
- `<Leave>` - ukazatel myši opustil widget.
- `<FocusIn>` - tento widget (nebo jeho potomek) získal klávesnicový focus. (De facto že okno bylo označeno a je aktivním oknem, ne na pozadí někde.)
- `<FocusOut>` - focus byl přesunut z tohoto widgetu na jiný. (Bylo označeno jiné okno, náš program ztratil focus a je někde na pozadí.)
- `<MouseWheel>` - uživatelka rolovala kolečkem myši. Směr posunu je poskytnut v atributu `delta` události, předávané volané funkci. (Nefunguje na Linuxu, tam je potřeba použít `<Button-4>` (up) a `<Button-5>` (down).)
- `<Configure>` - změna velikosti widgetu/okna, nejčastěji při resizu okna.
- `w`, `1`, `!` - můžeme definovat i přímo konkrétní znak.

```python
import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
  print(event.char)

def handle_w(event):
  print("tlacitko w bylo zmacknuto!")

def handle_wheel(event):
  if event.num == 4:
      print("linux mouse up")
  elif event.num == 5:
      print("linux mouse down")
  else:
      print("pohyb kolecka o:", event.delta)

window.bind("<Key>", handle_keypress)
window.bind("<MouseWheel>", handle_wheel)
window.bind("<Button-4>", handle_wheel)
window.bind("<Button-5>", handle_wheel)
window.bind("w", handle_w)

window.mainloop()
```

#### Reakce na kliknutí na button

Metodu `bind()` můžeme zavolat na objektu button, poté bude zavolána patřičná funkce ve chvíli, kdy je zmáčknuté tlačítko:

```python
import tkinter as tk

window = tk.Tk()

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(window, text="Click me!")
button.pack()

#<Button-1> je mouse left button
button.bind("<Button-1>", handle_click)

window.mainloop()
```

#### Atributy datového typy event

- event.widget: widget, který vyvolalo událost. Toto je platná instance tkinterovského udělátka. Při tisku ovšem získáte přes metodu __str__ pouze jeho jméno. Při porovnávání se však použije daná instance. Tento atribut se nastavuje u všech událostí.
- event.x, event.y: současná pozice myši, je v pixelech.
- event.x_root, event.y_root - současná pozice myši relativně k hornímu levému rohu obrazovky, je v pixelech.
- event.char - kód znaku, pouze u klávesnicových událostí, datový typ `str`.
- event.keysym - konkrétní symbol klávesy, jen u klávesnicových událostí.
- event.keycode - kód klávesy, jen u klávesnicových událostí.
- event.num - číslo tlačítka, jen u myších událostí.
- event.width, event.height - nová velikost widgetu, v pixelech jen u Configure událostí.
- event.type - typ události.

Z důvodu kompatibility je lepší se držet char, height, width, x, y, x_root, y_root a widget.

### Parametr command

Alternativou k používání metody `bind()`, je vytvoření widgetu s parametrem `command`, skrz který specifikujeme funkci, která bude zavolána.
Malá ukázka programu:

```python
import tkinter as tk

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()
```

## Vyskakovací okna

Někdy je potřeba uživatelky informovat o vzniklé situaci, k tomu můžeme použít vyskakovací okna.
Před použitím musíme importovat sub-modul messagebox, dál je to již velmi jednoduché:

```python
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

#prvni parametr: nazev okna, druhy parametr: zprava zobrazena v okne
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
messagebox.showinfo("Information", "Informative message")

window.mainloop()
```

