import threading
import subprocess
import os
import pyautogui as gui
import time
from playsound import playsound

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGraphicsDropShadowEffect, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer, QSize, pyqtSignal, QObject

# ----------------- Jarvis Backend -----------------
from BRAIN.MAIN_BRAIN.BRAIN.brain import *
from AUTOMATION.MAIN_INTEGRATION._integration_automation import *
from FUNCTION.MAIN_FUNCTION_INTEGRATION.function_integration import *
from FUNCTION.JARVIS_LISTEN.listen import *
from DATA.JARVIS_DLG_DATASET.DLG import *
from BRAIN.ACTIVITY.GREATINGS.WELCOME_GREATINGS.welcome_greatings import *
from BRAIN.ACTIVITY.GREATINGS.WISH_GREATINGS.wish_greatings import *
from BRAIN.ACTIVITY.ADVICE.advice import *
from BRAIN.ACTIVITY.JOKE.jokes import *
from AUTOMATION.JARVIS_BATTERY_AUTOMATION.BATTERY_PLUG_CHECK.battery_plug_check import *
from AUTOMATION.JARVIS_BATTERY_AUTOMATION.BATTERY_ALERT.battery_alert import *
from FUNCTION.CHECK_ONLINE_OFFLINE_STATUS.check_online_offline_status import *

# ----------------- Core Functions -----------------
def comain():
    while True:
        text = listen().lower()
        text = text.replace("jar", "jarvis")
        Automation(text)
        Function_cmd(text)
        Greating(text)

        if text in bye_key_word:
            x = random.choice(res_bye)
            speak(x)
            break
        elif "jarvis" in text:
            response = brain(text)
            speak(response)
        else:
            pass

def main():
    playsound(r"C:\Users\PRATI\Desktop\JARVIS4.1\DATA\MUSIC\SOUND_EFFECT\mixkit-sci-fi-click-900.wav")
    time.sleep(2)
    welcome()
    comain()

def jarvis():
    playsound(r"C:\Users\PRATI\Desktop\JARVIS4.1\DATA\MUSIC\SOUND_EFFECT\mixkit-bonus-earned-in-video-game-2058.wav")

    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=battery_alert)
    t3 = threading.Thread(target=check_plugin_status)
    t4 = threading.Thread(target=advice)
    t5 = threading.Thread(target=jokes)
    t6 = threading.Thread(target=realtime_online_checker)
    for t in [t1, t2, t3, t4, t5, t6]:
        t.start()

# ----------------- UI Classes -----------------
class SizeAnimator(QObject):
    sizeChanged = pyqtSignal(QSize)
    def animate(self, size, delay=0):
        QTimer.singleShot(delay, lambda: self.sizeChanged.emit(size))

class JarvisUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.is_listening = False
        self.size_animator = SizeAnimator()
        self.size_animator.sizeChanged.connect(self.mic_label.setFixedSize)

    def init_ui(self):
        self.setWindowTitle('Jarvis UI')
        self.setGeometry(80, 80, 400, 400)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.mic_label = QLabel(self)
        self.add_gif_to_label(
            self.mic_label,
            r"C:\Users\PRATI\Desktop\JARVIS4.1\USER_INTERFACE\d90957d7462b87ba8171fce62d2bf816.gif",
            size=(720, 220),
            alignment=Qt.AlignCenter
        )
        self.mic_label.mousePressEvent = self.start_listening

        layout = QVBoxLayout(self)
        layout.addWidget(self.mic_label, alignment=Qt.AlignCenter)

    def add_gif_to_label(self, label, gif_path, size=None, alignment=None):
        movie = QMovie(gif_path)
        label.setMovie(movie)
        self.movie = movie
        movie.start()
        if size:
            label.setFixedSize(*size)
        if alignment:
            label.setAlignment(alignment)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        label.setGraphicsEffect(shadow)

    def start_listening(self, event):
        if not self.is_listening:
            self.is_listening = True
            threading.Thread(target=jarvis).start()

# ----------------- Login Page -----------------
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jarvis Login")
        self.setGeometry(400, 200, 300, 200)

        self.layout = QVBoxLayout(self)
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Username")
        self.pass_input = QLineEdit(self)
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login", self)
        self.login_btn.clicked.connect(self.check_login)

        self.layout.addWidget(self.user_input)
        self.layout.addWidget(self.pass_input)
        self.layout.addWidget(self.login_btn)

    def check_login(self):
        username = self.user_input.text()
        password = self.pass_input.text()
        if username == "admin" and password == "1234":   # 🔑 Dummy credentials
            self.open_jarvis_ui()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid Username or Password!")

    def open_jarvis_ui(self):
        self.close()
        self.jarvis_ui = JarvisUI()
        self.jarvis_ui.showFullScreen()

# ----------------- Run App -----------------
if __name__ == "__main__":
    gui.hotkey("win", "d")
    app = QApplication([])
    login_page = LoginPage()
    login_page.show()
    app.exec_()
