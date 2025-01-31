
# pip install opencv-python pyautogui numpy keyboard
# Screen Recorder Using Python

import cv2
import numpy as np
import pyautogui
import keyboard
import time

# Get screen size
screen_size = pyautogui.size()

# Video settings
fps = 20
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = 'screenrecord.mp4'

# Initialize VideoWriter
out = cv2.VideoWriter(output, fourcc, fps, (screen_size.width, screen_size.height))

print('Recording... (press "n" to Stop)')

while True:
    # Capture screenshot
    screen = pyautogui.screenshot()
    
    # Convert screenshot to a numpy array
    frame = np.array(screen)
    
    # Convert RGB to BGR (OpenCV uses BGR)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Write the frame to the video file
    out.write(frame)
    
    # Check if 'n' is pressed to stop recording
    if keyboard.is_pressed('n'):
        print('Recording Stopped...')
        break
    
    # Add a small delay to reduce CPU usage
    time.sleep(1 / fps)

# Release the VideoWriter and close the file
out.release()
print(f'Video saved to {output}')