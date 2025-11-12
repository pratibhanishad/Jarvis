import pyautogui as ui
import random
import time
from FUNCTION.JARVIS_SPEAK.speak import *
from DATA.JARVIS_DLG_DATASET.DLG import open_dld


def open(text):

        x = random.choice(open_dld)
        # Open Windows search
        speak(x + " "+ text)
        time.sleep(0.5)
        ui.hotkey("win")
        time.sleep(0.2)
        # Type application name
        ui.write(text)
        time.sleep(0.5)
        ui.press("enter")

