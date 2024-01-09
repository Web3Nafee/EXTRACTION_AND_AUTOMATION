import pyautogui as py
import time

time.sleep(5)
py.position()
py.moveTo(x=1250, y=17, duration=1)
py.click()

py.moveTo(x=32, y=334, duration=2)
py.doubleClick()
time.sleep(20)
py.moveTo(x=1134, y=18, duration=2) 
py.click()
time.sleep(1)

# Above is for opening the program  


py.moveTo(x=260, y=552, duration=1) # open barbel
py.click()
time.sleep(1)
py.moveTo(x=1253, y=580, duration=1)
py.click()
py.moveTo(x=93, y=267, duration=1) # selecting document 
py.click()
time.sleep(1)

py.moveTo(x=235, y=330, duration=1) 
py.doubleClick()
py.moveTo(x=220, y=185, duration=1) 
py.doubleClick()

py.moveTo(x=228, y=183, duration=1) #click on the first compound
py.click()
py.moveTo(x=506, y=491, duration=1) #select the first compound
py.click()

#select the other compound
for x in range(2):
    time.sleep(1)
    py.moveTo(x=1253, y=580, duration=1)
    py.click()
    time.sleep(1)

    py.moveTo(x=250, y=309, duration=1) 
    py.click()
    py.press('down', presses=x+1)
    py.click()
    py.moveTo(x=506, y=491, duration=1) 
    py.click()