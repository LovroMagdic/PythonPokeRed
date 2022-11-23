from PIL import Image
from PIL import ImageGrab
import time
import os
import pyautogui
import numpy as np
import sys
from numpy import asarray
from numpy import savetxt

f = open("screen.csv", "r")
R = 0
G = 0
B = 0
i=0
for each in f:
    tmp = each.split(",")
    for i in range(0, 99, 3):
        R += int(tmp[i])
        G += int(tmp[i+1])
        B += int(tmp[i+2])
R = R / 1089
G = G / 1089
B = B / 1089
print("RED : %d, GREEN : %d, BLUE : %d" % (R, G, B))
f.close()

#idealna je 213
#za screen-left RED : 189, GREEN : 238, BLUE : 215 -- 214
#za screen-up RED : 160, GREEN : 209, BLUE : 181 --183
#za screen-right RED : 134, GREEN : 167, BLUE : 164 -- 155
#za screen-down RED : 160, GREEN : 170, BLUE : 151 -- 160