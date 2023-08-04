import pyautogui as pag
import time as t
import keyboard as clav
import random as rd
import win32api, win32con

from btnManager import *
from autoAnswerer import *

def autoLesson():
    print("automating a lesson")
    questionType = getQuestionType()
    if questionType == 0:
        print("Type de question non identifié \n")
    if questionType == 1:
        print("completion d'une phrase à trous \n")
        answerHoledSentenceFast()
    if questionType == 2:
        print("Réponse à une question QCM")
        answerQuestionFast()
    if questionType == 3:
        print("je met les mots dans l'ordre")
        orderWordsFast()
    if questionType == 4:
        rep = rd.randint(1, 2)
        answerTrueFalse(rep)
            

t.sleep(2)
autoLesson()