import pyautogui as pg
import time


def whatsapp():

    name = pg.prompt(text="", title="Enter Name")
    task = pg.prompt(text="", title="Enter Task")
    if task == "chat":
        message = pg.prompt(text="", title="Enter message")

    pg.hotkey("ctrl", "shift", "w")
    time.sleep(4)

    # search Contact
    pg.write(name)
    time.sleep(2)
    pg.click(188, 219)
    time.sleep(2)

    ######### call ########
    if task == "audio call":
        pg.click(1770, 81)
        time.sleep(1)
    elif task == "video call":
        pg.click(1715, 89)
        time.sleep(1)
    elif task == "chat":
        pg.write(message)
        pg.press("enter")
