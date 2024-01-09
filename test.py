import pyautogui
import time

time.sleep(1)

def hold_W (hold_time):
    import time, pyautogui
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.press('w')

hold_W(1)