import pyautogui
import time

# --- Basic Controls ---
def scroll_up():
    pyautogui.scroll('up')   # positive = up
    pyautogui.scroll('up')   # positive = up
    pyautogui.scroll('up')   # positive = up
    pyautogui.scroll('up')   # positive = up
    pyautogui.scroll('up')   # positive = up
    pyautogui.scroll('up')   # positive = up

def scroll_down():
    pyautogui.scroll('down')  # negative = down
    pyautogui.scroll('down')  # negative = down
    pyautogui.scroll('down')  # negative = down
    pyautogui.scroll('down')  # negative = down
    pyautogui.scroll('down')  # negative = down


def scroll_left():
    pyautogui.hotkey('home')  # negative = left

def scroll_right():
    pyautogui.hotkey('end')   #