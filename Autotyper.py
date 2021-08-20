import pyautogui
import time

time.sleep(6);

text = "Lorem ipsum dolor sit"

pyautogui.PAUSE = 0.001

charList = [ i for i in text ]

for char in charList:
    pyautogui.typewrite(char)
    pyautogui.typewrite(['enter'])
