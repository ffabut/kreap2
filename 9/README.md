# Lekce 8: Regulární výrazy

Regulární výrazy (anglicky regular expressions, zkráceně regexp, regex, či jen re) jsou výrazy regulárního jazyka, který umožňuje obecný popis textových řětězců.
S jejich pomocí tak můžeme obecně popsat textové řetězce, například: začíná na písmeno K a následují 4 znaky; nebo začíná řetězcem `mal` a končí buď na `á` nebo `ý`.
Můžeme tak například vyhledávat v textu nejen jedno konkrétní slovo, ale i jeho varianty, včetně skloňování, časování apod.

Nejčastější použití regulárních výrazů je:
- vyhledávání textu
  - prosté zjištění, zda vstupní text vyhovuje zadanému regulárnímu výrazu
  - zjištění pozice ve vstupním textu, kde shoda s regulárním výrazem začíná
- manipulace s textem
  - záměna textu v podvýrazech regexu
  - extrakce shod s regulárním výrazem do předané proměnné

Regulární výrazy nejsou Python specifickým tématem, jsou používány snad ve všech programovacích jazycích, a také například v OpenOffice a podobně.

## Syntax regulárních výrazů

Ke spouštění následujících výrazů můžeme použít jednu z mnoha webových služeb nabízející testování regulárních výrazů, například: [regexr.com](https://regexr.com/).

### Běžná písmena (literal characters) a speciální znaky (special characters)

Chceme-li regexem popsat konkrétní slovo za použítí běžných znaků (včetně mezery), stačí jej prostě normálně napsat:
- regex `Karel` bude mít shodu s řetězcem `Karel` v textu,
- regex `12 opic` bude mít shodu s řetězcem `12 opic` v textu.

Lehká komplikace přichází v moměntě, kdy chceme použít speciální znaky (`\^$.|?*+()[]{}`), kterým regex jazyk dává speciální význam.
Pokud je chceme použít jako obyčejné znaky, aniž by jim regex dal speciální význam, musíme je escapovat lomítkem:
- regex `12\$` bude mít shodu s řetězcem `12$` v textu,
- regex `konec\.` bude mít shodu s řetězcem `konec.` v textu,
- regex `C:\\Users\\Me` bude mít shodu s řetězcem `C:\Users\Me` v textu.

Další dva znaky, u kterých se neobejdeme bez escapování, jsou: nový řádek aka enter (`\n`) a tabulátor (`\t`). 

### Třídy znaků: jakýkoliv znak, znak z určité skupiny

Pokud chceme, aby regex odpovídal ne jednomu, ale několika znakům z určité skupiny znaků, můžeme k tomu použít některou z tříd znaků, které regex nabízí.
Jsou jimi:
.   jakýkoliv znak
\w  písmeno (word letter)
\d  číslice
\s	whitespace (mezera, tabulátor, nová řádka)
\W  NE-písmeno
\D  NE-číslice
\S	NE-whitespace
[abc]  některý ze znaků a, b nebo c
[^abc]  jakýkoliv znak kromě a, b, nebo c (^ je negace obecně)
[a-g]  jakýkoliv znak mezi a až g

Příklady:
- regex `Novotn.` bude mít shodu s: `Novotný`, `Novotná`, ale i `Novotnž` nebo `Novotn+`
- regex `Novotn\w` bude mít shodu s: `Novotný`, `Novotná`, `NovotnŽ`, ale už ne `Novotn+`
- regex `linka \d` bude mít shodu s: `linka 1`, `linka 9`, ale ne `linka 12` nebo `linka C`
- regex `Ahoj\sčlověče.` bude mít shodu s: `Ahoj člověče`, `Ahoj	člověče`, ale ne `Ahoj,člověče`

## Anchors -

Anchors slouží k popisu konců a začátků řetězců či slov.
Jsou k dispozici:

^  začátek řetězce
$  konec řetězce
\b  hranice slova
\B	nehranice slova

V řetězci `Máma mele maso. Táta má led. Máma mele sele.`:
- regex `^Máma` bude mít shodu s `Máma` na začátku řetězce, ne s tou v třetí větě
- regex `.....$` bude mít shodu se `sele.`
- regex `\ble` bude mít shodu se `le`d, ale ne se se`le`
- regex `le\b` bude mít shodu s me`le`, ale ne s `le`d
- regex `\Ble` bude mít shodu s me`le`, ale ne s `le`d
- regex `le\B` bude mít shodu s `le`d, ale s me`le`

### Kvantifikátory

Někdy se nám hodí vyhádřit množství znaků, k tomu můžeme použít kvantifikátory:

a*  nula nebo více písmen `a`
a+  jedno nebo více písmen `a`
a?	nula nebo jedno písmeno `a`

a{5}  pět písmen `a`
a{2,}  dvě nebo více písmen `a`
a{1,3}	jedno až tři písmena `a`

ab|cd  matchuje `ab` nebo `cd`

### Skupiny

Skupiny mají dvě použití: buď tzv. capturing group, které slovo jakoby označí a bude dál dostupné - buď jako výsledek v Pythonu, nebo v rámci zpětných referencí v regex,
anebo non-capturing group, pomocí kterých můžeme třeba opakovat některé slovo za použití kvantifikátorů:

(abc)  capturing group
(?:abc)  non-capturing group
\1  zpětná reference k první skupině - matchne přesně to, co se objevilo v 1. skupině

V řetězci `Máma mele maso. Máma mele selelelelelele.`:
- regex `mele (....)` označí `maso` a `sele`
- regex `se(?:le)+` označí `selelelelelele`

#### Greedy quantifiers

V základě kvantifikátor matchne co nejvíce znaků je možné.
Pokud chceme, aby matchoval co nejméně, přidáme za kvantifikátor otazník, tím vytvoříme tzv. lakomý kvantifikátor:

a+?  jedno nebo více písmen `a`, ale matchne jich co nejméně
a{2,}?  dvě a více písmen `a`, ale matchne jich co nejméně


## Regular Expression v Pythonu - modul `re`

Regulární výrazy jsou v Pythonu implementovány v nativním modulu [re](https://docs.python.org/3/library/re.html#module-re).

### Python a speciální znaky v řetězcích

Python sám o sobě některé znaky v řetězcích používá jako speciální (například zpětné lomítko - pro zápis enteru třeba `\n`) - pokud bychom tak zpětné lomítko chtěli používat, museli bychom jej pro Python escapovat (ze 2 lomítek se stane jedno) a potom escapovat ještě pro regex (ze dvou se stane jedno), čili pro vyjádření jednoho lomítka, bychom v pythonu museli zapsat: `\\\\`, což by Python poslal regexu jako `\\`, což by regex vyhodnotil jako znak `\`.
Například: `C:\\\\Users\\\\Me` by tak matchovalo `C:\Users\Me`.

Abychom se tomuto vyhnuli, můžeme zapisovat řetězce ne jako běžné textové řetězce v uvozovkách `"řetězec"`, ale jako raw řetězce, které začínají před uvozovkami písmenem r: `r"raw-řetězec"`.
Python v raw řetězcích nevyhodnocuje speciální znaky (zpětné lomítko) a tak je nemusí escapovat.
Dále tedy budeme používat raw řetězce.

### Regex Hello World - re.search()

Základní funkcí, kterou modul `re` nabízí je funkce `search()`, ta projde řetězec a vrátí první výsledek, který vyhovuje:

```python
import re

text = """
My, občané České republiky v Čechách, na Moravě a ve Slezsku,
v čase obnovy samostatného českého státu,
věrni všem dobrým tradicím dávné státnosti zemí Koruny české i státnosti československé,
odhodláni budovat, chránit a rozvíjet Českou republiku
v duchu nedotknutelných hodnot lidské důstojnosti a svobody
jako vlast rovnoprávných, svobodných občanů,
kteří jsou si vědomi svých povinností vůči druhým a zodpovědnosti vůči celku,
jako svobodný a demokratický stát, založený na úctě k lidským právům a na zásadách občanské společnosti,
jako součást rodiny evropských a světových demokracií,
odhodláni společně střežit a rozvíjet zděděné přírodní a kulturní, hmotné a duchovní bohatství,
odhodláni řídit se všemi osvědčenými principy právního státu,
prostřednictvím svých svobodně zvolených zástupců přijímáme tuto Ústavu České republiky"
"""

# výraz "Če.*\b" má význam: řetězec začíná písmeny Če, po něm jakékoliv psímeno 0krát nebo víckrát

match = re.search(r"Če\w*", text)

# celý matchlý řetězec je skryt pod indexem 0:
print(match[0]) # vypíše České

# informace o pozici, na které se výsledek vyskytuje je ve funkcích start() a end()
print(match.start()) #vypíše pozici, na které match v řetězci začíná
print(match.end()) #vypíše pozici, na které match končí
```

### Používání capturing groups

Pokud v regulárním výrazu použijeme capturing groups, pak budou výsledky pro tyto skupiny dostupné pod indexy 1 a více:

```python
import re

text = """
My, občané České republiky v Čechách, na Moravě a ve Slezsku,
v čase obnovy samostatného českého státu,
věrni všem dobrým tradicím dávné státnosti zemí Koruny české i státnosti československé,
odhodláni budovat, chránit a rozvíjet Českou republiku
v duchu nedotknutelných hodnot lidské důstojnosti a svobody
jako vlast rovnoprávných, svobodných občanů,
kteří jsou si vědomi svých povinností vůči druhým a zodpovědnosti vůči celku,
jako svobodný a demokratický stát, založený na úctě k lidským právům a na zásadách občanské společnosti,
jako součást rodiny evropských a světových demokracií,
odhodláni společně střežit a rozvíjet zděděné přírodní a kulturní, hmotné a duchovní bohatství,
odhodláni řídit se všemi osvědčenými principy právního státu,
prostřednictvím svých svobodně zvolených zástupců přijímáme tuto Ústavu České republiky"
"""

match = re.search(r"občané (\w*) (\w*)", text)

# celý matchlý řetězec je pořád skryt pod indexem 0:
print(match[0]) # vypíše: občané České republiky
print(match[1]) # vypíše: České
print(match[2]) # vypíše: republiky
```

### re.finditer()

Pokud bychom chtěli vyhledat všechny výskyty vyhovující našemu regexu a ne jen ten první jako u `search()`, pak můžeme použít funkci `finditer()`.
Ta vrací seznam výsledků hledání.


```python
import re

text = """
My, občané České republiky v Čechách, na Moravě a ve Slezsku,
v čase obnovy samostatného českého státu,
věrni všem dobrým tradicím dávné státnosti zemí Koruny české i státnosti československé,
odhodláni budovat, chránit a rozvíjet Českou republiku
v duchu nedotknutelných hodnot lidské důstojnosti a svobody
jako vlast rovnoprávných, svobodných občanů,
kteří jsou si vědomi svých povinností vůči druhým a zodpovědnosti vůči celku,
jako svobodný a demokratický stát, založený na úctě k lidským právům a na zásadách občanské společnosti,
jako součást rodiny evropských a světových demokracií,
odhodláni společně střežit a rozvíjet zděděné přírodní a kulturní, hmotné a duchovní bohatství,
odhodláni řídit se všemi osvědčenými principy právního státu,
prostřednictvím svých svobodně zvolených zástupců přijímáme tuto Ústavu České republiky"
"""

matches = re.finditer(r"Če\w*", text)

# přes seznam vyhovujících výsledků můžeme iterovat
for match in matches:
    print(match[0]) # vypíšeme celý vyhovující výsledek
```

### Další praktické funkce:

- [re.match()](https://docs.python.org/3/library/re.html#re.match)
- [re.fullmatch()](https://docs.python.org/3/library/re.html#re.fullmatch)
- [re.split()](https://docs.python.org/3/library/re.html#re.split)
- [re.sub()](https://docs.python.org/3/library/re.html#re.sub)
