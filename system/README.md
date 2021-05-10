# Automatizace ovládání operačního systému z Pythonu

V různých situacích se nám může hodit ovládat operační systém z Pythonu - například automatické spouštění VLC na výstavě, automatizování klikání ve webovém prohlížeči, kopírování složek a souborů atd.
Většinu z těchto věcí bychom mohli nakódit i v PowerShellu, či Bashi (terminalu na Mac a Linux) - avšak tento kód by byl pravděpodobně použitelný pouze na daném operačním systému.
Pokud bychom chtěli, aby náš kód byl univerzálně použitelný, pak je nejvhodnější volbou Python.

Dnes se podíváme na některé možnosti, které Python nabízí pro automatizaci úkonů v operačním systému.

## Informace o systému: built-in moduly os a platform

V některých případech se nevyhneme tomu, aby se skript lehce lišil na Windows, Mac a Linux.
Nebo nás prostě zajímá na jakém systému skript běží.
Abychom toto detekovali, můžeme použít například následující funkce:

```python
import os, platform

### Modul os
uname = os.uname()
print("<<< OS module >>>")
print("system name:", uname.sysname)
print("OS release:", uname.release)
print("version:", uname.version)
print("architecture 32/64bit/ARM atd:", uname.machine)
print("network name:", uname.nodename)

print("username:", os.getlogin())

### Modul platform je doporucovany zpusob, jak zjistovat info o systemu
print("\n<<< PLATFORM module >>>")
print("architecture:", platform.architecture())
print("platform:", platform.machine())
print("processor:", platform.processor())
print("python version:", platform.python_version())
print("uname:", platform.uname())
```

Plná dokumentace modulu `os` je dostupná na: https://docs.python.org/3/library/os.html  
Plná dokumentace modulu `platform` je dostupná na: https://docs.python.org/3/library/platform.html  

## Práce se soubory: built-in modul os a os.path

Modul `os` nabízí funkce pro otevření, čtení, zápius a zavření souborů:
- https://docs.python.org/3/library/os.html#os.open
- https://docs.python.org/3/library/os.html#os.read
- https://docs.python.org/3/library/os.html#os.open
- https://docs.python.org/3/library/os.html#os.close

Tyto funkce se hodí pro práci se soubory na úrovní bytů, pokud bychom chtěli dosánout velkých rychlostí zápisu apod, jak zmiňuje jejich dokumentace:

```
This function is intended for low-level I/O. For normal usage, use the built-in function open(), which returns a file object with read() and write() methods (and many more). To wrap a file descriptor in a file object, use fdopen(). 
```

Pro běžné použití je lepší použít funkci přímo `open()` dostupnou přímo v Pythonu bez potřeby importování `os`:

```
file = open('dog_breeds.txt')
```

### Tvorba a destrukce složek a souborů

Modul `os` umožňuje tvorbu, přejmenovávání, přesuny a mazání souborů a složek, více v příkladu:

```
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
```

## Spuštění programu z Pythonu: built-in modul subprocess

Pro spouštění dalších programů z Pythonu je nejlepší využít modul `subprocess`, dokumentace na: https://docs.python.org/3/library/subprocess.html?highlight=subprocess#module-subprocess.
Programy tímto způsobem spouštíme, jako bychom je volali z příkazové řádky - pokud chceme spustit program, který má grafické rozhraní, musíme nejprve zjistit, jak se spouští ne přes ikonu, ale přes příkazovku.

Například pro Google Chrome na Linuxu:
```
google-chrome twitter.com
```

Ideální je Googlit "How to open XYZ in Windows/Mac/Linux from terminal".

A nyní již příklad použití:

```python
import subprocess

subprocess.run("ls") #prvni argument je nazev programu, anebo seznam retezcu ["nazev-programu", "argument1", "argument2"...]
subprocess.run(["ls", "-a", "-x"]) # jako bychom v terminalu volali: "ls -a -x"

subprocess.run(["google-chrome", "seznam.cz"]) #zde se skript "zasekne", dokud program nedoběhne - v tomto případě když zavřeme okno prohlížeče
print("konec!")
```

Občas se nám hodí získat textový výstup volaného programu, v takovém případě můžeme použít:

```python
import subprocess

subprocess.run("ls", shell=True, check=True)
```

Větší příklad využití modulu je zde:

```python
import subprocess, time

subprocess.run("ls", shell=True, check=True) # shell=True vypise textovy vystup programu rovnou do konzole
#argument check=True zaridi, ze Python vypise chybu, pokud program skoncil chybou


result = subprocess.run("ls", capture_output=True) #zachyti textovy vystup, ten bude dostupny v navracenem objektu
print(result.stdout, result.stderr) #stdout standardni vystup programu, stderr vypisy errorovych hlasek

result.check_returncode() #zkontroluje, zda program skoncil spravne - alternativa check=True, pokud doslo k chybe, vyvola Exception Error


try: #volani zaobalime do try-except statementu, abychom v except mohli reagovat na timeout exception
  result = subprocess.run(["google-chrome", "ffa.vutbr.cz"], timeout=5) #timeout omezi beh programu na dany pocet sekund, pote jej nasilne ukonci
except subprocess.TimeoutExpired: #reagujeme na timeout exception, takze skript neskonci chybou, ale muze bezet dal
  print("timeout passed")


process = subprocess.Popen(["google-chrome", "avu.cz"]) #Popen neblokuje dalsi prubeh programu

print("process obsahujici prohlizec bezi a my pokraujeme v nasem python kodu")
time.sleep(10) #chvili pockame
process.kill() #a potom process ukoncime

print(process.stdout, process.stderr) #vypiseme stdout a stderr, jestli program nehodil nake chybove hlasky
```


