import pyautogui


def go_to_search():
    pyautogui.press("/")   # on QWERTY, use "/" ; AZERTY keyboards need Shift+/ sometimes

def toggle_play_pause():
    pyautogui.press("k")

def toggle_mute():
    pyautogui.press("m")

def toggle_fullscreen():
    pyautogui.press("f")

def toggle_theater_mode():
    pyautogui.press("t")

def toggle_miniplayer():
    pyautogui.press("i")

def exit_modes():
    pyautogui.press("esc")

def party_mode():
    pyautogui.typewrite("awesome")  # typing 'awesome' triggers party mode

# ----------- Navigation Shortcuts -----------

def navigate_forward():
    pyautogui.press("tab")

def navigate_backward():
    pyautogui.hotkey("shift", "tab")

def select_control():
    pyautogui.press("enter")

def settings_navigation_up():
    pyautogui.press("up")

def settings_navigation_down():
    pyautogui.press("down")

def settings_navigation_left():
    pyautogui.press("left")

def settings_navigation_right():
    pyautogui.press("right")

def close_settings_menu():
    pyautogui.press("esc")

import pyautogui

# Playback controls
def play_pause():
    pyautogui.press("space")

def volume_up():
    pyautogui.press("up")

def volume_down():
    pyautogui.press("down")

def mute_unmute():
    pyautogui.press("m")

def seek_forward():
    pyautogui.press("l")

def seek_backward():
    pyautogui.press("j")

def seek_forward_frame():
    pyautogui.hotkey("shift", ".")

def seek_backward_frame():
    pyautogui.hotkey("shift", ",")

def seek_to_beginning():
    pyautogui.press("home")

def seek_to_end():
    pyautogui.press("end")

def seek_to_next_chapter():
    pyautogui.hotkey("ctrl", "right")

def seek_to_previous_chapter():
    pyautogui.hotkey("ctrl", "left")

# Screen modes
def fullscreen_toggle():
    pyautogui.press("f")

def theater_mode():
    pyautogui.press("t")

def mini_player():
    pyautogui.press("i")

def exit_fullscreen():
    pyautogui.press("esc")

# Zoom / Pan (for spherical videos)
def pan_up():
    pyautogui.press("w")

def pan_down():
    pyautogui.press("s")

def pan_left():
    pyautogui.press("a")

def pan_right():
    pyautogui.press("d")

def zoom_in():
    pyautogui.press("]")

def zoom_out():
    pyautogui.press("[")

import pyautogui

# ---------- Playback Controls ----------
def play_pause():
    pyautogui.press("k")

def volume_up():
    pyautogui.press("up")

def volume_down():
    pyautogui.press("down")

def toggle_mute_unmute():
    pyautogui.press("m")

def seek_forward():
    pyautogui.press("l")

def seek_backward():
    pyautogui.press("j")

def seek_forward_frame():
    pyautogui.hotkey("shift", ".")

def seek_backward_frame():
    pyautogui.hotkey("shift", ",")

def seek_to_beginning():
    pyautogui.press("home")

def seek_to_end():
    pyautogui.press("end")

def seek_to_next_chapter():
    pyautogui.hotkey("ctrl", "right")

def seek_to_previous_chapter():
    pyautogui.hotkey("ctrl", "left")

def decrease_playback_speed():
    pyautogui.press("<")   # same as Shift + ,

def increase_playback_speed():
    pyautogui.press(">")   # same as Shift + .

# ---------- Video Navigation ----------
def move_to_next_video():
    pyautogui.shift("n")   # works only in playlist/queue

def move_to_previous_video():
    pyautogui.shift("p")   # works only in playlist/queue

# ---------- Subtitles ----------
def toggle_subtitles():
    pyautogui.press("c")

# ---------- Search ----------
def go_to_search_box():
    pyautogui.press("/")   # AZERTY me Shift + / = :

# ---------- Screen Modes ----------
def toggle_full_screen():
    pyautogui.press("f")

def toggle_theater_mode():
    pyautogui.press("t")

def toggle_miniplayer_mode():
    pyautogui.press("i")

def exit_full_screen():
    pyautogui.press("esc")

# ---------- Party Mode ----------
def toggle_party_mode():
    pyautogui.typewrite("awesome")   # easter egg
    pyautogui.press("enter")

# ---------- Spherical Video Controls ----------
def pan_up():
    pyautogui.press("w")

def pan_down():
    pyautogui.press("s")

def pan_left():
    pyautogui.press("a")

def pan_right():
    pyautogui.press("d")

def zoom_in():
    pyautogui.press("]")   # numpad + bhi kaam karega

def zoom_out():
    pyautogui.press("[")   # numpad - bhi kaam karega

