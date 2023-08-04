import pyautogui as pag
import time as t
import keyboard as clav
import random as rd
import win32api, win32con

from btnManager import *

def intervalCheckIfOnScreen(btnName, sleepMin = 0.001, sleepMax = 1, maxChecks = 5):
    print("currently checking if " + btnName + " is on screen \n")
    result = None
    check = 0
    while result == None and check < maxChecks:
        result = pag.locateOnScreen(btnName)
        t.sleep(rd.uniform(sleepMin, sleepMax))
        check+=1
    print("found " + str(result))
    return result

# 0 : None
# 1 : phrase à trous
# 2 : QCM
# 3 : mots à mettre dans l'ordre
# 4 : vrai ou faux

def getQuestionType():
    type = 0
    if not intervalCheckIfOnScreen("btns/completeSentence.PNG", sleepMax=0.3) == None:
        type = 1
    elif not intervalCheckIfOnScreen("btns/answerQuestion.PNG", sleepMax=0.3) == None:
        type = 2
    elif not intervalCheckIfOnScreen("btns/orderWords.PNG", sleepMax=0.3) == None:
        type = 3
    elif not intervalCheckIfOnScreen("btns/trueFalse.PNG", sleepMax=0.3) == None:
        type = 4
    return type

def answerHoledSentenceFancy(maxItemID = 6):
    found = None
    checkedID = maxItemID
    while found == None and checkedID > 0:
        checkedBtn = "order" + str(checkedID) + ".PNG"
        found = intervalCheckIfOnScreen("btns/" + checkedBtn, sleepMax=0.1, maxChecks=3)
        checkedID = checkedID - 1
        if clav.is_pressed("o + f"):
            break
    print(checkedID)

def answerHoledSentenceFast():
    y = 965
    x = 470
    btn = None
    while btn == None:
        click(x, y)
        t.sleep(0.1)
        btn = randClickOn("btns/continuer.PNG", checkCountermax=2)
        x = x + 20
        if clav.is_pressed("o + f"):
            break

def answerQuestionFancy():
    randClickOn("btns/boxCorner.PNG")

def answerQuestionFast():
    x = 980
    y = 857
    btn = None
    while btn == None:
        click(x, y)
        t.sleep(0.1)
        btn = randClickOn("btns/continuer.PNG", checkCountermax=2)
        y = y + 20
        if clav.is_pressed("o + f"):
            break

def orderWordsFast():
    y = 660
    x = 200
    btn = None
    while btn == None:
        click(x, y)
        t.sleep(0.1)
        btn = randClickOn("btns/continuer.PNG", checkCountermax=2)
        x = x + 40
        if clav.is_pressed("o + f"):
            break

def answerTrueFalse(rep):
    if rep == 1:
        btnName = "btns/False.PNG"
    elif rep == 2:
        btnName = "btns/True.PNG"
    randClickOn(btnName)
    randClickOn("btns/continuer.PNG")