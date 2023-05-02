from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pygetwindow
from datetime import datetime
import cv2 
import easyocr
import pyscreenshot as ImageGrab
import numpy as np


def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.21)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print(current_time," Click.")
    time.sleep(1.5)
def clickMiddleOfWindow():
    return

def keyboard_press(keystroke):
    pyautogui.press(keystroke)
    time.sleep(1.5)

def detectElement(element):
    finding =  pyautogui.locateOnScreen(element, confidence=0.8)
    if finding != None:
        return finding
    else:
        return False

def goToCity():
    city_button = detectElement("city_button.png")
    time.sleep(1.5)
    if city_button != False:
        print(current_time," city button found")
        click(city_button.left, city_button.top)
    time.sleep(1.5)
def onMap():
    city_button = detectElement("city_button.png")
    if city_button != False:
        return True
    else:
        return False
#STATIC PARAMS

ranking_type = "HELP"
# Parameters Definition 

try:
    window = pygetwindow.getWindowsWithTitle("Call of Dragons")[0]
    window.activate()
    
    midx,midy = window.left+window.width/2,window.top+window.height/2 #Calculate the mid of the window because many things are located in the center. 
   

except:
    print(current_time," /!\\ Please open the game first.")
    exit()
left,top = window.topleft
right,bottom = window.bottomright


if not onMap():
    keyboard_press("space") #once into city, go into space mode by pressing space

keyboard_press("o") #Into space mode, press O To enter Alliance menu


print("Loading Model")
reader = easyocr.Reader(['ch_sim','en'], gpu = True)
file = open("reporting.txt","w") 

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
keyboard_press("o")
alliance_params_button = detectElement("alliance_params.png")
if(alliance_params_button != False):
    time.sleep(0.21)
    print(current_time," Members icon found")
    click(alliance_params_button.left+60, alliance_params_button.top+20)
else:
    print(current_time," Members icon not found")

ranking_button = detectElement("ranking.png")
if(ranking_button != False):
    time.sleep(0.21)
    print(current_time," Members icon found")
    click(ranking_button.left+10, ranking_button.top+10)

    match ranking_type:
        case "BUILDING":
            ranking_building = detectElement("ranking_building.png")
            if(ranking_building != False):
                time.sleep(0.21)
                print(current_time," Members icon found")
                click(ranking_building.left+10, ranking_building.top+10)
            else:
                print("can't find "+ ranking_type)
                exit()
        case "HELP":
            ranking_help = detectElement("ranking_help.png")
            if(ranking_help != False):
                time.sleep(0.21)
                print(current_time," Members icon found")
                click(ranking_help.left+10, ranking_help.top+10)
            else:
                print("can't find "+ ranking_type)
                exit()


    #Click in the middle 
    while keyboard.is_pressed('q') == False: #the main loop (press q to pause the bot)
        click(int(midx+100),int(midy+100))
        print("Grabbing Window")
        im = ImageGrab.grab(bbox=(int(np.abs(window.left+window.width*0.42)), int(np.abs(window.top+window.height*0.50)), int(np.abs(window.right)), int(np.abs(window.bottom))))  # X1,Y1,X2,Y2
        im.save("window1.jpg")
        result = reader.readtext('window1.jpg')
        i = 0
        for r in result:
            print(r[1])
            try:
                file.write(r[1])
            except: 
                file.write("unknown_value")
            i+=1
            if(i >=2):
                i=0
                file.write("\n")
            else:
                file.write(",")
        j=0
        for j in range (0,7):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, int(midx+100), int(midy+100), -7, 0)
        

    else:
        print(current_time," Members icon not found")

    file.close()

"""                
    case "VILLAGE_EXPLORE":
        goToCity()
        time.sleep(4)
        scout_building = detectElement("scout_building.png")
        if scout_building != False:
            time.sleep(0.21)
            click(scout_building.left,scout_building.top)
        else:
            print(current_time," could not find the scout building")
            exit()

        village_icon = detectElement("village.png")
        if village_icon != False:
            click(village_icon.left,village.icon.top)
        else:
            print(current_time," could not find the village tab")
            exit()
        explore = detectElement("explore.png")
        if explore != False:
            click(explore.left,explore.top)
        else:
            print(current_time," could not find explore button")
            exit()
        exclamation = detectElement("exclamation.png")
        if exclamation != False:
            click(exclamation.left,exclamation.top+50) # we need to hit under the exclamation point as the target is under it.
        else:
            print(current_time," couldn't find the exclamation mark")
            exit();
        explore = detectElement("explore.png")
        if explore != False:
            click(explore.left,explore.top)
        else:
            print(current_time," could not find the second explore button")
            exit()

        #NOW WE NEED TO KNOW IN WHICH CASE WE ARE (Trade, gift, story..)

        #Then, ALLER.PNG -> Exclamation.. 

       # while keyboard.is_pressed('q') == False:
"""