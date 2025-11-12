import random
from DATA.JARVIS_DLG_DATASET.DLG import welcomedlg
from FUNCTION.JARVIS_SPEAK.speak import speak


def welcome():
    message = random.choice(welcomedlg)
    speak(message)
