import random
import time

import requests

from FUNCTION.JARVIS_LISTEN.listen import listen
from FUNCTION.JARVIS_SPEAK.speak import speak

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def advice():
    x = [ 600,550, 580, 400, 3000, 800, 700, 8200, 50, 568]
    x = random.choice(x)
    time.sleep(x)
    speak("I have some suggestion for you sir")
    text = listen().lower()
    if "yes tell me" in text or "yes" in text or "ha" in text:
        advice = get_random_advice()
        speak(advice)
    else:
        speak("No Problem I think you need some advive so I give")


