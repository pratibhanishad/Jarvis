import random
import time

import requests

from FUNCTION.JARVIS_LISTEN.listen import listen
from FUNCTION.JARVIS_SPEAK.speak import speak


def get_random_joke():
    headers = {
        'accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def jokes():
    x = [ 600,550, 580, 400, 3000, 800, 700, 8200, 50, 568]
    x = random.choice(x)
    time.sleep(x)
    speak("I have some jokes for you sir")
    text = listen().lower()
    if "yes tell me" in text or "yes" in text or "ha" in text:
        advice = get_random_joke()
        speak(advice)
    else:
        speak("No Problem sir, I just want to include some entertainment in your day")
