import pyautogui

width, height = pyautogui.size()

pyautogui.moveTo(1844, 84, duration=2)

pyautogui.typewrite('Hello world', interval=0.2)

