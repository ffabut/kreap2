from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

opts = Options()

browser = Firefox(options=opts)
browser.get('https://google.com')
time.sleep(2)

# prvky muzeme vyhledavat podle ID
#search_form = browser.find_element_by_id('search_form_input_homepage')

#take podle tridy - class
#search_form = browser.find_element_by_class_name("some class")

#A PODLE MNOHA DALSICH JAKO: by_link_text, by_partial_link_text, atd...

# prakticke je hledat podle xpath:
search_form = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/span/div/div/div[3]/button[2]/div")
search_form.click()
time.sleep(2)

search_form = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

search_form.send_keys('motorkarske obleceni')
time.sleep(2)

search_form.submit()

time.sleep(20)
browser.close()
