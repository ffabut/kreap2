"""
Program na vyhledani Fakulty Výtvarných Umění Brno na Google a presunuti na stranku fakulty.
Slo by pouzit pro boostovani Google search rankingu fakulty, anebo pro ovlivnovani toho, jak Google vnima nasi personu - mega fan FaVU.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#CHROME
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


option = webdriver.ChromeOptions()
option.add_argument("window-size=1412,900")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')

#Open Browser
driver_path = ChromeDriverManager().install()
print("driver installed at", driver_path)
driver = webdriver.Chrome(service=Service(driver_path), options=option)


# SOUHLAS s cookies a licencni smlouvou Google
driver.get("https://google.com")
time.sleep(1)
driver.find_element(By.ID, "L2AGLb").click()


def google_to_favu():
  driver.get("https://google.com")

  time.sleep(1)
  search_input = driver.find_element(By.ID, "APjFqb")
  time.sleep(1)
  search_input.send_keys("Fakulta výtvarných umění Brno")
  search_input.send_keys(Keys.RETURN)
  time.sleep(5)

  links = driver.find_elements(By.TAG_NAME, "a")
  for link_element in links:
    src = link_element.get_attribute("href")
    if src is None:
      continue
    #if "favu.vut.cz" in src:
    #link_element.is_enabled()
    if link_element.is_displayed():
      link_element.click()
      time.sleep(2)
      driver.back()
      time.sleep(1)

  time.sleep(5)


while True:
  google_to_favu()
  # favu_teacher_search() - tady by mohly byt jine funkce, ktere se budou opakovat


driver.close()
