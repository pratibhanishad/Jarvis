import difflib
import random
import webbrowser
from DATA.JARVIS_DLG_DATASET.DLG import websites, open_dld, success_open ,open_maybe,sorry_open
from FUNCTION.JARVIS_SPEAK.speak import speak


#  Website Open Function
def openweb(text):
    # Convert the input to lowercase
    website_name_lower = text.lower()

    #
    # Check if exact match exists
    if website_name_lower in websites:
        random_dlg = random.choice(open_dld)
        speak(random_dlg + text)
        url = websites[website_name_lower]
        webbrowser.open(url)
    else:
        # ✅ Fuzzy Matching
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            random_dlg = random.choice(open_dld)
            randonopen2 = random.choice(open_maybe)
            closest_match = matches[0]
            speak(randonopen2 + random_dlg + text)
            url = websites[closest_match]
            webbrowser.open(url)
            randonsucess = random.choice(success_open)
            speak(randonsucess)
        else:
            randonsorry = random.choice(sorry_open)
            speak(randonsorry + " named " + text)
