import time
import os
import pyautogui as pag
import PySimpleGUI as sg
import cv2
import numpy as np
from PIL import ImageGrab
groupicogray = cv2.cvtColor(cv2.imread(os.path.dirname(os.path.realpath(__file__)) + '\groupico.JPG'), cv2.COLOR_BGR2GRAY)
leavegroupgray = cv2.cvtColor(cv2.imread(os.path.dirname(os.path.realpath(__file__)) + '\leavegroup.JPG'), cv2.COLOR_BGR2GRAY)
inputs = sg.Window("Discord group leaver", layout=[[sg.Text("How many groups do you want to leave? (Make sure discord is open and all groups are visible)")],[sg.Input("")],[sg.Button('Perform action'), sg.Button('Cancel')]], margins=(100,50)).read()
if str(inputs[0]) == "Cancel":
    quit()
cycles = int(inputs[1][0])

for i in range(0, cycles):
    time.sleep(0.3)
    screen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1380))), cv2.COLOR_BGR2RGB)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, groupicogray, cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    xpos,ypos = mnLoc
    pag.click((xpos + 100), (ypos + 22))
    pag.click((xpos + 250), (ypos + 22))
    time.sleep(0.2)
    screen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1380))), cv2.COLOR_BGR2RGB)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, leavegroupgray, cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    xpos,ypos = mnLoc
    pag.click((xpos+100), (ypos+20))




#Debugging
#trows,tcols = groupicogray.shape[:2]
#final = cv2.rectangle(screen, (xpos, ypos), (xpos+tcols,ypos+trows),(0,0,255),2)
#cv2.imwrite("final.JPG", final)
#cv2.imshow('img', final)
#cv2.waitKey(0)
