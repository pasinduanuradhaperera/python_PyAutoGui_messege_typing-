# pyautogui library

import pyautogui as gui
import time
print("started you have 10 seconds to navigate") 
for i in range(10):
    print(i)
    time.sleep(1)
num = 1000
for i in range(num):
    gui.write("huuuuuuu")
    gui.press("enter")
    print(num - i, "to print")
