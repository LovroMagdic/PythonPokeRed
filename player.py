from PIL import Image
from PIL import ImageGrab
import time
import os
import pyautogui
import numpy as np
import sys
from numpy import asarray
from numpy import savetxt
import pyautogui

time.sleep(5)
dictImage = {
    "left": 214,
    "up":183,
    "right":155,
    "down": 160
}

res = 0
for key in dictImage:
    tmp = abs(dictImage[key] - 215)
    dictImage[key] = tmp

decision = min(dictImage, key=dictImage.get)
pyautogui.click(x=100, y=200)
if decision == "left":
    pyautogui.click(x=55, y=563)
    pyautogui.click(x=55, y=563)
elif decision == "up":
    pyautogui.click(x=74, y=538)
    pyautogui.click(x=74, y=538)
elif decision == "right":
    pyautogui.click(x=89, y=561)
    pyautogui.click(x=74, y=561)
elif decision == "down":
    pyautogui.click(x=74, y=587)
    pyautogui.click(x=74, y=587)

'''
Point(x=55, y=563)
Point(x=74, y=538)
Point(x=89, y=561)
Point(x=74, y=587)

positions of virtual pads arrow keys
'''