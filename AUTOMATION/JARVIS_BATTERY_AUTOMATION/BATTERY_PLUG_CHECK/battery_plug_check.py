import random
import psutil
from DATA.JARVIS_DLG_DATASET.DLG import plug_in, unplug
from FUNCTION.JARVIS_SPEAK.speak import speak


def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                random_low = random.choice(plug_in)
                speak(random_low)
            else:
                random_low = random.choice(unplug)
                speak(random_low)
            previous_state = battery.power_plugged
previous_state = None
plug_in1 = ["Charger is plugged check conferm","battery is Charging that means charger is pluged check completed"]
plug_out1 = ["Charger is unplugged","battery is not Charging that means charger is not pluged check completed"]

def check_plugin_status1():
    global previous_state
    battery = psutil.sensors_battery()

    if battery.power_plugged != previous_state:
        if battery.power_plugged:
            random_low = random.choice(plug_in1)
            speak(random_low)
        else:
            random_low = random.choice(plug_out1)
            speak(random_low)
        previous_state = battery.power_plugged

