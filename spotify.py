import pyautogui as pg
import time
import speech_recognition as sr
import voice


def song():

    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:

        try:
            voice.spotifymain()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            time.sleep(1)

            pg.hotkey("ctrl", "shift", "s")

            time.sleep(9)

            # search icon
            pg.click(95, 129)
            time.sleep(2)
            pg.write(text)
            time.sleep(3)
            if text == "my play":
                pg.click(774, 487)
            else:
                pg.click(904, 288)

        except:
            name = pg.prompt(text="", title="Enter song name")
            if name == "":
                pg.press("ctrl")
            else:
                pg.hotkey("ctrl", "shift", "s")
                time.sleep(9)

                # search icon
                pg.click(95, 129)
                time.sleep(2)
                pg.write(name)
                time.sleep(3)
                if name == "my play":
                    pg.click(774, 487)
                else:
                    pg.click(904, 288)
