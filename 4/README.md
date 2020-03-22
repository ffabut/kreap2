# Interakce s uživatelkou

Pokud chceme, aby náš web interagoval na uživatele a uživatelky, máme dvě základní možnosti:

- interakce v prohlížeči uživatelky (použijeme JavaScript)
- interakce na straně serveru (jazyk v kterém je napsán náš server, v našem případě Python)

Obě řešení přitom mají svá pro a proti a velká část úvah, plánování a realizace interakce s uživatelem je právě otázkou volby mezi prolížečem a serverem.

## Interakce v prohlížeči
Spousta interakcí je přítomná z důvodu UI (user interface) nebo UX (user experience) designu, jde o otevírající se meníčka, blikající tlačítka a podobné, u kterých není tak úplně třeba, aby o nich webový server vůbec věděl.
Takové interakce je ideální nechat na straně uživatelky - tedy v jejím webovém prohlížeči.
Pokud se tak rozhodneme, použijeme k programování JavaScript - jazyk, který je obsažen v ~99% všech webových prohlížečů a který umožňuje pracovat jak s HTML, tak CSS prvky webové stránky, tak i s akcemi uživatelek (klik, potažení myši, vstup klávesnice).
JavaScript nám tak umožňuje pracovat jak s obsahem a formou webu, tak i s akcemi uživatele.

Výhodou interakce na straně prohlížeče:
- nezatěžujeme výpočetně náš server
- nezatěžujeme síťové připojení serveru 
- nezatěžujeme data uživatelky
- je to rychlejší - reaguje browser pod rukou a ne server na druhé straně republiky/kontinentu/planety

Nevýhodou interakce na straně prohlížeče je:
- server o ničem neví
- kód si může v prohlížeči každý prohlédnout (pokud bychom chtěli něco skrývat, touto cestou to nepůjde)
- musíme použít JavaScript (nebo překlad do javascriptu, nebo implementaci Pythonu v JavaScriptu - třeba [Skulpt](http://skulpt.org/))

### Hello JavaScript!

JavaScript se může nacházet buď přímo v HTML souboru, nebo v odděleném souboru `.js`.

Pokud chceme vložit JavaScript přímo do HTML souboru, pak jej vkládáme mezi tagy `<script>`  a `</script>`.
Script tagů může být v dokumentu více.
Je to ale vhodné jen pro velmi jednoduchý kód, cokoliv složitějšího je lepší dát do odděleného souboru.
Hello world v JavaScriptu přímo v HTML může vypadat takto:

```html
<!DOCTYPE HTML>
<html>

<head>
  <script>
    alert( 'Hello, world!' );
  </script>
</head>

<body>

  This is text.

</body>

</html>
```

Mít JavaScript přímo v HTML dokumentu je praktické pro rychlé prototypování aplikace, ale velmi rychle se takové řešení může zvrhnout v nepřehledný chaos.
Proto je praktičtější přesunout JavaScript do odděleného souboru nebo více souborů a ty potom do HTML souboru pouze naimportovat.
Skript naimportujeme opět pomocí dvojice tagů `<script>` a `</script>`, avšak budeme specifikovat atribut `src`, v němž udáme cestu k souboru `.js`, v němž se nachází javascriptový kód.
Script tagy je ideální umísťovat mezi tagy `<head>` a `</head>`, ale není to nutnost - budou fungovat ať už jsou umístěny kdekoliv.

Hello world by potom vypadal takto:

```html
<!DOCTYPE HTML>
<html>

<head>
  <script src="hello.js"></script>
</head>

<body>
  This is text.
</body>

</html>
```

A k tomu soubor `hello.js` na stejné úrovni jako HTML soubor (ve stejné složce):
```javascript
alert( 'Hello, world! (From file hello.js)');
```

Pozor: pokud uvedeme atribut `src`, bude jakýkoliv kód uvedený v tagu `<script>` ignorovaný:

```html
<!DOCTYPE HTML>
<html>

<head>
  <script src="hello.js">
    alert('This will be ignored');
  </script>
</head>

<body>
  This is text.
</body>

</html>
```

Pokud chceme importovat více souborů, použijeme k tomu několik `<script>` tagů:

```html
<!DOCTYPE HTML>
<html>

<head>
  <script src="hello.js"></script>
  <script src="bye.js"></script>
  <script src=".js"></script>
</head>

<body>
  This is text.
</body>

</html>
```

### Více zdrojů k JavaScriptu

JavaScript je sám o sobě velmi obsáhlým tématem, na který v tomto kurzu není možné najít prostor.
Je však v oblasti webu rozhodně velmi užitečný, proto doporučujeme pro zájemkyně a zájemce jeho hlubší samostudium.
Zdroje mohou být například některý z těchto tutoriálů:
- [Úvod do javascriptu: Nepochopený jazyk](https://www.itnetwork.cz/javascript/zaklady/javascript-tutorial-uvod-do-javascriptu-nepochopeny-jazyk)
- [Jak psát web: Úvod do JavaScriptu](https://www.jakpsatweb.cz/javascript/javascript-uvod.html)

## Interakce na straně serveru

I když se dá interagovat s uživatelkami přímo v prohlížeči, existuje celá řada interakcí, které je lepší nebo přímo nutné odbavovat na serveru: registrace, ověřování hesla, výpisy hodnot z databáze, nebo prostě jen algoritmus, který si chceme nechat jen pro sebe schovaný pěkně na serveru, kde se k nimu nikdo nedostane.
V takových případech je lepší zvolit cestu interakce na straně serveru - vyvstává však otázka, jak dostaneme data z prohlížeče na server?

Dostat data z prohlížeče můžeme několika způsoby:
* HTTP metoda `POST`
* * skrze HTML form 
* * skrze JavaScript
* websockets
