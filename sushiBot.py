"""

Sushi Go Round bot
Play the game here: http://www.miniclip.com/games/sushi-go-round/en/
then run this script.
Note: You must mine the proper coordinates for your system and browser
The current coordinates are for 1600 x 900 screen resolution 
on the Chrome browser with the bookmarks toolbar enabled.
"""
from PIL import ImageGrab
import os
import time
import win32api
import win32con

#Global variables for top-left corner of game screen
x_pad = 316
y_pad = 307

def screenGrab():
	box = (x_pad+1,y_pad+1,640+x_pad,480+y_pad)
	im = ImageGrab.grab(box)
	im.save(os.getcwd() + '\\full_screen_' + str(int(time.time())) + '.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click!"

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'Left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'Left Release'

def mousePos(cord):
	win32api.SetCursorPos((cord[0] + x_pad, cord[1] + y_pad))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

'''
Class to store the mined coordinates of important in game items
f_ corresponds to the food stand at the bottom left of the game
t_ corresponds to the items in the telephone
'''
class Cord:
    f_shrimp = (47,336)
    f_rice = (88,336)
    f_nori = (45,380)
    f_roe = (86,380)
    f_salmon = (48,435)
    f_unagi = (92,436)

    #------------------

    phone = (575,356)
 
    menu_toppings = (529,272)
     
    t_shrimp = (491,222)
    t_nori = (489,274)
    t_roe = (571,276)
    t_salmon = (493,330)
    t_unagi = (578,217)
    t_exit = (593,335)
 
    menu_rice = (525,293)
    buy_rice = (541,288)
     
    delivery_norm = (491,296)

#Function to clear the plates based on their mined coordinates
def clear_tables():
    mousePos((90, 209))
    leftClick()
 
    mousePos((195, 213))
    leftClick()
 
    mousePos((292, 213))
    leftClick()
 
    mousePos((396, 214))
    leftClick()
 
    mousePos((494, 212))
    leftClick()
 
    mousePos((595, 210))
    leftClick()
    time.sleep(1)

"""
Function to fold the mat after making a sushi 
"""
def foldMat():
    mousePos((Cord.f_rice[0]+55,Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)

"""
Function to make the specified food based on their recipes 
found in the recipe menu in game. 
TODO: Add more recipes as the become unlocked
"""
def makeFood(food):
    if food == 'caliroll':
        print 'Making a caliroll'
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print 'Making a onigiri'
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print 'Making a gunkan'
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
    elif food == 'salmon':
        print 'Making a salmon roll'
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def startGame():
    #Click through the menus
    #First menu
    mousePos((315,200))
    leftClick()
    time.sleep(.1)

    #Second menu
    mousePos((305,391))
    leftClick()
    time.sleep(.1)

    #Third menu
    mousePos((581,455))
    leftClick()
    time.sleep(.1)

    #Fourth menu
    mousePos((312,372))
    leftClick()
    time.sleep(.1)

def main():
	pass

if __name__ == '__main__':
	main()