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
	win32api.SetCursorPos(cord[0] + x_pad, cord[1] + y_pad)

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

def main():
	pass

if __name__ == '__main__':
	main()