import pyautogui, time

time.sleep(10) #otevrete malovací program, zvolte stetec, dejte nekam do prostred platna
# zvolte cervenou barvu for kvicala efect

pyautogui.click(button="left")

distance = 600

while distance > 0:
  pyautogui.dragRel(distance, 0, duration=0.1, button='left')   # doprava 
  distance = distance - 5
  pyautogui.dragRel(0, distance, duration=0.1, button='left')   # dolu
  pyautogui.dragRel(-distance, 0, duration=0.1, button='left')  # doleva
  distance = distance - 5
  pyautogui.dragRel(0, -distance, duration=0.1, button='left')  # nahoru

