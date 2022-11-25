import pyautogui as pg
import time
import speech_recognition as sr
import voice
import keyboard as key


def makecall():

    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        try:
            voice.callmain()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            pg.hotkey("ctrl", "shift", "w")
            time.sleep(4)
            pg.click(142, 148)
            pg.write(text)
            time.sleep(2)
            pg.click(188, 219)
            time.sleep(2)
            pg.click(1770, 81)
            time.sleep(1)
        except:
            name = pg.prompt(text="", title="Enter Name")
            if name == "":
                pg.press("ctrl")
            else:
                pg.hotkey("ctrl", "shift", "w")
                time.sleep(4)
                pg.click(142, 148)
                pg.write(name)
                time.sleep(2)
                pg.click(188, 219)
                time.sleep(2)
                pg.click(1770, 81)
                time.sleep(1)
