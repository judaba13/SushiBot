from PIL import ImageGrab
import os
import time

def screenGrab():
	box = ()
	im = ImageGrab.grab()
	im.save(os.getcwd() + '\\full_screen_' + str(int(time.time())) + '.png', 'PNG')

def main():
	screenGrab()

if __name__ == '__main__':
	main()