import pyautogui as pg
import time
import whatsapp
import power
import spotify
name = pg.prompt(text="", title="App Manager")


def main():

    if name == "whatsapp":
        whatsapp.whatsapp()
    elif name == "power":
        power.power()
    elif name == "spotify":
        spotify.song()


main()
