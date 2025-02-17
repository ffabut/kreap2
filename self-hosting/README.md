# Lekce 10: Jdeme online

Až doposud jsme náš server spouštěli pouze lokálně.
A to buď u sebe na počítačí, anebo na repl.it.
Dneska jej zkusíme spustit na virtuálním serveru pod naší vlastní doménou. 

## Obecný popis celé situace

Pokud chceme, aby náš Tornado webserver byl dostupný pod nějakou adresou (například `www.mujserver.cz`), musíme udělat několik kroků:

1. mít server, na kterém náš Tornado kód poběží
2. mít zaregistrovanou doménu
3. nastavit DNS domény, aby směřovaly na IP adresu našeho serveru

## Server

### Jaký server?

Jaký přesně server použijeme, je relativně jedno - může jít o pronajatý fyzický stroj někde v zámoří, může jít o virtuální stroj (na jednom výkonném serveru běží až desítky virtuálních slabších serverů), ale klidně to může být nějaký starší notebook u nás doma.
Může jít o stroj, který běží na operačním systému Linux, Windows nebo i Mac.
Obecně je nejpopulárnější asi Linux, jelikož je zdarma, svobodný a bezpečný.

Naprosto nezbytnou povinností ale je, aby náš server měl statickou IP adresu.
Co to znamená?
IP adresa počítačů se může měnit - například když s notebookem přejdeme do jiné WIFI sítě, ale i může se měnit i u nás doma - většina poskytovatelů negarantuje, že na domácí síti budeme mít statickou IP adresu (může se nám tak ze dne na den měnit).
Důvodem je to, že IP adres je málo a tak poskytovatelé šetří.

Pokud by se IP adresa našeho serveru neustále měnila, měli bychom problém - návštěvníci a návštěvnice by náš server druhý den už nenašli.
Proto naprosto bezpodmíněčně potřebujeme server se statickou IP adresou - s IP adresou, která se nemění a zůstane pořád stejná.

### Otevření portu 80 a 443

Internetové připojení je by default realizováno přes port 80 (HTTP) a 443 (HTTPS) - operační systémy ale tyto porty mají defaultně zavřené a jakékoliv připojení odmítají.
Namísto webu by se nám tak objevila jen hláška `Unable to connect` nebo `Connection refused`.

Aby náš server mohl poskytovat webové stránky, musíme otevřít port 80, případně i 443.

### Spuštění Tornado webu

Nyní máme otevřený port, ale na stroji neběží nic, co by odbavovalo příchozí HTTP požadavky a vracelo zpět požadované webové stránky.
Musíme tak spustit námi napsaný Tornado web server.
Máme přitom dvě možnosti:
- spustit tornado server na portu 80 jako administrátor/root
- nebo jej spustit na jiném volném portu, například na 8080, a nastavit přesměrování z portu 80 na port 8080

Po spuštění Tornada by web měl být dostupný na IP adrese našeho serveru, stačí jej zadat do prohlížeče a zkontrolovat, IP adresa může být například: `165.80.17.16`.
(Port 80 nemusíme přidávat (`165.80.17.16:80`), prohlížeč si jej přidá sám.)

## Doména

Server běží a web je dostupný na IP adrese, což je fajn, ale ne moc praktické - lidi si jen těžko budou pamatovat takto hnusné číslo.
Proto bylo vytvořeno DNS - domain name system, který nám umožní zaregistrovat nějakou čitelnou doménu (například `mujserver.cz`) a tu v pozadí nasměrovat na IP adresu našeho serveru.
Uživatelky a uživatelé se tak vůbec nemusí starat o IP adresy webů, které navštěvují, a prostě jen vidí čitelná a jasná jména.

Doménu musíme zaregistrovat u některého z registrátorů domén.
Můžeme použít například https://www.forpsi.com/ nebo https://www.wedos.cz/, ale i řadu dalších registrátorů.

### Nastavení DNS

Když máme zaregistrovanou doménu, musíme nastavit samotné DNS.
Přes uživatelské rozhraní registrátora se doklikáme k nastavení DNS pro naši doménu a poté nastavíme A record na IP adresu našeho serveru.
Například:

```
hostname        TTL     type       value
mujserver.cz	1800	A	       185.199.111.153
```

Aby DNS přesměrovávalo i variantu adresy s předponou (subdoménou) www, můžeme nastavit další CNAME record, který www.mujserver.cz přesměruje na mujserver.cz, který poté bude nasměrován na IP adresu:

```
hostname           TTL     type       value
mujserver.cz	   1800	   A	      185.199.111.153
www.mujserver.cz   1800    CNAME      mujserver.cz
```

Po nastavení DNS je potřeba počkat až několik hodin, než se změna projeví na světových DNS serverech.
Poté již bude náš web viditelný pod naší doménou a ne jen pod IP adresou, takže například na adrese: `mujserver.cz`.

## Příklady

TODO

### Nastavení služby na serveru

RHEL/CentOS/Fedora:

```
[Unit]
Description=My Server
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=myuser
WorkingDirectory=/home/myuser/server-code
ExecStart=python3 -u /home/myuser/server-code/main.py

[Install]
WantedBy=multi-user.target
```

