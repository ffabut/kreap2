# Lekce 8: Spolupráce - Git a GitHub

Proč se k programování učit ještě systém pro správu verzí jako je Git?
Proč si zanášet hlavu další problematikou?

1. Git nám dá přehled o vývoji kódu v čase (lépe se hledají vlastní omyly).
2. Když něco pokazíme, můžeme se vždy vrátit k verzi kódu před měsícem/týdne/včera večer.
3. Git nám pomůže pracovat ve více lidech - pomůže efektivně vyřešit to, když 2 lidé editovali stejný soubor.
4. S Gitem můžeme vytvářet souběžně více verzí kódu - `branch` - a efektivně mezi nimi přeskakovat
5. Git ulehčuje zálohování kódu - lehce se s ním nahrává na síť GitHub, lehce se s ním kód stahuje z GitHubu na jiné počítače - třeba na server, kde běží náš web.

Psaní softwaru není jednorázová záležitost, ale spíše kontinuální činnost.
V programu je vždy co zlepšovat (uživatelé nachází chyby) a i když by nebylo, vychází nové verze operačních systémů, nové verze modulů, programovacích jazyků a také se mění data, weby, databáze a API, na kterých je náš program závislý.

## Git (a GitHub)

Git je open source nástroj pro správu verzí a historie kódu.
Je dostupný na Windows, Mac i Linux.
Je velmi rozšířený a defacto je průmyslovým standardem.
Pokud bychom chtěli pracovat jako programátorky nebo obecně v IT, budeme se muset Git naučit.
Při pohovoru je znalost Gitu velkou výhodou.
Znalost Gitu nám pomůže i z pozice designéra/3D modeláře/grafičky pokud budeme spolupracovat s nějakou programátorkou - spolupráce bude efektivní a programátorky to ocení.

Github je sociální síť pro programátory, která umožňuje přes Git nahrávat kód online.)
Github krom ukládání nahraných repositářů také přehledně zobrazuje historii změn a další vychytávky.

### Terminologie

Git používá speficickou terminologii, kterou je lepší si dopředu vysvětlit.

#### Repository

Repository (repozitář) představuje defacto projekt.
V praxi jde o složku, v které máme uloženy naše zdrojové soubory a kterou Git sleduje.
Složka může obsahovat jak soubory, tak další složky - vše bude Git sledovat.
Git informace o změnách ukládá do vlastní podsložky `.git` - nemusí nás zajímat, ale je tam.

Pokud repozitář nahrajeme online, pak jej Github zobrazí jako oddělenou podstránku, která bude obsahovat přehled důležitých informací o našem projektu.

#### Commit

Commit je defacto uložení stavu kódu, které je doprovozeno určitým komentářem - názvem commitu, který říká, co zhruba jsme změnili.
Commit představuje všechny změny "od posledně".
V ideálním případě commitujeme po měnších částech a commitujeme změny, které už fungují.
Commity se řadí za sebe do řady a tím vytváří historii.

#### Branch

Repositáře mohou obsahovat více souběžných verzí projektu - říkáme jim branches/větve.
V základě pracujeme na větvi master.
Ale můžeme vytvořit další branche - na masteru například můžeme mít hlavní verzi programu a v branchi experimental se můžeme současně s tím pokoušet o nějaké nové featury atd.
Mezi branchemi můžeme přepínat, takže můžeme přepnout do master, udělat změny, commitnout do masteru, pak přepnout do experimental, udělat změny, commitnout a jít zase pracovat na master.

Jednotlivé branche pak budou mít rozdílné historie - master a experimental budou mít každá jen ty commity, které jsme na nich commitli.

#### Fork

Pokud se nám nějaký projekt líbí, můžeme jej forknout - vytvořit si na GitHubu vlastní "kopii"/fork celého repositáře a na něm začít dělat vlastní změny.

#### Origin

Origin označuje původní umístění našeho repozitáře.
Často je to prostě adresa našeho repozitáře/projektu na Githubu.
Git díky tomu ví, kam má nahrávat a odkud si brát nové změny.

#### Remote

