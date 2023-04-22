from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pygetwindow
from datetime import datetime


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

GOLD = "search_GOLD.png"
MANA = "search_MANA.png"
IRON = "search_IRON.png"
WOOD = "search_WOOD.png"
DARKLINGS = "search_darklings.png"
GATHER = "gather.png"
CREATE_LEGIONS = "create_legions.png"
MARCH = "march.png"

# Parameters Definition 

MAX_LEGIONS = 5 # The maximum number of legions you have. (Can't yet be a subset of you maximum legions.)
DESIRED_RESOURCE = MANA # The resource you want to collect. Can be one of: ("MANA", "GOLD", "WOOD", "IRON")

FULL = "FULL_"+str(MAX_LEGIONS)+".png"

EXPONENTIAL_BACKOFF = 1
#Find the window
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

keyboard_press("f") #Into space mode, press F, not to pay respect but to enter search mode.


while keyboard.is_pressed('q') == False: #the main loop (press q to pause the bot)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    keyboard_press("f")
    search_darklings = detectElement(DARKLINGS)
    if(search_darklings != False):
        time.sleep(0.21)
        print(current_time," Darklings search icon is not selected, selecting it.")
        click(search_darklings.left, search_darklings.top)
    else:
        print(current_time," Darklings search icon is selected, proceed...")
        print(current_time," User has selected resource: "+DESIRED_RESOURCE)
        resource_search = detectElement(DESIRED_RESOURCE)

        if resource_search != False: 
            print(current_time," Desired resource found")
            click(resource_search.left, resource_search.top)
        else:
            print(current_time," can't find desired resource")

        search_button = detectElement("search_button.png")
        if search_button != False:
            print(current_time," Search Button found")
            click(search_button.left+20, search_button.top+15)
        else:
            print(current_time," no search button found.")
        marker = detectElement("marker.png")
        time.sleep(2)
        click(int(midx),int(midy))

        gather_button = detectElement(GATHER)
        if gather_button != False:
            print(current_time," Gather Button found")
            click(gather_button.left+25,gather_button.top+15)
        else:
            print(current_time," no gather button")
        create_legions = detectElement(CREATE_LEGIONS)
        if create_legions != False:
            print(current_time," create legions Button found")
            click(create_legions.left+25,create_legions.top+15)
        else:
            print(current_time," no create legions button")
            full = detectElement(FULL)
            if full != False:
                print(current_time," The legions are full, sleeping "+str(EXPONENTIAL_BACKOFF)+" minute")
                sleep(60*EXPONENTIAL_BACKOFF)
                if EXPONENTIAL_BACKOFF <= 10:
                   EXPONENTIAL_BACKOFF+=1
            else:
                print(current_time," The legions are not full, continuing")
                EXPONENTIAL_BACKOFF=1

        march = detectElement(MARCH)
        if march != False:
            print(current_time," march Button found")
            click(march.left+25,march.top+30)
        else:
            print(current_time," no march button")


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