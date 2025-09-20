import threading
from BRAIN.MAIN_BRAIN.BRAIN.brain import *
from AUTOMATION.MAIN_INTEGRATION._integration_automation import *
from FUNCTION.MAIN_FUNCTION_INTEGRATION.function_integration import *
from FUNCTION.JARVIS_LISTEN.listen import *
from DATA.JARVIS_DLG_DATASET.DLG import *
from BRAIN.ACTIVITY.GREATINGS.WELCOME_GREATINGS.welcome_greatings import *
from BRAIN.ACTIVITY.GREATINGS.WISH_GREATINGS.wish_greatings import *
from BRAIN.ACTIVITY.ADVICE.advice import *
from BRAIN.ACTIVITY.JOKE.jokes import *
from AUTOMATION.JARVIS_BATTERY_AUTOMATION.BATTERY_PLUG_CHECK.battery_plug_check import *
from AUTOMATION.JARVIS_BATTERY_AUTOMATION.BATTERY_ALERT.battery_alert import *
from playsound import playsound
import eel
from FUNCTION.CHECK_ONLINE_OFFLINE_STATUS.check_online_offline_status import *

eel.init(r'C:\Users\chatu\OneDrive\Desktop\J.A.R.V.I.S\web')

def comain():
   while True:
       text= listen().lower()
       text = text.replace("jar", "jarvis")
       Automation(text)
       Function_cmd(text)
       Greating(text)

       if text in bye_key_word:
           x= random.choice(res_bye)
           speak(x)
           break
       elif "jarvis" in text:
           response = brain(text)
           speak(response)

       else:
          pass
def main():
    playsound(r"C:\Users\PRATI\Desktop\JARVIS4.1\DATA\MUSIC\SOUND_EFFECT\mixkit-sci-fi-click-900.wav")
    time.sleep(2)
    # while True:
    #     wake_cmd = hearing().lower()
    #     if wake_cmd in wake_key_word:
    welcome()
    comain()
        # else:
        #     pass

def jarvis():
    playsound(r"C:\Users\PRATI\Desktop\JARVIS4.1\DATA\MUSIC\SOUND_EFFECT\mixkit-bonus-earned-in-video-game-2058.wav")

    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=battery_alert)
    t3 = threading.Thread(target=check_plugin_status)
    t4 = threading.Thread(target=advice)
    t5 = threading.Thread(target=jokes)
    t6 = threading.Thread(target=realtime_online_checker)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()


jarvis()