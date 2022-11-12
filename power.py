import pyautogui as pg
import time


def power():
    name = pg.prompt(text="", title="Enter Power mode")

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
