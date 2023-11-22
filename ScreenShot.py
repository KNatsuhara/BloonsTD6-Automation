import pyautogui as pyg
from PIL import Image
import pytesseract
import os
import time
import cv2

# imgMoney = pyg.screenshot(region=(211,87,226,65))
# imgMoney.save(r"Money\testScreenshot.png")

imgMoney = pyg.screenshot(region=(283,72,160,50))
# imgMoney.save(r"Money/" + fname)
imgMoney.save(r"C:\Users\Koji\OneDrive\BloonsTD6 Automation\BloonsTD6-Automation\Money\monkeyMoney.png")

# for i in range (5):
#     time.sleep(5)
#     fname = 'test' + str(i) + '.png'
#     print(fname)
#     imgMoney = pyg.screenshot(region=(263,72,403,119))
#     # imgMoney.save(r"Money/" + fname)
#     imgMoney.save(r"C:\Users\Koji\OneDrive\BloonsTD6 Automation\BloonsTD6-Automation\Money\test.png")