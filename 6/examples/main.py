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

# alternativně můžeme použít metodu fetchall() k získání seznamu všech řádků:
c.execute('SELECT * FROM users')
rows = c.fetchall()

# přes seznam řádků samozřejmě můžeme procházet pomocí cyklu FOR
for row in rows:
    print("user:", row[0], "mail:", row[1], "kredit:", row[2], "vek:", row[3])

# Kdyz jsme hotovi, nezapomeneme zavrit pripojeni k databazi
conn.close()