Remote označuje kopii originu - nejčastěji složku na PC, v které děláme změny, které potom nahráváme do původního hlavního repozitáře.

#### Github

Na Github můžeme nahrávat naše repozitáře.
Je to prostě jen server, který je schopný komunikovat s Gitem, ukládat a poskytovat repozitáře.
(Plus zobrazovat cool doprovodné informace online.)

Existují ale i další online varianty - například Gitlab, Bitbucket, BeanStalk.

Stejně tak můžeme rozjet vlastní Gitový server někde u sebe, nebo online - k tomu můžeme použít třeba Gitlab (Gitlab nabízí jak online platformu, tak i open source kód, který si můžeme sami rozjet a sami se o něj starat).

### Instalace Gitu

Git by měl jít nainstalovat bez větších potíží na Windows, Mac i Linux podle vygoogleného návodu.
Případně je návod zde: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

Než však Git začneme naplno používat, je potřebna nastavit v gitu svoje jméno a email.
Git totiž všechny změny podpisuje - aby lidé věděli, kdo danou změnu udělal a nezapomínalo se na autorky a autory, byť dávají svůj kód často svět zadarmo a svobodně jako open source.
Díky emailu je také možné autorky kontaktovat - třeba kvůli otázce, jak jejich kód funguje, nebo pokloně, jak je ten kód strašně elegantně chytrý.

Nastavení jména a emailu provedeme těmito příkazy:

```
git config --global user.name "Lucie Limitová"
git config --global user.email "lucie@gmail.com"
```

### Základní workflow s GitHubem a Gitem

#### Založení repozitáře (přes Github)

Repositář můžeme založit dvě způsoby - buď lokálně, anebo přímo na Githubu (případně).
Pro jednoduchost teď začneme založením přes GitHub.

Na Githubu si vytvoříme účet, logneme se a vpravo nahoře vedle naší profilovky zmáčkneme na tlačítko `++`.
Z nabídky poté vybereme `new repository`.
Repozitář pojmenujeme, můžeme přidat popis v description a vybereme zda bude repozitář veřejný nebo soukromý (veřejný je lepší - ostatní tak uvidí, jak jsme šikovní).

Dále můžeme vybrat licenci (jestli bude náš projekt cool a open source), přidat README.md (soubor obsahující návod k našemu programu) a případně pridat soubor `.gitignore` (obsahuje názvy souborů, které má git ve složce ignorovat).

Po založení repozitáře nás Github přesměruje na domovskou stránku repozitáře, ta má adresu `https://github.com/mujnick/nazevrepozitare`. 
Repozitář buď bude prázdný, anebo bude již obsahovat licenci, readme, případně gitignore, pokud jsme zvolili, aby nám tyto soubory GitHub rovnou vytvořil.

#### Clone - vytvoření kopie repozitáře na PC

Abychom mohli začít pracovat s repozitářem na našem počítači, musíme repozitář z GitHubu naklonovat - git jej stáhne a vytvoří lokální kopii.

1. Otevřeme terminál/příkazovou řádku/powershell
2. Pomocí příkazu `cd` (change directory) najedeme do složky, v které chceme umístit kopii repozitáře - pracovní složka terminálu teď bude `/home/myname/code`, případně jiná lokace, kterou jsme zadali
3. Zadáme název programu/příkazu, který voláme (git), jméno podpříkazu (clone) a jako poslední parametr zadáme adresu repozitáře - git nám v pracovní složce, v které se terminál nachází, vytvoří novou složku nazvanou jménem našeho repozitáře a do ní stáhne veškeré soubory celého repozitáře. Repozitář v našem příkladu bude na adrese: `/home/myname/code/repositoryname`.

```
cd /home/myname/code
git clone https://github.com/myusername/repositoryname
```

Nyní v repozitáři můžeme vytvářet soubory, které potřebujeme, a začít programovat.
Když máme pocit, že jsme něco naprogramovali a chceme to uložit, přejdeme k dalšímu bodu.

#### Staging - označení souborů, které chceme commitovat

