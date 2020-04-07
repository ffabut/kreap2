# Lekce 5: Databáze - jazyk SQL, jednoduchá databáze SQLite

Nejen v případě webových serverů, ale i běžných skriptů a jiných aplikací v Pythonu, je občas potřeba uložit data tak, aby byla dostupná i po restartu aplikace/skriptu/serveru/systému.
K perzistentnímu uložení dat přitom nemůžeme využít proměnné - ty jsou nenávratně ztraceny po ukončení programu.

## Ukládání dat do souboru
Jednou z možností je data ukládat do textového souboru - ať již jako jednoduchý text (např. co řádek to jeden záznam), anebo je ukládat do souboru ve formátu JSON.
Nevýhodou tohoto řešení je, že není příliš přátelské k asynchronicitě: pokud se například tři uživatelé zaregistrují na náš web, může se stát, že se server pokusí zapsat všechny tři hodnoty ve stejném čase a dojde k chybě.

Pokud ale ohlídáme, že do souboru píšeme jen z jednoho procesu v čase, pak jsme v bezpečí.
Zápis do souboru se tak hodí spíš na méně časté zápisy jako třeba ukládání konfiguračních souborů nějaké aplikace - to je v kombinaci s formátem JSON nebo YAML naprosto běžná praxe.

## Ukládání dat do databáze

Druhou a více robustní možností je ukládat data do databáze.
Databáze jsou více profesionálním řešením problému ukládání dat a nabízí řadu výhod (některé jen část z nich):
- lepší výkon při zápisu nebo čtení velkého objemu dat
- databáze může běžet na odděleném počítači
- k databázi můžeme přistupovat na dálku přes síť
- databáze umožňují komplexnější způsob vyhledávání dat

### Databáze využívající jazyk SQL 
Formátů/jazyků databází je velká řada, jednou z nejrozšířenějších jsou ale databáze využívající princip a jazyk SQL (Structured Query Language).

SQL je implementováno mnoha firmami i řadou open source projektů, které se liší především výkonem, maximální velikostí, jednoduchostí, mírnými odchylkami ve funkcionalitě jazyka SQL, zda jsou open source nebo placené, ale v zásadě jsou si velmi podobné.
Mají 90% společného a to je SQL, dá se mezi nimi přecházet.

#### SQL servery

Některými z implementací SQL databází jsou:
- MariaDB (open source, vyvíjí mariaDB foundation)
- PostgreSQL (open source, vyvíjí University of California, Berkeley)
- mySQL (rozšířená, vyvíjí Oracle Corporation)

Většina SQL databází je založena na principu serveru - na našem počítači nebo někde jinde v síti běží SQL software a k němu se připojujeme a na něj posíláme dotazy.
SQL systém poté řeší všechny technikálie - kdy, kam, jak ukládat data a podobně.

#### Server-less SQL

Existuje ale i varianta SQL bez serveru: SQLite.
Jde o jednoduchou implementaci SQL v jazyce C (přenesenou do Pythonu), které stačí pouze textový soubor - technikálie o správě dat přitom řeší samotný Python modul SQLite, případně C knihovna SQLite.
Tuto variantu se v tomto kurzu naučíme používat.

### Ne-SQL databáze

Existují i databáze založené na jiném než SQL principu, například:
- NoSQL databáze (MongoDB)
- graph databáze (Dgraph, neo4j) - vhodné pro zachycování sociálních sítí

## Databáze SQLite3

SQLite3 je nativním modulem v Pythonu (není třeba instalovat), který umožňuje pracovat s textovým souborem jakoby byl běžnou SQL databází.
Čtení a zápis dat do databáze tak neřeší specializovaný server, který někde musí být nainstalován a dál běžet 24/7, ale namísto toho zápis/čtení řeší přímo modul SQLite3, kdy je potřeba.

