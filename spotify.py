import pyautogui as pg
import time


def song():
    name = pg.prompt(text="", title="Enter song name")
    pg.hotkey("ctrl", "shift", "s")
    time.sleep(6)

    # search icon
    pg.click(95, 129)
    time.sleep(1)
    pg.write(name)
    time.sleep(3)
    if name == "my playlist":
        pg.click(774, 487)
    else:
        pg.click(904, 288)
