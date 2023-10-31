import pyautogui as pyg
import time

tower_first = ['Hero', 'Dart', 'Boomerang', 'Bomb', 'Tack', 'Ice', 'Glue', 'Sniper', 'Sub', 'Buccaneer']
tower_second = ['Ace', 'Heli', 'Mortar', 'Dartling', 'Wizard', 'Super', 'Ninja', 'Alchemist', 'Druid', 'Banana']
tower_third = ['Spike', 'Village', 'Engineer', 'Beast']

TOWERS_ON_BOARD = []

def Set_Game_Window():
    # Hover mouse at the top left corner of the window on the monkey logo
    # Preset window dimensions to 1440 x 900
    time.sleep(3)
    pyg.dragTo(10,10,1, button='left')
    pyg.click()

def Screen_Shot():
    image = pyg.screenshot('Test_ScreenShot')

def Reset_Screen():
    pyg.click(1237,910)

class Tower:
    def __init__(self, towerName, xPos, yPos):
        self.towerName = towerName
        self.xPos = xPos
        self.yPos = yPos
    
    def Select_Tower(self, towerName):
        pyg.click(1300,255) #Hero
        pyg.press('esc')
        pyg.press('esc')
        pyg.press('esc')
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
                pyg.click(1300,620) #Tack
            elif (towerName == 'Village'):
                pyg.click(1400,620) #Village
            elif (towerName == 'Engineer'):
                pyg.click(1300,740) #Engineer
            elif (towerName == 'Beast'):
                pyg.click(1400,740) #Beast
        
        if (towerName == 'Hero' or towerName == 'Ace'):
            pyg.click(1300,255)
        elif (towerName == 'Dart' or towerName == 'Heli'):
            pyg.click(1400,255)
        elif (towerName == 'Boomerang' or towerName == 'Mortar'):
            pyg.click(1300,370)
        elif (towerName == 'Bomb' or towerName == 'Dartling'):
            pyg.click(1400,370)
        elif (towerName == 'Tack' or towerName == 'Wizard'):
            pyg.click(1300,480)
        elif (towerName == 'Ice' or towerName == 'Super'):
            pyg.click(1400,480)
        elif (towerName == 'Glue' or towerName == 'Ninja'):
            pyg.click(1300,600)
        elif (towerName == 'Sniper' or towerName == 'Alchemist'):
            pyg.click(1400,600)
        elif (towerName == 'Sub' or towerName == 'Druid'):
            pyg.click(1300,715)
        elif (towerName == 'Buccaneer' or towerName == 'Banana'):
            pyg.click(1400,715)

    def Place_Tower(self):
        self.Select_Tower(self.towerName)
        pyg.moveTo(self.xPos, self.yPos)
        pyg.click()
    
    def UpgradeTier1(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < 628): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1170, 463)
        else:
            pyg.click(266, 463)
        Reset_Screen()
    
    def UpgradeTier2(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < 628): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1170, 583)
        else:
            pyg.click(266, 583)
        Reset_Screen()
    
    def UpgradeTier3(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < 628): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1170, 709)
        else:
            pyg.click(266, 709)
        Reset_Screen()
    
    def Sell(self):
        pyg.click(self.xPos, self.yPos) # Select Tower
        time.sleep(0.1)
        if (self.xPos < 628): # Based on tower xPos the upgrades tab is on the left or right side
            pyg.click(1160, 808)
        else:
            pyg.click(271, 808)
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
Hero = Tower('Hero', 627, 428)
Hero.Place_Tower()

Druid1 = Tower('Druid', 526, 434)
Druid1.Place_Tower()
Druid1.UpgradeTier1()
Druid1.UpgradeTier2()

Engineer1 = Tower('Engineer', 524, 486) # 526, 489)
Engineer1.Place_Tower()
Engineer1.UpgradeTier2()
Engineer1.UpgradeTier3()

Village1 = Tower('Village', 508, 325)
Village1.Place_Tower()
Village1.UpgradeTier1()
Village1.UpgradeTier1()
Village1.UpgradeTier1()
Village1.UpgradeTier2()

Bomb1 = Tower('Bomb', 425, 420)
Bomb1.Place_Tower()

Wizard1 = Tower('Wizard', 366, 422)
Wizard1.Place_Tower()

Alchemist1 = Tower('Alchemist', 271, 364)
Alchemist1.Place_Tower()

Sniper1 = Tower('Sniper', 359, 281)
Sniper1.Place_Tower()

Sniper2 = Tower('Sniper', 410, 276)
Sniper2.Place_Tower()


# Place Tower First
# Upgrade the Tower