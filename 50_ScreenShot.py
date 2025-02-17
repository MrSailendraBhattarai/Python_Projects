
import pyautogui
from PIL import Image

myScreenshot=pyautogui.screenshot()
myScreenshot.save(r'screenshot.png')
print('Success ')
Image.open(r'screenshot.png')
