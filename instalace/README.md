# Instalace externích modulů

## Virtuální prostředí

Nejjistější způsob, jak  instalovat externí moduly, je použít virtuální prostředí.
Pro každý projekt tak můžeme mít izolované prostředí, které nebude sdílet moduly s jinými projekty ani se systémem.

### Vytvoření virtuálního prostředí
Pro vytvoření virtuálního prostředí použijeme modul venv, který je součástí standardní knihovny Pythonu.
Otevřeme terminál, případně PowerShell, pomocí `cd` se přesuneme do složky projektu, na kterém chceme pracovat a zadáme následující příkaz:

```
python -m venv .venv
```
`python` - voláme příkaz pyhon
`-m venv` - říkáme, že chceme použít modul venv
`.venv` - název složky, ve které bude virtuální prostředí vytvořeno (název .venv je konvencí)

Nyní bychom ve složce našeho projektu měli vidět novou složku `.venv`, která obsahuje virtuální prostředí.
Pokud ji nevidíme, můžeme mít v našem prohlížeči souborů nastaveno, že se nám nezobrazují skryté soubory a složky, protože název `.venv` začíná tečkou, což je konvence pro skryté soubory a složky.

### Aktivace virtuálního prostředí
Virtuální prostředí je potřeba aktivovat, aby se nám při instalaci modulů a spouštění Pythonu používalo právě toto prostředí.
Aktivace je nutné provést v každém nově otevřeném terminálu/PowerShellu, ve kterém chceme s projektem pracovat.

Linux/MacOS:
```
source .venv/bin/activate
```

Windows (PowerShell):
```
.venv\Scripts\Activate.ps1
```

PowerShell nám může při pokusu o aktivaci virtuálního prostředí hlásit chybu, že skript nelze spustit, protože je zakázaný.
To je způsobeno nastavením bezpečnostního Execution Policy, které určuje, jaké skripty je možné spouštět.
Pro povolení spouštění skriptů můžeme použít následující příkaz, který nám umožní spouštět skripty pouze v rámci aktuálního uživatelského účtu:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Poté by již aktivace měla fungovat bez problémů.