SQLite3 není tak rychlé při obrovské velikosti databáze, nebo při zápisu v řádech stovek či tisíců hodnot za sekundu, ale pro většinu menších a středních webů v klidu stačí.
SQLite3 není třeba instalovat, stačí vytvořit prázdný soubor, tím si ušetříme spoustu práce, a nemusí běžet pořád - tím ušetříme výkon stroje, na kterém běží náš webserver.
V případě masivního růstu velikosti projektu, který používá SQLite3, můžeme provést migraci na některou z variant plnohodnotných SQL serverů.

### Terminologie SQLite

Connection - jde o připojení k samotné databázi (v SQLite má význam defacto otevření souboru, v běžném SQL jde o připojení k SQL serveru).

Cursor - objekt vytvořený na daném připojení-connection. Skrze kurzor můžeme volat jednotlivé příkazy SQL.

Execute - konkrétní příkaz, který se má provést - může data vkládat nebo získávat.

Commit - potvrzení, že se mají provedené změny natrvalo zapsat do databáze.

Table - tabulka v rámci databáze (například users, products atd.) - může obsahovat různé množství sloupců (username, email atd.), jednotlivé záznamy jsou řazeny v rows/řádcích (řádek=1uživatel).   

### Začínáme s SQLite3

Než začneme musíme vytvořit prázdný soubor, který bude SQLite3 používat k ukládání dat do databáze.
Pro tuto kapitolu budeme používat název souboru `example.db`.

Když je soubor vytvořen, začneme tím, že vytvoříme skript `create_table.py` v rámci něhož v databázi vytvoříme nový table (novou tabulku - do níž poté můžeme zapisovat jednotlivé záznamy):

```python
import sqlite3 #importujeme modul sqlite3

# pripojime se k databazi
conn = sqlite3.connect('example.db')

#na pripojeni vytvorime kurzor - pres tento kurzor pote muzeme provadev prikazy - execute()
c = conn.cursor()

# Pomocí funkce execute() vytvoříme table, který má 6 sloupců:
# 2 textové (text) sloupce pojmenované: username, email
# 1 sloupec s reálným číslem (real) pojmenovaný: credit
# 1 sloupec s celým číslem (int): vek
c.execute("CREATE TABLE users (username text, email text, credit real, vek int)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
```

Nyní máme v databázi `example.db` jeden table/tabulku pojmenovanou `users`, která má 6 sloupců.
Teď můžeme do této tabulky zapsat nové hodnoty, vytvořme soubor `main.py` a pojďme na to:

```python
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

### ZÁPIS DO DATABÁZE

# Insert a row of data
c.execute("INSERT INTO users VALUES ('agajdosi','gajdosik@gmail.com', 101.65, 27)")

# další řádek dat
c.execute("INSERT INTO users VALUES ('petra','petra@gmail.com', 560.00, 29)")

# Save (commit) the changes
conn.commit()

### ČTENÍ Z DATABÁZE

# data získáme pomocí SQL příkaz SELECT, * má význam, že chceme všechny sloupce
c.execute('SELECT * FROM users')

# z kurzoru nyní můžeme dostat výsledky
# pomocí metody fetchone() získáme jeden řádek
row = c.fetchone()

# řádek je typu tuple, tedy seřazený neměnný seznam prvků
# například: ("agajdosi", "andreas.gajdosik@gmail.com", 101.65, 27) 
# můžeme vypsat prvky tuplu:
print("user:", row[0], "mail:", row[1], "kredit:", row[2], "vek:", row[3])

# Kdyz jsme hotovi, nezapomeneme zavrit pripojeni k databazi
conn.close()
```

Někdy se může hodit získat všechny řádky a ne pouze ten první, pro to můžeme použít metodu `fetchall()`:

```python
# alternativně můžeme použít metodu fetchall() k získání seznamu všech řádků:
c.execute('SELECT * FROM users')
rows = c.fetchall()

# přes seznam řádků samozřejmě můžeme procházet pomocí cyklu FOR
for row in rows:
    print("user:", row[0], "mail:", row[1], "kredit:", row[2], "vek:", row[3])
```

