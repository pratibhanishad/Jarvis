from AUTOMATION.JARVIS_GOOGLE_AUTOMATION.SEARCH_IN_GOOGLE.search_in_google import *
from AUTOMATION.JARVIS_GOOGLE_AUTOMATION.OPEN_WEBSITE.open_website import *
from AUTOMATION.JARVIS_GOOGLE_AUTOMATION.SCROLE_AUTOMATION.scrole_automation import *
from AUTOMATION.JARVIS_GOOGLE_AUTOMATION.TAB_AUTOMATION.tab_automation import *
from AUTOMATION.COMMON_AUTOMATION.COMMON_CLOSE.close import *
from AUTOMATION.COMMON_AUTOMATION.COMMON_OPEN.open import *

def google_cmd(text):
    if "open" in text:
        if "website" in text or "site" in text:
           text = text.replace("open", "")
           text = text.replace("website", "")
           text = text.replace("site", "")
           text = text.strip()
           openweb(text)
        else:
            text = text.replace("open","")
            text = text.strip()
            if text == "":
                pass
            else:
                open(text)
    if "scroll up" in text:
        scroll_up()

    elif "scroll down" in text:
        scroll_down()

    elif "scroll left" in text:
        scroll_left()

    elif "scroll right" in text:
        scroll_right()

    elif text.endswith("search in google") or text.startswith("search on google"):
        text = text.replace("search in google", "")
        text = text.replace("search on google", "")
        search_google(text)
    elif text == "close tab":
        close_tab()
    elif text == "reopen closed tab":
        reopen_closed_tab()
    elif text == "next tab":
        next_tab()
    elif text == "previous tab":
        previous_tab()
    elif text == "first tab":
        first_tab()
    elif text == "second tab":
        second_tab()
    elif text == "third tab":
        third_tab()
    elif text == "fourth tab":
        fourth_tab()
    elif text == "fifth tab":
        fifth_tab()
    elif text == "sixth tab":
        sixth_tab()
    elif text == "seventh tab":
        seventh_tab()
    elif text == "eighth tab":
        eighth_tab()
    elif text == "last tab":
        last_tab()
    elif text == "duplicate tab":
        duplicate_tab()
    elif text == "move tab left":
        move_tab_left()
    elif text == "move tab right":
        move_tab_right()
    elif text == "pin tab":
        pin_tab()
    elif text == "mute tab":
        mute_tab()
    elif text == "search tabs":
        search_tabs()
    elif text == "open tab in new window":
        open_tab_in_new_window()
    elif text == "send tab to left window":
        send_tab_to_left_window()
    elif text == "send tab to right window":
        send_tab_to_right_window()
    elif text == "new tab":
        new_tab()
    else:
        pass