import pyautogui
import time
while True:
    pyautogui.typewrite('test. ')
    pyautogui.press('enter')
    time.sleep(.8)
    pyautogui.typewrite('I Love you. ')
    time.sleep(.8)
    pyautogui.press('enter')