Než vytvoříme commit, musíme označit soubory, které chceme commitovat/uložit - takto označené soubory jsou potom staged (připraveny ke commitu a budou součástí commitu).
Ke stagování slouží gitový příkaz `add`.
Postupně označíme všechny soubory, které chceme stagovat do commitu, například:

```
git add main.py
git add README.md
```

#### Commitování změn

Když máme staged soubory, můžeme přejít ke commitování.
K tomu použijeme gitový podpříkaz commit a pomocí flagu `-m` doprovodíme commit zprávou popisující podstatu našich změn:

```
git commit -m This is my first commit, yay!!!
```

Nebo ideálně volit nějakou commit zprávu k tématu změn, například:

```
git commit -m Adding main.py and README
```

Super, právě jsme commitovali naše úpravy!
Nyní můžeme dál pokračovat v programování a pak zase commitovat a tak pořád dokola.

#### Zobrazení historie

Abychom měli důkaz o našich úpravách, můžeme použít gitový podpříkaz `log` k zobrazení historie úprav našeho repozitáře:

```
commit 8438d2d4f0bd5fb7ed32d2e4b52c4cb04fe611af (HEAD -> master)
Author: agajdosi <andreas.gajdosik@gmail.com>
Date:   Tue Apr 28 14:58:46 2020 +0200

    My first commit, yay!!!
```

#### Nahrání commitů na server (GitHub) 

Commitované změny jsou prozatím součástí pouze lokálního repozitáře.
Abychom je nahráli na server, použijeme gitový podpříkaz `push`:

```
git push
```

Git si během klonování uložil umístění původního origin repozitáře, takže ví, kam tlačit změny.
Do repozitáře ale Github nedovolí tlačit každému, proto se nás git zeptá na username a následně na password do GitHubu.

Super, teď jsou naše změny online!

### Commitování přes Visual Studio Code

Pokud používáme editor Visual Studio Code, můžeme ke commitování použít jeho support pro Git.
V tom případě naklonujeme repozitář a výslednou složku otevřeme ve VSCode.
Když poté ve VSCode vytvoříme nové soubory nebo složky, změny se ukážou v panelu Source Control - ten jeho ikonka je dostupná v levém svislém menu (3 tečky propojené čárou do tvary písmene Y).

Když toto menu rozklikneme, uvidíme v levém panelu změny - uvedené pod nadpisem Changes.
Jednotlivé soubory pak můžeme přidat do stage přes symbol `+`.
Nahoře poté můžeme zadat commit message a commitovat enterem.
To nám ulehčuje celý proces commitování.

#### Příkazová řádka ve VSCode

Pokud ve VSCode zmáčkneme klávesovou zkratku `ctrl+shift+;` otevře se v dolní části VSCode panel terminálu.
Ten má rovnou nastavenou working directory na složku otevřenou ve VSCode (náš projekt) a nemusíme tak přepínat nikam pomocí `cd`, ale můžeme rovnou `push`ovat:

```
git push
```

Po vyzvání zadáme username, password a máme vše nahráno na GitHub!

### Branch - větvení

Gitové repozitáře můžeme větvit - vytvářet více variant kódu na jednotlivých větvích.
Na hlavní větvi `master` můžeme průběžně opravovat chybičky našeho programu, zatímco na větvi `future` můžeme dělat radikální změny a zkoušet budovat zcela novou verzi našeho programu - experimentovat.
Nemusíme přitom mít pro každou verzi novou kopii složky repozitáře, ale stačí v gitu přepínat branche.
Jak na to?

#### Master branch

Základní branch je nazvaná `master` - v ní se až doposud nacházíme, je vytvořena při každém vytvoření nového repozitáře.
Na `master` branch je dobré mít nejaktuálnější stabilní verzi našeho projektu, je to takový kmen.


#### Podpříkaz branch
Branch na kterém se nacházíme zjistíme pomocí gitového podpříkazu `branch`:
```
$ git branch
 * master
```

#### Vytvoření nové větve: git checkout -b

