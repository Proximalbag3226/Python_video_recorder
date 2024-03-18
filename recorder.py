import cv2
import numpy as np 
import pyautogui
import keyboard         

#First we declared the fpsm, the resolution and the name for the video 
fps = 20.0
resolution = pyautogui.size()
video_name = input("Please enter a name for the video ").strip().lower()
key = input("Please enter a key to interrupt the video recording ").strip().lower()

#And the codec type 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'{video_name}.mp4', fourcc, fps, resolution)

#Start a while cicle to get the frames for the screen and take the screenshots to make the video
while True:
    frame = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
    
    out.write(frame)
    
    if keyboard.is_pressed(key):
        break
out.release()
cv2.destroyAllWindows()
        