from selenium import webdriver #ridi vytvoreni okna, ustredni modul
import time #pro sleep


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


driver.get("https://www.artalk.cz") #nacteme URL
time.sleep(1) #spanek pro lepsi citelnost procesu (ci maskovani se za realneho cloveka)

elem = driver.find_element(by="id", value="search-text") #vyhledame element podle ID, kterou ma search field na artalku nastaveny na "search-text"

elem.send_keys("Miloš Zeman") #do elementu posleme text - jako by uzivatel*ka skutecne psal*a
time.sleep(1) 
elem.send_keys("\n") #posilame enter pro odeslani hledani

time.sleep(10) #zde cekame, abychom si mohly*i prohlednout vysledky
driver.close()
