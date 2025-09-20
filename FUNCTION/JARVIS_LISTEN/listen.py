import speech_recognition as sr
import os
import threading
from deep_translator import GoogleTranslator
from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.LIGHTBLUE_EX + "I am Listening...",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)

def Trans_hindi_to_english(txt):
    t = GoogleTranslator(
        source="auto",
        target="en"
    )
    tr_word = t.translate(txt)
    return tr_word


def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 220
    recognizer.dynamic_energy_adjustment_damping = 0.05
    recognizer.dynamic_energy_ratio = 1.5
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.3
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTBLUE_EX +"I am Listening...",end="",flush=True)
            try:
                audio = recognizer.listen(source,timeout=None)
                print("\r"+Fore.LIGHTYELLOW_EX + "Got it ,Now Recognizing..",end="",flush=True)
                recognized_txt = recognizer.recognize_google(audio, language="hi-IN")

                if recognized_txt:
                    translated_txt = Trans_hindi_to_english(recognized_txt)
                    print("\r"+Fore.BLUE + "Pratibh Nishad :" + translated_txt)
                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt =  ""
            finally:
                print("\r",end="",flush=True)

        os.system("cls"  if os.name == "nt" else "clear")
        #threading part
        listen_thread = threading.Thread(target=listen)
        print_thread = threading.Thread(target=print_loop)
        listen_thread.start()
        print_thread.start()


def hearing():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 220
    recognizer.dynamic_energy_adjustment_damping = 0.05
    recognizer.dynamic_energy_ratio = 1.5
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.3
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone(device_index=9) as source:

        recognizer.adjust_for_ambient_noise(source)
        while True:

            try:
                audio = recognizer.listen(source,timeout=None)

                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    translated_txt = Trans_hindi_to_english(recognized_txt)

                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt =  ""
            finally:
              print("\r",end="",flush=True)
