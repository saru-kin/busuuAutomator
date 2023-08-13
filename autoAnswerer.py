import pyautogui as pag
import time as t
import random as rd
from pynput.mouse import Controller as MouseController

from btnManager import *

def intervalCheckIfOnScreen(btnName, sleepMin = 0.001, sleepMax = 1, maxChecks = 5):
    print("currently checking if " + btnName + " is on screen \n")
    result = None
    check = 0
    while result == None and check < maxChecks:
        result = pag.locateOnScreen(btnName)
        print(result)
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
    elif not intervalCheckIfOnScreen("btns/order1.PNG", sleepMax=0.3) == None:
        type = 5
    elif not intervalCheckIfOnScreen("btns/order2.PNG", sleepMax=0.3) == None:
        type = 6
    elif not intervalCheckIfOnScreen("btns/order3.PNG", sleepMax=0.3) == None:
        type = 7
    elif not intervalCheckIfOnScreen("btns/test.PNG", sleepMax=0.3) == None:
        type = 8
    return type

def answerHoledSentenceFancy(maxItemID = 6):
    found = None
    checkedID = maxItemID
    count = 0
    while found == None and count < 50 and checkedID > 0:
        checkedBtn = "order" + str(checkedID) + ".PNG"
        found = intervalCheckIfOnScreen("btns/" + checkedBtn, sleepMax=0.1, maxChecks=3)
        checkedID = checkedID - 1
    print(checkedID)

def answerHoledSentenceFast():
    y = 965
    x = 470
    btn = None
    count = 0
    while btn == None and count < 50:
        click(x, y)
        t.sleep(0.1)
        btn = randClickOn("btns/continuer.PNG", checkCountermax=2)
        x = x + 20

def answerQuestionFancy():
    randClickOn("btns/boxCorner.PNG")

def answerQuestionButton(btn):
    print("yo")
    randClickOn(f"btns/{btn}.PNG")

def answerQuestionFast():
    x = 980
    y = 857
    count = 0
    while btn == None and count < 50:
        click(x, y)
        t.sleep(0.1)
        btn = randClickOn("btns/continuer.PNG", checkCountermax=2)
        y = y + 20

def orderWordsFast():
    y = 660
    x = 200
    btn = None
    count = 0
    while btn == None and count < 50:
        click(x, y)
        t.sleep(0.1)
        btn = randClickOn("btns/continuer.PNG", checkCountermax=2)
        x = x + 40

def answerTrueFalse(rep):
    if rep == 1:
        btnName = "btns/False.PNG"
    elif rep == 2:
        btnName = "btns/True.PNG"
    randClickOn(btnName)
    randClickOn("btns/continuer.PNG")