Pokud chceme začít nezávazně experimentovat, můžeme vytvořit novou branch `experiment` a na ní dělat úpravy.
K vytvoření nové větve slouží gitový podpříkaz `checkout` a flag `-b`:

```
$ git checkout -b experiment
 Switched to a new branch 'experiment'

$ git branch
 * experiment
```

#### Přepnutí na jinou branch

K přepnutí na jinou existující branch opět použijeme gitový podpříkaz `checkout`, protože branch existuje, už nemusíme používat flag `-b`:

```
$ git checkout master
 Switched to a branch 'master'

$ git checkout experiment
 Switched to a branch 'experiment'
```



### Pull - stažení nových změn

Občas se může stát, že na origin repozitáři jsou změny, které nemáme v lokálním repozitáři.
Například jsme programovali na jiném počítači, vytvořili několik commitů a pushli je na github.
Jak sesynchronizovat zastaralý lokální repozitář s novými změnami?
Použijeme gitovský podpříkaz `pull`:

```
git pull
```

Git pull stáhne změny z origin repozitáře a nové commity aplikuje na naši historii.
Budeme tak mít vše up-to-date.

### Spolupráce

Nyní máme vytvořený vlastní repozitář na Githubu, máme jej naklonovaný u sebe na počítačí, přidali jsme několik commitů a pushnuli je na Github.
Jak uděláme to, aby s námi někdo mohl spolupracovat?

#### Fork repozitáře na Githubu

Naše spolupracovnice se přihlásí na GitHub, vyhledá náš repozitář, otevře jeho webovou stránku a napravo nahoře klikne na tlačítko `Fork` (pozor repozitář musí být veřejný).
Github následně vytvoří kopii repozitáře na profilu spolupracovnice.

Například:

Původní repozitář se nachází na adrese: `https://github.com/myusername/AwesomeRepository`.
Její fork repozitáře bude nyní na: `https://github.com/herusername/AwesomeRepository`.

#### Clone

Spolupracovnice nyní naklonuje svůj fork:

```
git clone https://github.com/herusername/AwesomeRepository
```

Spolupracovnice teď může začít pracovat na lokální verzi svého forku.
Může dělat stage, dělat commity a pushovat do svého forknutého repozitáře na Githubu, není nijak omezena. 

Oba dva pracujete na vlastních kopiích celého projektu a jste svými pány těchto repositářů.
Github však ví, že její repozitář je forkem toho vašeho, že z něj vychází - a bude tak nabízet možnost přenést její nové změny do vašeho původního repozitáře - tzv. vytvořit `Pull Request`.

#### Pull Request

`Pull Request` je žádostí o to, aby původní repozitář přijal změny provedené na Forku - aby je pullnul do sebe (proto Pull Request a ne Push Request).
Pull request můžeme vytvořit z webové stránky forku na GitHubu.

Při vytváření Pull Requestu vybereme, z jakého forku a větve chceme udělat PR a na který repozitář a větev chceme udělat pull request.

Například:

```
github.com/herusername/AwesomeRepository - master ---> github.com/myusername/AwesomeRepository - master
github.com/herusername/AwesomeRepository - newfeature ---> github.com/myusername/AwesomeRepository - master
github.com/anotheruser/AwesomeRepository - experiment ---> github.com/myusername/AwesomeRepository - master
```

Pull Request se poté zobrazí na původním repozitáři a jeho vlastník či vlastnice (vy) jej můžete přijmout.

##### Pozor - PR se updatuje podle toho, co nově přidáme do branche

Dokud se pull request neuzavře odmítnutím nebo přijetím kódu, do té doby všechny nové změny na dané větvi budou zahrnuty do Pull Requestu.
Pokud uděláme PR s kódem pro nějaké vylepšení a pustíme se do dalšího kódění na stejné větvi, tak všechny nové commity nahrané na danou větev do GH budou živě přidávány do Pull Requestu.
To se hodí, pokud nám vlastník repozitáře řekne, že nám v PR něco chybí/je špatně a máme udělat změny nebo něco přidat.

