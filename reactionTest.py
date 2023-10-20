import pyautogui
import keyboard
import numpy
import time

#failsafe otherwise it will constantly loop because once it's clicked to get a score the pxel autos to that rgb value starting the while lopp again. 
#so press 'h' on your keyboard to stop the program
while  keyboard.is_pressed('h') == False:
    #checks to see if the rgb values of the pixel at 772,526 on my screen match the rgb values i passed through: that being 34,34,34 if so click the screen
    #at that position
    if pyautogui.pixelMatchesColor(772,526,(34,34,34)):
        #using another library numpy to add randomness to the clicks to give variation and make it less bot like. 
        #we do not set a low range so it can have the ability to click instantly if it wants but the max length we want it to take is 0.3 seconds at a max
        time.sleep(numpy.random.uniform(high=0.3))
        #important to specify where to click otherwise it will click where you leave that mouse which could be a disaster. 
        pyautogui.click(x=772, y=526)  
        #just so we can see the score the code got instead of immediately trying again.
        time.sleep(1)
      
