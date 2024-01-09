#importing the libraries 
# converting the sdf to pdb using discovery studio   
import pyautogui as py
import time

time.sleep(5)
py.position()
py.moveTo(x=1250, y=17, duration=1)
py.click()
py.moveTo(x=127, y=206, duration=1)
py.doubleClick()
time.sleep(10)

 # picking the compound

py.moveTo(x=15, y=38, duration=1)
py.click()
py.moveTo(x=34, y=78, duration=1)
py.click()
py.moveTo(x=113, y=248, duration=1)
py.click()
py.moveTo(x=240, y=290, duration=1)
py.doubleClick()
py.moveTo(x=264, y=164, duration=1) 
py.doubleClick()

   #saving the first compound
py.moveTo(x=237, y=169, duration=1) #click on the first compound
py.click()
py.moveTo(x=507, y=469, duration=1)
py.click()
py.moveTo(x=15, y=33, duration=1)
py.click()
py.moveTo(x=69, y=204, duration=1)
py.click()
time.sleep(1)

py.moveTo(x=104, y=216, duration=1)
py.click()
py.moveTo(x=280, y=424, duration=1)
py.click()
py.moveTo(x=244, y=504, duration=1)
py.click()
py.moveTo(x=506, y=467, duration=1)
py.click()


#SAVING THE REST AS PDB
for i in range (3):
    py.moveTo(x=15, y=38, duration=1)
    py.click()
    py.moveTo(x=34, y=78, duration=1)
    py.click()
    py.moveTo(x=244, y=169, duration=1)
    py.click()
    py.press('down', presses=i+1)
    py.moveTo(x=507, y=469, duration=1)
    py.click()
    py.moveTo(x=15, y=33, duration=1)
    py.click()
    py.moveTo(x=69, y=204, duration=1)
    py.click()
    py.moveTo(x=104, y=216, duration=1)
    py.click()
    py.moveTo(x=280, y=424, duration=1)
    py.click()
    py.moveTo(x=244, y=504, duration=1)
    py.click()
    py.moveTo(x=506, y=467, duration=1)
    py.click()