Pokud je ale vše OK a my jen jedeme dál v přidávání dalších vychytávek, pak akorát přidáme nadbytečný kód do Pull Requestu a dost možná PR vlastník repozitáře nepřijme.

Abychom se tomu vyhli, je ideální dělat nové commity na novém branchi/větvi a do branche, z které je udělán PR, přidávat jen commity týkající se oprav daného PR.

Například z masteru, z kterého máme otevřený PR, se přepneme na novou branch newfeature, kde pokračujeme ve vývoji nových funkcí, aniž bychom měnili kód na master branch, čímž bychom měnili PR:

```
$ git branch
 * master
$ git checkout -b newfeature
 Switched to a new branch 'newfeature'
$ git branch
 * newfeature
```

##### Zavření Pull Requestu

Majitel repozitáře může PR zavřít a tím jej odmítnout.
Případně jej může přijmout, v ten moment se všechny commity v branchi, z které PR vychází, vezmou a překopírují (mergnou) do cílové větve repozitáře (nejčastěji `master`) a vše je hotovo.
Vaše změny jsou nyní součástí originálního repozitáře.

Další změny na branch, která byla součástí PR, se už v originálním repozitáři neprojeví.
Branch tak opět můžeme začít používat k vývoji dalších funkcí, případně ji smazat a jet vývoj na nové branchi.

### Syncování forku s originálním repozitářem

Občas se stane, že na originálním repozitáři přibydou commity, a my bychom je chtěli nahrát k nám do forku, abychom měli čerstvé změny a měli fork syncnutý s originálem.

#### Přidání dalšího repozitáře jako `remote`

Repozitář, z kterého chceme čerpat commity, si nejprve přidáme jako `remote`, aby git znal adresu takového repozitáře.
Pojmenujeme si jej jak chceme, pro originální repozitář můžeme použít například název `upstream` - místo nad proudem, z něhož my dále pod proudem čerpáme nejnovější změny:

```
$ git remote
 origin
$ git remote add upstream https://github.com/originalauthor/awesomerepo
$ git remote -v
 origin https://github.com/myusername/awesomerepo (fetch)
 origin https://github.com/myusername/awesomerepo (push)
 upstream https://github.com/originalauthor/awesomerepo (fetch)
 upstream https://github.com/originalauthor/awesomerepo (push)
```

Origin je místo, odkud jsme naklonovali náš repozitář (fork).
Upstream je nyní místo, kde sídlí originální repozitář.

#### Stáhnutí změn z remote

Změny obsažené na vzdáleném repozitáři můžeme stáhnout pomocí příkazu `fetch`.
Z remote repozitáře `upstream` to můžeme udělat takto:

```
$ git fetch upstream
```

Git nám poté vypíše, jaké nové změny na tomto repu jsou - nové branche a další změny.

#### Aplikování změn na naši lokální branch

Před aplikací přepneme na větev, na kterou chceme aplikovat změny.
Dejme tomu, že chceme aplikovat na nás lokální `master`, aby byl up-to-date s `master` na originálním repozitáři:

```
$ git checkout master
```

Když jsme na našem masteru, můžeme aplikovat změny.
Použijeme příkaz `rebase` a zvolíme z jakého remote repozitáře a z jaké jeho větve, nyní chceme z remote `upstream` a z něj větev `master`:

```
$ git rebase upstream/master
```

### Rebase - braní commitů z našich jiných branchí

Dejme tomu, že jsme vynalezli super změny na branchi `experiment` a teď je chceme do `masteru`?

Pak přepnem (checkout) na master a dáme rebase z `experiment`:

```
$ git checkout master
$ git rebase experiment
```

To nám do branche master natáhne změny z experiment.

### Několik dobrých zásad

- branch `master` mějme jako hlavní branch, na které je fungující kód
- PR dělejme z nemaster branchi - pokud chceme udělat PR našeho masteru, udělejme novou branch třeba `prmaster` a PR udělejme z ní
- branch `master` se snažme mít co nejaktuálnější s originálním upstream repozitářem

## Další zdroje ke Gitu

[Kompletní online kniha o Gitu - Gitbook](https://git-scm.com/book/en/v2)
