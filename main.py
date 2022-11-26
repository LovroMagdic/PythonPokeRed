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
from random import *


'''
Point(x=193, y=175) gornji lijevi
Point(x=287, y=174) gornji desni
Point(x=293, y=273) donji desni
Point(x=199, y=273) donji lijevi
'''
last_decision = ""
direction_array = []
csv_array = []
arr = []

#box_size 90x90
left,upper,right,lower = 193.5,174.5,286.5,266.5
d = 31

class my_dictionary(dict):
 
  # __init__ function
  def __init__(self):
    self = dict()
  # Function to add key:value
  def add(self, key, value):
    self[key] = value

def get4points():
    time.sleep(3)
    print(pyautogui.position())
    time.sleep(3)
    print(pyautogui.position())
    time.sleep(3)
    print(pyautogui.position())
    time.sleep(3)
    print(pyautogui.position())

def getScreen():
    for i in range(60):
        screenshot = ImageGrab.grab(bbox=(left,upper,right,lower)) #left,upper,right,lower
        name = "screen" + ".jpg"
        os.chdir(r"C:\Users\Lovro\Desktop\PythonPokeRed\recordings")
        screenshot.save(name, 'PNG')
        return(name)

def direction(source):
    #polje 1
    img = Image.open(source)
    box = (d*0, d, d, d*2)
    img2 = img.crop(box)
    string = source.replace(".jpg", "-left.jpg")
    direction_array.append(string)
    img2 = img2.save(string)

    #polje2
    img = Image.open(source)
    box = (d, d*0, d*2, d)
    img2 = img.crop(box)
    string = source.replace(".jpg", "-up.jpg")
    direction_array.append(string)
    img2 = img2.save(string)

    #polje3
    img = Image.open(source)
    box = (d*2, d, d*3, d*2)
    img2 = img.crop(box)
    string = source.replace(".jpg", "-right.jpg")
    direction_array.append(string)
    img2 = img2.save(string)

    #polje4
    img = Image.open(source)
    box = (d, d*2, d*2, d*3)
    img2 = img.crop(box)
    string = source.replace(".jpg", "-down.jpg")
    direction_array.append(string)
    img2 = img2.save(string)

def getCsv():
    for each in direction_array:
        image = Image.open(each)
        # convert image to numpy array
        data = asarray(image)
        data_reshaped = data.reshape(data.shape[0], -1)
        name = each.replace(".jpg", ".csv")
        savetxt(name, data_reshaped, fmt='%d', delimiter=',')
        csv_array.append(name)

def decide(dictImage):
    for key in dictImage:
        tmp = (10 - (dictImage[key] % 10) ) + dictImage[key]
        dictImage[key] = tmp

    decide = min(dictImage, key=dictImage.get)
    arr.append(decide)
    save = [decide, dictImage[decide]]
    del dictImage[decide]

    decide = min(dictImage, key=dictImage.get)
    arr.append(decide)

    dictImage[save[0]] = save[1]

    if dictImage[arr[0]] == dictImage[arr[1]]:
        rem = randint(0, 1)
        arr.remove(arr[rem])
    return arr[0]

def last_decide(dictImage, last_decision):
    temp = 0
    for key in dictImage:
        temp = temp + dictImage[key]
    temp = temp / 4

    if dictImage[last_decision] > temp:
        choice = decide(dictImage)
        return choice
    else:
        return last_decision

#main
while True:
    screen = getScreen()
    direction(screen)
    getCsv()
    dictImage = my_dictionary()

    for each in csv_array:
        f = open(each)
        R, G, B, i = 0, 0, 0, 0
        for line in f:
            tmp = line.split(",")
            for i in range(0, 90, 3):
                R += int(tmp[i])
                G += int(tmp[i+1])
                B += int(tmp[i+2])
        R = R / 961
        G = G / 961
        B = B / 961
        #print("RED : %d, GREEN : %d, BLUE : %d" % (R, G, B))
        pixel_value = int((R+G+B)/3)
        #print("%d" % (pixel_value))
        dictImage.add(each, pixel_value)
        f.close()

    #idealna je 213
    res = 0
    # print(dictImage)1
    for key in dictImage:
        tmp = abs(213 - dictImage[key])
        dictImage[key] = tmp
    print(dictImage)
    if last_decision == "":
        decision = decide(dictImage)
    else:
        decision = last_decide(dictImage, last_decision)
    last_decision = decision
    arr = []
    print(decision)
    if decision == "screen-left.csv":
        pyautogui.click(x=55, y=563)
        time.sleep(0.2)
        # pyautogui.click(x=55, y=563)
    elif decision == "screen-up.csv":
        pyautogui.click(x=74, y=538)
        time.sleep(0.2)
        # pyautogui.click(x=74, y=538)
    elif decision == "screen-right.csv":
        pyautogui.click(x=89, y=561)
        time.sleep(0.2)
        # pyautogui.click(x=89, y=561)
    elif decision == "screen-down.csv":
        pyautogui.click(x=74, y=587)
        time.sleep(0.2)
        # pyautogui.click(x=74, y=587)
    time.sleep(0.1)

