import os, shutil

wd = os.getcwd() # ziskame working directory (odkud jsme volali skript)
scriptDirectory = os.path.dirname(os.path.realpath(__file__)) # cesta, kde je umisten nas skript
# pokud jsme volali python ze slozky, kde je skript, pak budou stejne
# ale pokud jsme volali "python python/main.py" skript z /home/me a skript je v /home/me/python/main.py, pak se budou lisit

print(wd, scriptDirectory)

contents = os.listdir(scriptDirectory)
print(contents) #seznam obsahujici nazvy souboru a slozek ve slozce

# zmena working directory
os.chdir(scriptDirectory) # nyni je working directory uz urcite ve slozce, kde je nas skript

#vytvareni nove slozky
os.mkdir("novaSlozka")
os.mkdir("jinanovaSlozka")
print(os.listdir(wd))

#vytvareni nove slozky, vcetne slozek, ve kterych je, paklize neexistuji:
os.makedirs("slozkaneexistuje/takyne/uzurcitene/mojeNovaSlozka") # toto projde bez problemu, funkce vytvori vsechny slozky, ktere v ceste neexistuji
# os.mkdir("slozkaneexistuje2/takyne2/uzurcitene2/mojeNovaSlozka") # toto by ale neproslo, protoze cesta slozkaneexistuje2/takyne2/uzurcitene2
# v ktere chceme vytvorit mojeNovaSlozka neexistuje, doslo by k erroru
print(os.listdir(wd))

#prejmenovani/presunuti souboru nebo slozky, neprojde pokud nove jmeno jiz existuje
os.rename("novaSlozka", "prejmenovanaSlozka")
print(os.listdir(wd))

#prejmenovani/presunuti souboru nebo slozky, projde, pokud cilove jmeno existuje (replace puvodniho souboru/slozky)
os.replace("prejmenovanaSlozka", "jinanovaSlozka")
print(os.listdir(wd))

#Mazani
# os.remove() # odstrani soubor
os.rmdir("jinanovaSlozka") #odstrani prazdnou slozku
print(os.listdir(wd))

shutil.rmtree("slozkaneexistuje") #vymaze slozku a vsechen jeji obsah, davat pozor!!!!
print(os.listdir(wd))
