import pyautogui, time

time.sleep(5)

f = open("rapgod.txt", "r")

for word in f:
    pyautogui.write(word)
    pyautogui.press("enter")
    