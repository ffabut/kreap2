from selenium import webdriver
import time


#CHROME
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #vytvorime okno prohlizece, instalaci driveru resi webdriver_manager

#FIREFOX:
#from selenium.webdriver.firefox.service import Service
#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

#EDGE:
#from selenium.webdriver.edge.service import Service
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
#driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))


driver.get("https://www.idnes.cz")
time.sleep(1)

current_url = driver.current_url
title = driver.title
print(f"We are on URL '{current_url}' and title of this page is: {title}.")

driver.get("https://www.favu.vut.cz")
time.sleep(1)

current_url = driver.current_url
title = driver.title

print(f"We are on URL '{current_url}' and title of this page is: {title}.")


driver.close()