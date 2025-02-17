import requests

r = requests.get("https://www.favu.vut.cz/fakulta/historie-soucasnost")

if print(r.status_code) != 200:
    print("Status code není 200, asi se něco pokazilo! Ale zkusme to dál...")

# vypiseme stazeny soubor
print(r.text)

# r.text bychom klidne mohli rovnou vrátit v RequestHandleru
# a defacto tak na našem webu zobrazovat cizí HTML
