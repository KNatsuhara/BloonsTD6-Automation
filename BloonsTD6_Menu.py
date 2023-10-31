import pyautogui as pyg
import time

tower_first = ['Hero', 'Dart', 'Boomerang', 'Bomb', 'Tack', 'Ice', 'Glue', 'Sniper', 'Sub', 'Buccaneer']
tower_second = ['Ace', 'Heli', 'Mortar', 'Dartling', 'Wizard', 'Super', 'Ninja', 'Alchemist', 'Druid', 'Banana']
tower_third = ['Spike', 'Village', 'Engineer', 'Beast']

def Set_Game_Window():
    # Hover mouse at the top left corner of the window on the monkey logo
    # Preset window dimensions to 1440 x 900
    time.sleep(3)
    pyg.dragTo(10,10,1, button='left')
    pyg.click()

def Select_Tower(towerName):
    pyg.click(1300,255) #Hero
    pyg.press('esc')
    pyg.press('esc')
    pyg.press('esc')
    for x in range(15):
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

def Place_Tower(towerName, xPos, yPos):
    Select_Tower(towerName)
    pyg.moveTo(xPos, yPos)
    pyg.click()

def Screen_Shot():
    image = pyg.screenshot('Test_ScreenShot')


# Set_Game_Window()
Place_Tower('Hero', 627, 428)
Place_Tower('Druid', 526, 434)
Place_Tower('Engineer', 526, 489)
# Place_Tower('Village', 510, 328)
# Place_Tower('Bomb', 431, 415)
# Place_Tower('Wizard', 368, 425)
# Place_Tower('Alchemist', 273, 367)
# Place_Tower('Sniper', 361, 284)
# Place_Tower('Sniper', 412, 279)