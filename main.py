import pyautogui as pg
import time
import whatsapp
import power
import spotify
import speech_recognition as sr
import voice
import call


def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        try:
            voice.mainmain()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            l = text.split()

            if "whatsapp" in l:
                whatsapp.whatsapp()
            elif "power" in l:
                power.power()
            elif "spotify" in l:
                spotify.song()
            elif "call" in l:
                text = l[1]
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
            name = pg.prompt(text="", title="App Manager")
            if name == "":
                pg.press("ctrl")
            else:
                if name == "whatsapp":
                    whatsapp.whatsapp()
                elif name == "power":
                    power.power()
                elif name == "spotify":
                    spotify.song()


main()
