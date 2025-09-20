import pyautogui
import time

def play_pause():
    pyautogui.press("space")

def volume_up():
    pyautogui.press("up")

def volume_down():
    pyautogui.press("down")

def seek_forward_5s():
    pyautogui.press("right")

def seek_backward_5s():
    pyautogui.press("left")

def seek_backward_10s():
    pyautogui.press("j")

def seek_forward_10s():
    pyautogui.press("l")

def frame_backward():
    pyautogui.press(",")

def frame_forward():
    pyautogui.press(".")

def seek_to_percent(num):  # num = 0 to 9
    pyautogui.press(str(num))

def seek_to_start():
    pyautogui.press("home")  # ↖ key = home

def seek_to_end():
    pyautogui.press("end")

def prev_chapter():
    pyautogui.hotkey("ctrl", "left")

def next_chapter():
    pyautogui.hotkey("ctrl", "right")

def decrease_speed():
    pyautogui.hotkey("shift", ",")

def increase_speed():
    pyautogui.hotkey("shift", ".")

def next_video():
    pyautogui.hotkey("shift", "n")

def prev_video():
    pyautogui.hotkey("shift", "p")


