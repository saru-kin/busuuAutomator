import pyautogui as pag
import time as t
import random as rd
from pynput.mouse import Button, Controller

from math import *

def rescale(x, y):
    x = (x * 1800) / 3024
    y = (y * 1170) / 1964
    return x, y

def click(x, y):
    x, y = rescale(x, y)
    mouse = Controller()
    # mouse.move(x,y)
    mouse.position = (x + 40, y + 40)
    t.sleep(0.1)
    mouse.click(Button.left)
    mouse.position = (x, y)
    t.sleep(0.1)
    mouse.click(Button.left)
    mouse.position = (x + 40, y + 40)
    t.sleep(0.1)
    mouse.press(Button.left)
    t.sleep(0.3)
    mouse.release(Button.left)
    mouse.position = (x, y)
    t.sleep(0.1)
    mouse.press(Button.left)
    t.sleep(0.3)
    mouse.release(Button.left)
    # mouse.position = (y, x)
    # mouse.click(Button.left)
    
def randClickOn(btnName, conf=0.8, sleepTime=0, checkCountermax = 5, verticalOffset = 5, horizontalOffset = 5, Vrestrain = 0, Hrestrain = 0):
    if sleepTime == 0:
        sleepTime = rd.uniform(0, 0.2)
    checkCounter = 0
    btn = None
    while btn == None and checkCounter < checkCountermax:
        btn = pag.locateOnScreen(btnName, confidence=conf, grayscale=True )
        checkCounter = checkCounter + 1
        t.sleep(sleepTime)
    if not btn == None:
        print("button found")
        randClickIn(btn.left, btn.top, btn.width - Hrestrain, btn.height - Vrestrain, sleepTime)
    return btn

def randClickIn(left, top, width, height, sleepTime=0):
    if sleepTime == 0:
        sleepTime = rd.uniform(0, 0.2)
    executionReport = "chill"
    x = left
    y = top
    t.sleep(sleepTime)
    click(x, y)
    return executionReport

def checkAndClickFacultativeBtn(btnName, conf=0.8,checkMax = 10):
    actuallyClicked = False
    checkCount = 0
    btn = None
    while btn == None or checkCount<checkMax:
        btn = pag.locateOnScreen(btnName, confidence=conf, grayscale=True)
        checkCount = checkCount + 1
    if not btn == None:
        randClickIn(btn.left, btn.top, btn.width, btn.height)
        actuallyClicked = True
    return actuallyClicked

def keepOnClicking(btnName, confidence = 0.8, consecutiveChecks = 5, sleepMin = 0.001, sleepMax = 1):
    stopTime = rd.uniform(sleepMin, sleepMax)
    goOn = randClickOn(btnName)
    if not goOn == None:
        print("clicked on " + btnName + "\n")
        while not goOn == None:
            t.sleep(rd.uniform(0.1, 0.8))
            goOn = randClickOn(btnName, conf = confidence, sleepTime=stopTime, checkCountermax=consecutiveChecks)
            if not goOn == None:
                print("clicked on " + btnName + "\n")