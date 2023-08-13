import pyautogui as pag
import time as t
import random as rd

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
    if questionType == 5:
        answerQuestionButton("order1")
    if questionType == 6:
        answerQuestionButton("order2")
    if questionType == 7:
        answerQuestionButton("order3")
    if questionType == 8:
        answerQuestionButton("test")
                       
def main():
    """Utility function to get screen resolution"""

    mouse = MouseController()
# 1799, 1169
    while True:
        mouse.position = (830, 600)
        mouse.click(Button.left)
        t.sleep(0.1)
        # mouse.position = (979, 724)
t.sleep(2)
# main()
# 1799, 1169
autoLesson()