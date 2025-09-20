import random
import time
import psutil
from DATA.JARVIS_DLG_DATASET.DLG import low_b, medium_m, full_f
from FUNCTION.JARVIS_SPEAK.speak import speak


def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 10:
            random_low = random.choice(low_b)
            speak(random_low)
        elif percent < 30:
            random_medium = random.choice(medium_m)
            speak(random_medium)
        elif percent == 100:
            random_full = random.choice(full_f)
            speak(random_full)
        else:
            pass

        time.sleep(1500)

def battery_alert1():
        time.sleep(3)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 10:
            random_low = random.choice(low_b)
            speak(random_low)
        elif percent < 30:
            random_medium = random.choice(medium_m)
            speak(random_medium)
        elif percent == 100:
            random_full = random.choice(full_f)
            speak(random_full)
        else:
            speak("sir, your battery is in perfect battery level")

