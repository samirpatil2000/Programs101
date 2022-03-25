import pyautogui as pg

import time 

time.sleep(1000)

for _ in range(10):
    pg.write("Hey testing PYAUTOGUI")
    pg.press('enter')