import requests
from os.path  import basename

r = requests.get("xxx")
soup = BeautifulSoup(r.content)

for link in links:
    if "http" in link.get('src'):
        lnk = link.get('src')
        with open(basename(lnk), "wb") as f:
            f.write(requests.get(lnk).content)

