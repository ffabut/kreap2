import pyautogui, time

time.sleep(10) #prosim, manualne otevrete textovy editor, nebo najedte nekam, kam se da vkladat text

pyautogui.click() #program klikne

pyautogui.typewrite('Hello world!') #a vepise text

pyautogui.hotkey('ctrl', 's') #klavesove zkratky muzeme volat pomoci funkce hotkey()
#pokusime se o ulozeni a dal je to na nas...
