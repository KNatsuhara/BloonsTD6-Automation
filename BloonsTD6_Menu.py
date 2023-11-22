import pyautogui as pyg
from PIL import Image
import pytesseract
import time
import cv2
import numpy as np
import re
import OCR

tower_first = ['Hero', 'Dart', 'Boomerang', 'Bomb', 'Tack', 'Ice', 'Glue', 'Sniper', 'Sub', 'Buccaneer']
tower_second = ['Ace', 'Heli', 'Mortar', 'Dartling', 'Wizard', 'Super', 'Ninja', 'Alchemist', 'Druid', 'Banana']
tower_third = ['Spike', 'Village', 'Engineer', 'Beast']
directory = r'Money'
middle_x_point = 615
IN_GAME_MONEY = 0

TOWERS_ON_BOARD = []

def Set_Game_Window():
    # Hover mouse at the top left corner of the window on the monkey logo
    # Preset window dimensions to 1440 x 900
    time.sleep(3)
    pyg.dragTo(10,10,1, button='left')
    pyg.click()

def Screen_Shot_Money():
    imgMoney = pyg.screenshot(region=(283,72,160,50))
    # imgMoney.save(r"Money/" + fname)
    imgMoney.save(r"C:/Users/Koji/OneDrive/BloonsTD6 Automation\BloonsTD6-Automation/Money/monkeyMoney.png")

def Image_Processing():
    image_path = r"Money/monkeyMoney.png"

    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    white_lo = np.array([0, 0, 255])
    white_hi = np.array([0, 0, 255])

    # Mask image to only select browns
    mask = cv2.inRange(hsv, white_lo, white_hi)

    # Change image to black where we found brown
    img[mask>0]=(255,255,255)

    invert_img = cv2.bitwise_not(mask)

    cv2.imwrite(r"Money/result1.png", invert_img)

def read_img():
    path_to_tesseracct = r"D:/Pytesseract/tesseract.exe"
    image_path = r"Money\result1.png"

    img = Image.open(image_path)

    pytesseract.tesseract_cmd = path_to_tesseracct

    # Pass the image through pytesseract
    text = pytesseract.image_to_string(img)
    return text

def Parse_Text(input_string):
    # Use a regular expression to extract only numbers
    numbers = re.findall(r'\d+', input_string)

    # Combine the extracted numbers into a single string
    result_string = ''.join(numbers)

    # Convert the parsed string to an integer (if needed)
    parsed_value = int(result_string)

    return (parsed_value)


def Reset_Screen():
    pyg.click(1225,894)

