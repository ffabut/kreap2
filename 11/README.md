
## Pygame

Pygame je externí modul pro tvorbu her, grafik či animací v Pythonu.
Před použitím musíme pygame nainstalovat pomocí instalátoru `pip3`:

```
pip3 install --user pygame
```

### Inicializace pygame

Před použitím musíme modul pygame importovat a následně zavolat funkci `pygame.init()`.
Tato funkce nastaví nejen samotný pygame pro konkrétní OS na kterém náš skript běží (Windows, Mac, Linux) a my se tak nemusíme starat o rozdílnosti mezi jednotlivými OS.
Současně `pygame.init()` případně automaticky zavolá `init()` funkce na dalších importovaných pygame modulech, například na modulu `joystick`, opět aby byly tyto hardwarová zařízení správně nastavena pro daný operační systém a my se tak nemuseli zabývat zbytečnými rozdílnostmi mezi OS.

### Nastavení/inicializace okna

Po inicializaci pygame musíme nastavit velikost okna.
K tomu slouží funkce `pygame.display.set_mode()`, která inicializuje grafické okno.
Kompletní přehled argumentů funkce je: `set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface` (funkce vrací objekt typu pygame.Surface).

Objekt Surface představuje plochu, do které je možné vykreslovat.
V tomto případě jde o plochu okna programu, do níž budeme vykreslovat, avšak Surface můžeme vytvořit i pro jiné účely - například mít Surface, do něhož vykreslíme animaci naší postavy a tento postavový Surface až následně vykreslíme na konkrétní místo na hlavním Surface.
Surface se tedy neváže pouze výlučně k ploše okna.

#### Výška a šířka okna

Prvním argumentem této funkce je tuple či seznam obsahující dva integer prvky - šířku a výšku okna v pixelech, ukázka:

```python
width = 600
height = 400

pygame.display.set_mode([width, height])
```

Pokud výšku, šířku nebo oboje nastavíme na hodnotu 0, pak bude výška či šířka automaticky nastavena na výšku či šířku aktuálního monitoru:

```python
width = 600
height = 0

# okno bude mít šířku 600px a výšku rovnou výšce monitoru
pygame.display.set_mode([width, height])
```

#### Flags - dodatečné nastavení okna

Dalším parametrem funkce jsou dodatečné možnost, tzv. flags.
Dostupné flags jsou:

```
pygame.FULLSCREEN    create a fullscreen display
pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
pygame.OPENGL        create an OpenGL-renderable display
pygame.RESIZABLE     display window should be sizeable
pygame.NOFRAME       display window will have no border or controls

Pygame 2 has the following additional flags available.
pygame.SCALED        resolution depends on desktop size and scale graphics
pygame.SHOWN         window is opened in visible mode (default)
pygame.HIDDEN        window is opened in hidden mode
```

Použití je následující:

```python
width = 600
height = 400
flags = pygame.FULLSCREEN

pygame.display.set_mode([width, height], flags)
```

Jednotlivé možnosti/flags můžeme kombinovat pomocí bitwise operátoru, tzv. trubky `|`.
V tomto případě spouštíme okno ve fullscreenu s dvojitým bufferem a hardwarovou akcelerací:

```python
width = 600
height = 400
flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE

pygame.display.set_mode([width, height], flags)
```

####  depth, display, vsync

Pro informace o dalších argumentech se podívejte do dokumentace Pygame: https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode 

### Vykraslovací smyčka - draw loop

Hru či animaci je potřeba v čase průběžně znovu a znovy vykreslovat, často také chceme reagovat na aktivitu hráčky.
Abychom toho byli schopní je ideální vytvořit nekonečný cyklus, v jehož rámci budeme kontrolovat aktivitu hráčky/uživatelky, aktualizovat polohu herních elementů, vykreslovat nový frame do okna hry a případně také dělat další výpočty jako aktualizovat tahy nepřítele, počítat zdraví, údery, poškození, skóre, či kontrolovat zda hráčka hru nevyhrála, či neprohrála.

Každá iterace cyklem while je de facto vykreslení nového frame-u naší hry.

Pro draw loop se hodí cyklus while, do něhož umístíme podmínku, skrze kterou se dá cyklus opustit - abychom mohli hru jako uživatelky někdy taky zavřít, příklad:

```python
running = True

while running: # dokud je True, tak cyklus porad a porad bezi

  # zde kontrolujeme herni eventy - konkretne zmacknuti tlacitka close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # zde bychom vykreslovali prvky
  # a aktualizovali surface/canvas/plochu okna

# kdyz cyklus skonci, hru ukoncime / zavreme okno
pygame.quit()
```

Draw loop / nekonečný cyklus while je celkem praktický koncept pro všechny situace, kdy chceme během běhu programu průběžněš reagovat vstup dat nějakým výstupem a to tak dlouho, dokud program uživatelka nezavře.
Použili jsme ho již v prvním semestru, když jsme si ukazovali možnosti cyklu while.

