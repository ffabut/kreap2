# "Kompilace" souborů pomocí PyInstaller

Python je interpretovaný jazyk - skripty tedy můžeme velmi jednoduše spouštět na všech operačních systémech, ale musíme na nich nainstalovat Python.
To může být někdy překážkou.
Abychom nutnost instalovat Python obešli, můžeme se pokusit o to, co dělají kompilované jazyky - zkompilovat Python kód do binárního spustitelného souboru (například: soubor .exe na Windows).
Nevýhodou je, že jde o relativně složitější proces.

Druhou a jednodušší možností je se pokusit kompilaci napodobit - vytvořit bundle.
Neboli zabalit Python interpret, náš skript a všechny potřebné moduly do jedné složky či jednoho souboru, který půjde spustit.
De facto nejde o binární soubor, ale uživatelka to nepozná - může jej stáhnout, jednoduše spustit a to je hlavní.

Pro bundlování můžeme použít:
- na Win, Mac a Linux [modul PyInstaller](https://www.pyinstaller.org/).
- na Windows pro tvorbu .exe modul [Py2exe](http://py2exe.org/)

Ke kompilaci lze použít:
- kompilovat za pomocí modulu [Nuitka](https://nuitka.net/pages/download.html)
- kompilovat za pomocí CPythonu

Vzhledem k jednoduchosti a podpoře klíčových platforem se zaměříme na Pyinstaller.

## Instalace

PyInstaller je modulem 3. strany, takže jej musíme prvně nainstalovat přes `pip`:

```
pip install --user pyinstaller
```

Kromě modulu pyinstaller se během toho nainstaluje i spustitelný soubor `pyinstaller`, který budeme posléze používat pro tvorbu bundlů.

## O Pyinstalleru

Pyinstaller umožňuje bundlovat Python skripty jak na Windows, Mac, tak Linux.
Ale pozor: není možné vytvářet bundle na jiný operační systém než na ten, na kterém `pyinstaller` spouštíme - nejde dělat tzv. cross-compilation, či spíš cross-bundling.
Abychom vytvořili verze pro všechny hlavní operační systémy, musíme:
- bundle pro Windows bundlovat na Windows,
- bundle pro Mac bundlovat na Mac,
- bundle pro Linux bundlovat na Limuxu.

Je to trochu opruz, ale i řada jazyků na tom není o moc lépe.
V praxi se často používají virtual machines (například VirtualBox, KVM atd.), CI služby umožňující spouštění skriptů na dočasně půjčených Win/Mac/Linux strojích (např. [Github Actions](https://github.com/features/actions)), nebo fyzicky běžící stroje u vývojářů a holt se "buildí" na 3 pro to vyhrazených noteboocích...

## Bundling

Pyinstaller nemusíme importovat do souboru, ale namísto toho jej voláme jako program v příkazové řádce.
Prvním parametrem je cesta nebo název skriptu, který chceme zabundlovat.
Nakonec použijeme flag `--onefile`, který způsobí, že výstupem pyinstalleru nebude složka obsahující všechny potřebné dependence, ale pouze jeden zkomprimovaný a spustitelný soubor:

```
pyinstaller main.py --onefile
```

Poznámka: Pokud by se náš Python program skládal z více souborů, budeme pyinstaller volat na ten soubor, z něhož importujeme všechny ostatní, a skrze který náš program běžně spouštíme pomocí Pythonu `python main.py`. Takový ústřední/startovní/vstupní soubor, z něhož importujeme vše ostatní budeme mít dost často pojmenovaný právě `main.py`.

Při svém běhu `pyinstaller` vytvoří několik souborů a složek, jsou jimi:
- `*.spec` file (pojmenovaný dle názvy skriptu, tedy např. `main.spec`), který udržuje nastavení toho, jak bundling probíhá. Dá se tunit, ale pro jednodušší projekty se jím nemusíme vůbec zaobírat.
- složka `build`, v níž pyinstaller uchovává metadata a další pro něj potřebné záznamym, také nás nemusí moc trápit
- složka `dist`, v níž se objeví spustitelný soubor (anebo složka obsahující všechny dependencies včetně spustielného souboru, pokud jsme nezvolili možnost `--onefile`). Spustitelný soubor i případná složka budou pojmenovány stejně jako náš originální skript, v našem ukázkovém případě tedy `main`. Později je samozřejmě můžeme přejmenovat na něco hezčího.

Celá struktura vypadá následovně:

```
example/
├── build
│   └── main
│       ├── Analysis-00.toc
│       ├── base_library.zip
│       ├── EXE-00.toc
│       ├── localpycos
│       │   └── struct.pyo
│       ├── PKG-00.pkg
│       ├── PKG-00.toc
│       ├── PYZ-00.pyz
│       ├── PYZ-00.toc
│       ├── warn-main.txt
│       └── xref-main.html
├── dist
│   └── main
├── main.py
├── main.spec
└── __pycache__
    └── main.cpython-39.pyc
```

## Spouštění

To, že vše funguje, jak má, můžeme vyzkoušet v příkazové řádce:

```
dist/main
```

případně na Windows:

```
dist/main.exe
```

## Distribuce

Zabundlovaný soubor nyní můžeme přejmenovat dle libosti a distribuovat uživatelkám, které mají stejný OS jako my.
Ty poté budou schopny jednoduše spustit tento soubor, aniž by musely instalovat Python:

```
muj-prvni-bundle.exe
```

Pokud bychom chtěli vytvořit verze i na další operační systémy, pak musíme celý proces zopakovat na strojích, které na těchto OS běží.
Často můžeme vynechat Linux (lidi na Linuxu si binárku dost často sami udělají), takže nám stačí 2 stroje: jeden Windows a jeden Mac pro tvorbu fajn spustitelných souborů. 
