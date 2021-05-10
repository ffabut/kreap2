import pyautogui

# PAUSE = x nastavi, ze po kazdem prikazu pyautogui pocka x sekund
# dobre na debugging, je videt, co se deje a taky se to da lehceji ukoncit
pyautogui.PAUSE = 1

# FAILSAFE=True nastavi, ze v pripade nutnosti bude program ukoncem,
# pokud mys hodne rychle presuneme do leveho horniho rohu
pyautogui.FAILSAFE = True

# muzeme zjistit vysku a sirku obrazovky
width, height = pyautogui.size() # muzeme pak definovat mista kam klikame pomoci procent
#aby byl skript prenositelny i na jinak velke obrazovky
print(width, height)

for i in range(0): #mysi hybeme funkce moveTo, prvni parametr je x-sirka, druhy y-vyska, 
      pyautogui.moveTo(100, 100, duration=1) #parametr duration urcuje, jak ryhle se mys bude pohybovat
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
      pyautogui.moveTo(0.5*width, 0.5*height) #polovina sirky, polovina vysky = stred obrazovky
      #nejvice prenositelne napric ruzne velkymi monitory

#dostupna je i funkce moveRel (ta urcuje pohyb relativne k aktualni pozici mysi)
pyautogui.moveTo(0, 200, duration=5) #o dveste dolu, zaciname, ale kde se aktualne nachazela mys

# muzeme ziskat pozici mysi
x, y = pyautogui.position()
print(x, y)


#kliknuti mysi, parametr button urcuje, jake tlacitko klika
pyautogui.click(200, 200, button='left', duration=1)

#muzeme ovladat take tah mysi
pyautogui.drag(200, 0, duration=4)

#stejne tak existuje dragRel
pyautogui.drag(-100, 100, duration=4)

