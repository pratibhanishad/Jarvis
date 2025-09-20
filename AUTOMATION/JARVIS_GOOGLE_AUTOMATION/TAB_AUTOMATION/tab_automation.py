import pyautogui

def new_tab():
    pyautogui.hotkey("ctrl", "t")

def close_tab():
    pyautogui.hotkey("ctrl", "w")

def reopen_closed_tab():
    pyautogui.hotkey("ctrl", "shift", "t")

def next_tab():
    pyautogui.hotkey("ctrl", "tab")

def previous_tab():
    pyautogui.hotkey("ctrl", "shift", "tab")

def first_tab():
    pyautogui.hotkey("ctrl", "1")

def second_tab():
    pyautogui.hotkey("ctrl", "2")

def third_tab():
    pyautogui.hotkey("ctrl", "3")

def fourth_tab():
    pyautogui.hotkey("ctrl", "4")

def fifth_tab():
    pyautogui.hotkey("ctrl", "5")

def sixth_tab():
    pyautogui.hotkey("ctrl", "6")

def seventh_tab():
    pyautogui.hotkey("ctrl", "7")

def eighth_tab():
    pyautogui.hotkey("ctrl", "8")

def last_tab():
    pyautogui.hotkey("ctrl", "9")

def duplicate_tab():
    pyautogui.hotkey("alt", "d")
    pyautogui.hotkey("alt", "enter")

def move_tab_left():
    pyautogui.hotkey("ctrl", "shift", "pageup")

def move_tab_right():
    pyautogui.hotkey("ctrl", "shift", "pagedown")

def pin_tab():
    pyautogui.hotkey("ctrl", "shift", "p")  # (works with some extensions)

def mute_tab():
    pyautogui.hotkey("ctrl", "m")  # requires custom mapping in Chrome flags

def search_tabs():
    pyautogui.hotkey("ctrl", "shift", "a")

def open_tab_in_new_window():
    pyautogui.hotkey("ctrl", "shift", "n")  # new window
    pyautogui.hotkey("ctrl", "shift", "t")  # move last tab

def send_tab_to_left_window():
    pyautogui.hotkey("ctrl", "shift", "left")

def send_tab_to_right_window():
    pyautogui.hotkey("ctrl", "shift", "right")
