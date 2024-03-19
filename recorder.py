import cv2
import numpy as np
import pyautogui
import keyboard         

try:
    #First we declared the fps, the resolution and the name for the video
    resolution = pyautogui.size()
    video_name = input("Please enter a name for the video ").strip().lower()
    key = input("Please enter a key to interrupt the video recording ").strip().lower()
    fps = float(input("Enter the amount of frames per second ").strip())
    
    #Make the corresponding validations for the necessary values
    if not video_name or type(video_name) != str:
        raise ValueError("The video name is invalid please try again ")
    
    if fps <= 0 or fps > 30:
        raise ValueError("The amount of frames per second is invalid please try again in the range 1 to 30")

    #Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'{video_name}.mp4', fourcc, fps, resolution)

    #Start a while cicle to get the frames for the screen and take the screenshots to make the video
    while True:
        frame = np.array(pyautogui.screenshot())
        frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
        out.write(frame)
    
    #Stop the recording if the selected key is pressed
        if keyboard.is_pressed(key):
            break
    
    #Release resources
    out.release()
    cv2.destroyAllWindows()
    print(f"Video recording completed: The video was saved whit the name {video_name}.mp4")
    
#Show the exeptions 
except Exception as e:
    print(f"An error occurred {e}")
        