#### Vykreslení pozadí a objektu

Abychom každý frame začali s čistou plochou, je dobré na začátku iterace vykreslit pozadí jednou barvou.
K tomu můžeme použít metodu `fill()`, kterou nabízí objekt pygame.Surface.
Tato metoda jako argumenty přijímá tuple/seznam 3 RGB barev v rozmezí 0-255:

```python
screen.fill((255, 255, 255))
```

Pro vykreslování objektů na plátno můžeme použít modul `pygame.draw`.
Pro vykreslení kruhu můžeme použít funkci `pygame.draw.circle(surface, color, center, radius) -> Rect` například:

```python
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
```

#### Aktualizace obrazu

Aby se námi provedené vykreslení pozadí a kruhu skutečně promítlo na obrazovku, musíme zavolat funkci `pygame.display.flip() -> None` případně `pygame.display.update(rectangle=None) -> None`, který umožňuje vykreslit jen obdelníkovou část obrazovky.
Například:

```python
pygame.display.update()
```

### Ukázkový program

Pokud výše zmíněný kód zkombinujeme, dostaneme základní pygame prográmek:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 400])

running = True

# nekonecny loop, v nemz se odehrava aktualizace hry
while running:

  # zde kontrolujeme herni eventy - konkretne zmacknuti tlacitka close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # nastaveni bileho pozadi okna
  screen.fill((255, 255, 255))

  # vykreslime modry kruh
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

  # update vykresleni obrazovky
  pygame.display.update()


pygame.quit()
```

### Vykreslování základních tvarů

#### pygame.draw - vykreslování základních tvarů

Modul `pygame.draw` nám nabízí několik užitečných funkcí pro vykreslování základních tvarů:

- `pygame.draw.rect(surface, color, rect) -> Rect`
- `pygame.draw.polygon(surface, color, points) -> Rect`
- `pygame.draw.circle(surface, color, center, radius) -> Rect`
- `pygame.draw.ellipse(surface, color, rect) -> Rect`
- `pygame.draw.arc(surface, color, rect, start_angle, stop_angle) -> Rect`
- `pygame.draw.line(surface, color, start_pos, end_pos, width) -> Rect`
- `pygame.draw.lines(surface, color, closed, points) -> Rect`
- `pygame.draw.aaline(surface, color, start_pos, end_pos) -> Rect`
- `pygame.draw.aalines(surface, color, closed, points) -> Rect`

Detaily k funkcím modulu `pygame.draw` je možné nalézt na: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect.

Všimněme si, že všechny tyto funkce vrací objekt `pygame.Rect` - obdélník ohraničující námi vykreslený objekt.
To je praktické, jelikož tento objekt potom můžeme použít jako parametr funkce `pygame.display.update()` a tím updatovat pouze tu část obrazovky, kterou jsme pozměnili - tím ušetříme výkon.

Pro lepší představu se můžete podívat na [ukázkový program draw-example.py](draw-example.py) představující použití funkcí modulu `pygame.draw`.

#### pygame.image - vykreslování obrázků aka bitmap

Pokud chceme vykreslit obrázek na Surface, pak jej musíme prvně načíst pomocí funkce `pygame.image.load(filename) -> Surface`.
Navrácený object Surface poté stačí pomocí funkce `blit()` vykreslit na hlavní plátno:

```python
img = pygame.image.load("myimage.jpg")
screen.blit(img, (50, 50))
```

Pro lepší přehled si můžete prohlédnout ukázkový program [image-example.py](image-example.py).

#### pygame.font - vykreslování textu

Pro vykreslení fontu musíme prvně vytvořit objekt `Font`, to můžeme udělat dvěma způsoby:
- `pygame.font.SysFont(name, size, bold=False, italic=False) -> Font` - vytvoří font z fontů dostupných v operačním systému
- `pygame.font.Font(filename, size) -> Font` - načte font ze souboru, pokud je název filename None, pak použije defaultní font

Na objektu font poté můžeme volat metodu `Font.render(text, antialias, color, background=None) -> Surface`, s jejíž pomocí dostaneme objekt Surface, který poté už stačí pouze umístít na konkrétní místo na hlavním plátně pomocí funkce `pygame.Display.blit()`:

```python
myfont = pygame.font.SysFont('Comic Sans MS', 130)
textsurface = myfont.render('Some Text', False, (0, 0, 0))
screen.blit(textsurface,(50,50))
```

Kompletní kód je dostupný v [text-example.py](text-example.py).


### Uložení Surface jako obrázku

Surface, ať už hlavní Surface představující plátno obrazovky, anebo nějaký jiný pod-Surface, můžeme uložit jako obrázek.
K tomu můžeme použít funkci `pygame.image.save(Surface, filename) -> None`.
Podporované formáty jsou BMP, TGA, PNG, nebo JPEG.
Použití je jednoduché:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 400])
#
# něco vykreslujeme
#
pygame.image.save(screen, "screenshot.jpg") # ukládáme
```



