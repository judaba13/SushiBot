"""

Grabs Sushi Go Round Screen in Chrome browser with the
bookmarks toolbar enabled. All coordinates are for a screen
resolution of 1600 x 900.

You must change the coordinates of x_pad and y_pad accordingly
if your system does not match these specs by using an image 
program such as paint.net to find the specific coordinates of 
the top top-left part of the Sushi Go Round screen
"""
from PIL import ImageGrab
import os
import time

#Global variables for top-left corner of game screen
x_pad = 316
y_pad = 307

def screenGrab():
	box = (x_pad+1,y_pad+1,640+x_pad,480+y_pad)
	im = ImageGrab.grab(box)
	im.save(os.getcwd() + '\\full_screen_' + str(int(time.time())) + '.png', 'PNG')

def main():
	screenGrab()

if __name__ == '__main__':
	main()