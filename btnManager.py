import pyautogui as pag
import time as t
import keyboard as clav
import random as rd
import win32api, win32con

from math import *


def click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    t.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def randClickOn(btnName, conf=0.8, sleepTime=0, checkCountermax = 5, verticalOffset = 0, horizontalOffset = 0, Vrestrain = 0, Hrestrain = 0):
    if sleepTime == 0:
        sleepTime = rd.uniform(0, 0.2)
    checkCounter = 0
    btn = None
    while btn == None and checkCounter < checkCountermax:
        btn = pag.locateOnScreen(btnName, confidence=conf, grayscale=True )
        checkCounter = checkCounter + 1
        t.sleep(sleepTime)
    if not btn == None:
        randClickIn(btn.left + horizontalOffset, btn.top + verticalOffset, btn.width - Hrestrain, btn.height - Vrestrain, sleepTime)
    return btn

def randClickIn(left, top, width, height, sleepTime=0):
    if sleepTime == 0:
        sleepTime = rd.uniform(0, 0.2)
    executionReport = "chill"
    x = left + floor(rd.uniform(1, width))
    y = top + floor(rd.uniform(1, height))
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