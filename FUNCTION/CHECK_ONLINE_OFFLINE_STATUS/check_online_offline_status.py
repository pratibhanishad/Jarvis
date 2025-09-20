import requests

from FUNCTION.JARVIS_SPEAK.speak import speak
from FUNCTION.OFFLINE_VOICE.speak2 import fspeak

def is_online(url="https://www.google.com", timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code>=200 and response.status_code < 300
    except requests.RequestException:
        return False

# Optional test code
def internet_status():
    if is_online():
        x= "YES PRATIBHA ! I AM READY AND ONLINE"
        speak(x)
    else:
       x = "HEY THERE SIR ! I AM FRIDAY, SORRY BUT JARVIS IS CURRENTLY NOT ONLINE"
       print(x)

def internet_status():
    if is_online():
        x= "hey PRATIBHA ! I AM READY AND ONLINE"

    else:
       x = "HEY THERE SIR ! I AM FRIDAY, SORRY BUT JARVIS IS CURRENTLY NOT ONLINE"


def realtime_online_checker():
    prev_status = None

    while True:
        try:
            current_status = internet_status()

            if current_status != prev_status:
                fspeak(current_status)
                prev_status = current_status
        except Exception as e:
            print(e)
            pass