class Tower:
    def __init__(self, towerName, xPos, yPos):
        self.towerName = towerName
        self.xPos = xPos
        self.yPos = yPos
    
    def Select_Tower(self, towerName):
        pyg.click(1285,250) #Hero
        pyg.press('esc')
        pyg.press('esc')
        pyg.press('esc')
        # Scroll to the top

        for x in range(17):
            pyg.scroll(10)
        time.sleep(0.5)
        
        if towerName in tower_second:
            for x in range(11):
                time.sleep(0.1)
                pyg.scroll(-10)
        elif towerName in tower_third:
            for x in range(15):
                time.sleep(0.1)
                pyg.scroll(-10)
            if (towerName == 'Spike'):
                pyg.click(1285,620) #Tack
            elif (towerName == 'Village'):
                pyg.click(1385,620) #Village
            elif (towerName == 'Engineer'):
                pyg.click(1285,740) #Engineer
            elif (towerName == 'Beast'):
                pyg.click(1385,740) #Beast
        
        if (towerName == 'Hero' or towerName == 'Ace'):
            pyg.click(1285,250)
        elif (towerName == 'Dart' or towerName == 'Heli'):
            pyg.click(1385,255)
        elif (towerName == 'Boomerang' or towerName == 'Mortar'):
            pyg.click(1285,360)
        elif (towerName == 'Bomb' or towerName == 'Dartling'):
            pyg.click(1385,360)
        elif (towerName == 'Tack' or towerName == 'Wizard'):
            pyg.click(1285,470)
        elif (towerName == 'Ice' or towerName == 'Super'):
            pyg.click(1385,470)
        elif (towerName == 'Glue' or towerName == 'Ninja'):
            pyg.click(1285,580)
        elif (towerName == 'Sniper' or towerName == 'Alchemist'):
            pyg.click(1385,580)
        elif (towerName == 'Sub' or towerName == 'Druid'):
            pyg.click(1285,690)
        elif (towerName == 'Buccaneer' or towerName == 'Banana'):
            pyg.click(1385,690)

    def Place_Tower(self):
        self.Select_Tower(self.towerName)
        pyg.click(self.xPos, self.yPos)

    def UpgradeTier1(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < middle_x_point): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1156, 450) # Right Side
        else:
            pyg.click(250, 450) # Left Side
        Reset_Screen()
    
    def UpgradeTier2(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < middle_x_point): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1156, 577)
        else:
            pyg.click(250, 577)
        Reset_Screen()
    
    def UpgradeTier3(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < middle_x_point): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1156, 700)
        else:
            pyg.click(250, 700)
        Reset_Screen()
    
    def Sell(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < middle_x_point): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1152, 804)
        else:
            pyg.click(254, 804)
        Reset_Screen()
        # Delete tower
        del self
    
    def Set_Target_Priority(self, targetName):
        targetSelection = ['First', 'Last', 'Close', 'Strong']
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < 628): # Based on tower xPos the upgrades tab is on the left or right side
            if targetName in targetSelection:
                for x in range(targetSelection.index(targetName)):
                    pyg.click(1190, 370)
        else:
            if targetName in targetSelection:
                for x in targetSelection.index(targetName):
                    pyg.click(286, 369)
        Reset_Screen()
    
    def Set_Target(self, xTarget, yTarget):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < 628): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1072, 367)
        else:
            pyg.click(182, 367)
        # Set target position
        pyg.click(xTarget, yTarget)
        Reset_Screen()

    def Secondary_Ability(self, xTarget, yTarget):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < 628): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1207, 307)
        else:
            pyg.click(307, 307)
        # Set target position
        Reset_Screen()


# pytesseract OCR library Opitcal Character Recognition
# Screenshot
# Crop image to show only the money
# Reads the amount of money the user currently has
# Delete old money images

# Set_Game_Window()

# Dart1 = Tower('Dart')
# Dart1.Place_Tower()

# Dart2 = Tower('Dart')
# Dart2.Place_Tower()

if __name__ == "__main__":
    for i in range(10):
        time.sleep(2)
        Screen_Shot_Money()
        time.sleep(1)
        Image_Processing()
        time.sleep(1)
        money = read_img()
        # OCR.image_to_text()
        IN_GAME_MONEY = Parse_Text(money)
        print(IN_GAME_MONEY)

# Hero = Tower('Hero', 627, 428)
# Hero.Place_Tower()

# Druid1 = Tower('Druid', 512, 407)
# Druid1.Place_Tower()
# Druid1.UpgradeTier1()
# Druid1.UpgradeTier2()

# Engineer1 = Tower('Engineer', 512, 459) # 526, 489)
# Engineer1.Place_Tower()
# Engineer1.UpgradeTier2()
# Engineer1.UpgradeTier3()

# Village1 = Tower('Village', 498, 312)
# Village1.Place_Tower()
# Village1.UpgradeTier1()
# Village1.UpgradeTier1()
# Village1.UpgradeTier1()
# Village1.UpgradeTier2()

# Bomb1 = Tower('Bomb', 417, 410)
# Bomb1.Place_Tower()

# Wizard1 = Tower('Wizard', 352, 406)
# Wizard1.Place_Tower()

# Alchemist1 = Tower('Alchemist', 255, 309)
# Alchemist1.Place_Tower()

# Sniper1 = Tower('Sniper', 347, 277)
# Sniper1.Place_Tower()

# Sniper2 = Tower('Sniper', 403, 276)
# Sniper2.Place_Tower()


# Place Tower First
# Upgrade the Tower