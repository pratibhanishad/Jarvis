import random
import datetime
from datetime import date
from DATA.JARVIS_DLG_DATASET.DLG import good_morningdlg, good_afternoondlg, good_eveningdlg, good_nightdlg
from FUNCTION.JARVIS_SPEAK.speak import speak

today = date.today()
formatted_date = today.strftime("%d %B %Y")
nowx = datetime.datetime.now()

def wish():
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gd_dlg = random.choice(good_morningdlg)
        speak(gd_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(good_afternoondlg)
        speak(ga_dlg)
    elif 17 <= current_hour < 21:
        ge_dlg = random.choice(good_eveningdlg)
        speak(ge_dlg)
    else:
        gn_dlg = random.choice(good_nightdlg)
        speak(gn_dlg)

def Greating(text):
    if "good morning" in text or "good afternoon " in text or "good evening in text" or "good night in text":
        wish()
    else:
        pass
