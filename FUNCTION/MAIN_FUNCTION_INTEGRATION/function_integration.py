from FUNCTION.CHECK_INTERNET_SPEED.check_speed import *
from FUNCTION.CHECK_ONLINE_OFFLINE_STATUS.check_online_offline_status import *
from FUNCTION.CHECK_TEMPERATURE.check_temperature import *
from FUNCTION.CLOCK.clock import *
from FUNCTION.FIND_MY_IP.find_my_ip import *
from FUNCTION.MUSIC_WITH_CLAP.clap_with_music import *
from FUNCTION.SEO_GENERATOR.seo_generator import *
import pyautogui as gui

def Function_cmd(text):
    if "check internet speed" in text or "check speed test" in text or "speed test" in text or "internet speed" in text:
        check_internet_speed()
    elif "are you there" in text or "hello there" in text:
        internet_status()
    elif "check temperature" in text or "temperature" in text:
        Temp()
    elif "find my ip" in text or "ip address" in text:
        speak("your ip is" +  find_my_ip())
    elif "what is the time" in text or "time " in text or "what time is" in text:
        what_is_the_time()
    elif "start clap with music system " in text or "start smart music system" in text or "start clap with music" in text or "start clap music" in text:
        speak("ok now starting")
        clap_to_music()
    elif "activate seo generator" in text or "activate youtube title generator" in text or "activate seo generator" in text:
         seo_app()
    elif "select all" in text or "select all paragraph" in text:
        gui.hotkey("ctrl", "a")
    elif "write" in text or "likho" in text or "right" in text:
        speak("writing")
        text = text.replace("write", "").replace("likho", "").replace("right", "")
        gui.write(text)

    elif "enter" in text or "press enter" in text or "send" in text:
        gui.press("enter")

    elif "select all" in text or "select all paragraph" in text:
        gui.hotkey("ctrl", "a")

    elif "copy" in text or "copy this" in text:
        gui.hotkey("ctrl", "c")


    elif "paste" in text or "paste here" in text or "paste kr do" in text:
        gui.hotkey("ctrl", "v")

    elif "undo" in text or "undo karo" in text:
        gui.hotkey("ctrl", "z")

    elif "copy last paragraph" in text:
        gui.hotkey("ctrl", "shift", "c")

    # Volume increase
    elif "increase volume" in text or "volume badhao" in text or "increase the volume" in text:
        for _ in range(5):
            gui.press("volumeup")
        print("Volume increased.")

    # Volume decrease
    elif "decrease volume" in text or "volume kam karo" in text or "decrease the volume" in text:
        for _ in range(5):
            gui.press("volumedown")
        print("Volume decreased.")

    # Full volume
    elif "full volume" in text or "full volume kr do" in text:
        for _ in range(20):
            gui.press("volumeup")
        speak("now your system in full volume")
        print("now your system in full volume")

    # Mute
    elif "mute" in text:
        gui.press("volumemute")
        print("Volume muted.")


    # Show location
    elif "show me location" in text or "check location" in text or "where is" in text:
        text = text.replace("show me the location", "")
        text = text.replace("check location", "")
        text = text.replace("where is", "")
        map(text)

    # Take rest / sleep
    elif "take some rest" in text or "go to sleep" in text or "so jao jarvis" in text or "aaram kr lo" in text:
        speak("ok sir! call me any time again")

        # Scroll
    elif "scroll up" in text or "uper jao" in text or"Scroll" in text:
        speak("scrolling page load.")
        gui.hotkey("ctrl", "up")

    elif "scroll down" in text:
        speak("scrolling down")
        gui.hotkey("ctrl", "down")  # example shortcut

        # Media controls
    elif "play" in text or "pause" in text or "stop" in text:
        speak("play your vidio  ")

    elif "next" in text:
        gui.hotkey("shift", "n")

    elif "previous" in text:
        gui.hotkey("shift", "p")
        # Window controls

    elif "minimize window" in text or "minimise" in text or "minm" in text:
        speak("Minimizing window.")
        gui.hotkey("win", "down")
        # Tabs
    elif "new tab" in text or "close window" in text:
        gui.hotkey("ctrl", "t")

    elif "close tab" in text:
        gui.hotkey("ctrl", "w")

    elif "switch tab" in text:
        gui.hotkey("ctrl", "tab")
        # Volume
    elif "volume up" in text or "volume badhao " in text:
        gui.press("volumeup")

    elif "volume down" in text or "volume kam kr do " in text:
        gui.press("volumedown")

    elif "mute" in text:
        gui.press("volumemute")
        # Screenshot

    elif "take screenshot" in text or "screenshot" in text:
        speak("Taking screenshot.")
        screenshot = gui.screenshot()
        filename = f"screenshot_{int(time.time())}.png"
        screenshot.save(filename)
        speak(f"Screenshot saved as {filename}")

    elif "shutdown" in text:
        speak("Shutting down your PC.")
        os.system("shutdown /s /t 1")

    elif "restart" in text:
        speak("Restarting your PC.")
        os.system("shutdown /r /t 1")

    elif "save page as" in text or "print " in text:
        speak("saveing page as")
        gui.hotkey("ctrl", "s")

    elif "open history" in text or "view history" in text:
        speak("opening History.")
        gui.hotkey("ctrl", "h")

    elif "clear history" in text:
        speak("clearing history data")
        gui.hotkey("ctrl", "shift", "del")

    elif "show desktop" in text or "hide windows" in text:
        speak("showing desktop")
        gui.hotkey("win", "m")

    elif "open file explorer" in text or "open my computer" in text:
        speak("Opening File Explorer.")
        gui.hotkey("win", "e")

    elif "open task manager" in text or "task manager" in text:
        speak("Opening Task Manager.")
        gui.hotkey("ctrl", "shift", "esc")

    elif "refresh" in text or "refresh the page" in text:
        speak("Refreshing.")
        gui.hotkey("f5")

    elif "open run" in text or "run command" in text:
        speak("Opening Run window.")
        gui.hotkey("win", "r")
    # Zoom In
    elif "zoom in" in text:
        speak("Zooming in.")
        gui.hotkey("ctrl", "+")

    elif "new window" in text:
        speak("Opening new browser window.")
        gui.hotkey("ctrl", "n")

        # Incognito Mode
    elif "open incognito" in text or "incognito mode" in text:
        speak("Opening incognito window.")
        gui.hotkey("ctrl", "shift", "n")

    # Zoom Out
    elif "zoom out" in text:
        speak("Zooming out.")
        gui.hotkey("ctrl", "-")

        # Go Back in Browser
    elif "go back" in text or "previous page" in text:
        speak("Going back.")
        gui.hotkey("alt", "left")

    # Go Forward in Browser
    elif "go forward" in text or "next page" in text:
        speak("Going forward.")
        gui.hotkey("alt", "right")

    # Page Reload Hard
    elif "hard reload" in text or "force reload" in text:
        speak("Hard reloading the page.")
        gui.hotkey("ctrl", "shift", "r")


    # Minimize All Windows
    elif "minimize all" in text:
        speak("Minimizing all windows.")
        gui.hotkey("win", "d")

    # Close Current Window
    elif "close window" in text:
        speak("Closing current window.")
        gui.hotkey("alt", "f4")

    # Switch Between Windows
    elif "switch window" in text:
        speak("Switching windows.")
        gui.hotkey("alt", "tab")

    # Reopen Last Closed Tab
    elif "reopen tab" in text or "restore tab" in text:
        speak("Reopening last closed tab.")
        gui.hotkey("ctrl", "shift", "t")

    # Scroll to Top
    elif "scroll top" in text or "go to top" in text or "Go to" in text:
        speak("Scrolling to top.")
        gui.press("home")

    # Scroll to Bottom
    elif "scroll bottom" in text or "go to bottom" in text:
        speak("Scrolling to bottom.")
        gui.press("end")

    # Select Current Line
    elif "select line" in text or"Select line" in text:
        speak("Selecting current line.")
        gui.hotkey("shift", "home")

    elif text.startswith("search"):
        gui.hotkey("/")
        text = text.replace("search", "").strip()
        gui.write(text)
        speak(f"searching {text}")
        time.sleep(1)
        gui.press("enter")
        print(f"searching {text}")


    else:
        pass

