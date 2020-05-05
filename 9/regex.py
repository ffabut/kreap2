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

### výraz "Če.*\b" má význam: řetězec začíná písmeny Če, po něm jakýkoliv znak 0 nebo víckrát a končí hranicí slova
match = re.search(r"Če\w*", text)

print(match[0]) # vypíše České
print(match.start()) #vypíše pozici, na které match v řetězci začíná
print(match.end()) #vypíše pozici, na které match končí


### používání capturing groups
match = re.search(r"občané (\w*) (\w*)", text)

# celý matchlý řetězec je pořád skryt pod indexem 0:
print(match[0]) # vypíše: občané České republiky
print(match[1]) # vypíše: České
print(match[2]) # vypíše: republiky



### searchall()
matches = re.finditer(r"Če\w*", text)

# přes seznam vyhovujících výsledků můžeme iterovat
for match in matches:
    print(match[0]) # vypíšeme celý vyhovující výsledek
