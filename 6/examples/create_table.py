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
