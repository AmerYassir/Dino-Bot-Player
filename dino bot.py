
import cv2
import pyautogui
import numpy as np
import keyboard
import time
# Set the region of the screen to record (left, top, width, height)
screen_region = (200, 470, 800, 100)
time.sleep(2)
vision=5
try:
    while True:
        screenshot = pyautogui.screenshot(region=screen_region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        for i in range(0,10,1):

            if  all(channel == value for channel, value in zip(frame[15, i+vision], (172, 172, 172))):
                
                keyboard.press("space")
 
                vision+=1
                print("hump "+str(vision))
            
            if  all(channel == value for channel, value in zip(frame[75, i+vision], (172, 172, 172))):
                
                keyboard.press("down")
 
                vision+=1
                print("hump "+str(vision))
        #cv2.imshow("Screen Recording", frame)
        
        # Exit the loop when 'q' key is pressed
        
except KeyboardInterrupt:
    pass

# Close OpenCV windows
cv2.destroyAllWindows()
