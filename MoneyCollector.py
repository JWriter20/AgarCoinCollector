import threading
import datetime
import webbrowser
import time

currentDT = datetime.datetime.now()

hour = currentDT.hour

requiredHour = 19

def getCoins():
    from pynput.mouse import Button, Controller
    webbrowser.open("https://agar.io/")
    mouse = Controller()
    delay = 0.001
    button = Button.left
    mouse.position = (351, 395)
    time.sleep(8)
    mouse.click(button)
    time.sleep(1)
    mouse.position = (893, 355)
    mouse.click(button)

    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press('w')
    keyboard.release(Key.cmd)
    keyboard.release('w')

while True:
    if hour == requiredHour:
        getCoins()
        if requiredHour == 24:
            requiredHour = 1
        else:
            requiredHour += 1
    time.sleep(600)
