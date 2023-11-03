import pyautogui as pyg
from PIL import Image
import pytesseract
import os
import time
import cv2

# imgMoney = pyg.screenshot(region=(211,87,226,65))
# imgMoney.save(r"Money\testScreenshot.png")


filename = 'test'

for i in range (5):
    time.sleep(5)
    fname = 'test' + str(i)
    print(fname)
    imgMoney = pyg.screenshot(region=(211,87,226,65))
    imgMoney.save(r"Money\testScreenshot.png")