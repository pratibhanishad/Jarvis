import pyautogui as ui
import random
from FUNCTION.JARVIS_SPEAK.speak import *
from DATA.JARVIS_DLG_DATASET.DLG import open_dld


def open(text):
    x = random.choice(open_dld)
    speak(x+""+text)
    time.sleep(0.5)
    ui.hotkey("win")
    time.sleep(0.2)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
