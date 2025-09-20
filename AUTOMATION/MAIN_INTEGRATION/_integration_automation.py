from AUTOMATION.COMMON_AUTOMATION.COMMON_INTEGRATION.common_integration import *
from AUTOMATION.JARVIS_GOOGLE_AUTOMATION.GOOGLE_INTEGRATION.google_integration_main import *
from AUTOMATION.JARVIS_BATTERY_AUTOMATION.BATTERY_INTEGRATION.battery_integration_main import *
from AUTOMATION.JARVIS_YOUTUBE_AUTOMATION.YOUTUBE_INTEGRATION.youtube_integration_main import *

def Automation(text):
      youtube_cmd(text)
      google_cmd(text)
      battery_cmd(text)
      common_cmd(text)


