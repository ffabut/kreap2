"""Jednoduchy program na monitorovani webkamery a prubezne stahovani aktualniho obrazku. Jde vlastne o jednoducheho daemona.
Krome ukazky stahovani obrazku, ukazuje taky jak udelat program, ktery se bude stale opakovat, pobezi "donekonecna" na pozadi.
To je resene hlavne nekonecnym while cyklem a try-except blokem, ktery zachyti chyby a zachrani program pred zastavenim v pripade chyb - napr. vypadku internetu.
"""

import requests
from bs4 import BeautifulSoup
import re
import os
import time

URL = "https://www.hvezdarna.cz/zive/kamera/"
OUT = "./images"
os.makedirs(OUT, exist_ok=True) # vytvori adresar, pokud neexistuje


def get_image_URL() -> str:
  """Download HTML page and extract the URL of the image."""
  resp = requests.get(URL)
  soup = BeautifulSoup(resp.text, 'html.parser')
  image = soup.find("img", src=re.compile(r'\/ryba\/day_latest\.jpg\?\d{10,11}'))
  image_url = f"https://www.hvezdarna.cz{image['src']}"
  return image_url


def download_image(url: str) -> str:
  """Download the image located on the URL."""
  image_name = url.split("?")[1] + ".jpg"
  image_dest = f"{OUT}/{image_name}"

  exists = os.path.exists(image_dest)
  if exists:
    print("file already exists")
    return image_dest

  resp = requests.get(url)
  with open(image_dest, "wb") as file:
    file.write(resp.content)
  
  return image_dest


# MAIN PROGRAM LOOP - repeats the check and download every 10 seconds to monitor 24/7
while True:
  try:
    url = get_image_URL()
    file_dest = download_image(url)
    print(f"Image successfully downloaded: {file_dest}")
  except Exception as e:
    print("Something went wrong:", e)
  time.sleep(10)
