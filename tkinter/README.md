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
label_widget.pack() #funkce pack() promítne widget do okna

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

## Kompozice widgetů: widget.grid()

Abychom měli rozmístění widgetů v okně pod kontrolou, můžeme využít metodu widgetů `grid()`.
Pokud chceme nějaký widget umístit na specifické místo v rámci okna, můžeme tuto pozici specifikovat pomocí metody `grid()`:

```python
button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=1, row=1)
button4.grid(column=2, row=2)
```

Může se nám stát, že budeme chtít nějaký prvek umístit přes více řádků či sloupců gridu, pak můžeme v metodě `grid()` použít parametry `rowspan=` a `columnspan=`:

```python
button1.grid(column=0, row=0, rowspan=2)
button2.grid(column=1, row=0)
button3.grid(column=1, row=1, columnspan=2)
button4.grid(column=2, row=2)
```

Větší ukázku můžeme vidět zde:

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

