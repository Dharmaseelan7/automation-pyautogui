import pyautogui as pg
import time
import speech_recognition as sr
import voice


def power():
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        try:
            voice.powermain()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            time.sleep(1)
            pg.hotkey("ctrl", "esc")
            time.sleep(1)
            pg.click(1266, 957)
            time.sleep(1)
            if text == "sleep":
                pg.doubleClick(1255, 824)
            elif text == "shut down":
                pg.doubleClick(1266, 869)
            elif text == "restart":
                pg.doubleClick(1260, 903)

        except:
            name = pg.prompt(text="", title="Enter Power mode")
            if name == "":
                pg.press("ctrl")
            else:
                pg.hotkey("ctrl", "esc")
                time.sleep(1)
                pg.click(1266, 957)
                time.sleep(1)

                if name == "sleep":
                    pg.doubleClick(1255, 824)
                elif name == "shut down":
                    pg.doubleClick(1266, 869)
                elif name == "restart":
                    pg.doubleClick(1260, 903)
