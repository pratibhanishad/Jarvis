from AUTOMATION.JARVIS_BATTERY_AUTOMATION.BATTERY_ALERT.battery_alert import*
from AUTOMATION.JARVIS_BATTERY_AUTOMATION.BATTERY_PLUG_CHECK.battery_plug_check import*
from AUTOMATION.JARVIS_BATTERY_AUTOMATION.CHECK_BATTERY_PERCENTAGE.check_battery_percentage import *

def battery_cmd(text):
    if "check battery percentage" in text or "battery percentage" in text:
        battery_percentage()

    elif "check plug" in text or "check battery plug" in text:
        check_plugin_status()

    elif "give me battery alert" in text or "battery alert" in text:
        battery_alert1()

    else:
        pass
