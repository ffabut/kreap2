from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

driver.get("https://seznam.cz")

wait = WebDriverWait(driver, timeout=30)
element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
print("ELEMENT BY TAG NAME:", element)


element = wait.until(EC.presence_of_element_located((By.ID, "non-existing-id"))) #zde si pockame... az nakonec bude error - element na strance neexistuje
print("ELEMENT BY ID:", element)

driver.close()
