from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pygetwindow


def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.21)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")


def detectElement(element):
    finding =  pyautogui.locateOnScreen(element, confidence=0.8)
    if finding != None:
        return finding
    else:
        return False
#Find the window
window = pygetwindow.getWindowsWithTitle("Call of Dragons")[0]
left,top = window.topleft
right,bottom = window.bottomright

def relaunchScout(idle_scout):
    click(idle_scout.left,idle_scout.top)
    time.sleep(0.21)
    scout_zone = False
    while scout_zone == False:
        print("not finding it, ")
        print(scout_zone)
        scout_zone = detectElement("scout_zone.png")
        time.sleep(0.21)

    if scout_zone != False:
        click(scout_zone.left, scout_zone.top)
        scout_zone=True

    explore = False
    while explore == False:
        explore = detectElement("explore.png")

    if explore != False:
        click(explore.left,explore.top)
        explore=True
        return True

    return True

def goToCity():
    city_button = detectElement("city_button.png")
    time.sleep(5)
    if city_button != False:
        print("city button found")
        click(city_button.left, city_button.top)



#initialize and see what is the state (idle scouts on the map or in their basement.)
mission="MAP_EXPLORE"


goToCity()
time.sleep(4)

while keyboard.is_pressed('q') == False: #the main loop (press q to pause the bot)

    idle_scout = detectElement("idle_scout.png")
    if(idle_scout != False):
        time.sleep(0.21)
        print("Found an idle scout. Relaunching it")
        relaunchScout(idle_scout)
        time.sleep(5.00)
    else:
        print("I dont see it")
"""                
    case "VILLAGE_EXPLORE":
        goToCity()
        time.sleep(4)
        scout_building = detectElement("scout_building.png")
        if scout_building != False:
            time.sleep(0.21)
            click(scout_building.left,scout_building.top)
        else:
            print("could not find the scout building")
            exit()

        village_icon = detectElement("village.png")
        if village_icon != False:
            click(village_icon.left,village.icon.top)
        else:
            print("could not find the village tab")
            exit()
        explore = detectElement("explore.png")
        if explore != False:
            click(explore.left,explore.top)
        else:
            print("could not find explore button")
            exit()
        exclamation = detectElement("exclamation.png")
        if exclamation != False:
            click(exclamation.left,exclamation.top+50) # we need to hit under the exclamation point as the target is under it.
        else:
            print("couldn't find the exclamation mark")
            exit();
        explore = detectElement("explore.png")
        if explore != False:
            click(explore.left,explore.top)
        else:
            print("could not find the second explore button")
            exit()

        #NOW WE NEED TO KNOW IN WHICH CASE WE ARE (Trade, gift, story..)

        #Then, ALLER.PNG -> Exclamation.. 

       # while keyboard.is_pressed('q') == False:
"""