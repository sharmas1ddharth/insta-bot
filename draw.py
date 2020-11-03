import pyautogui, time

time.sleep(5)

distance = 100

while distance > 0:
    pyautogui.drag(distance, 1, duration=0.5)
    distance -=7
    pyautogui.drag(2, distance, duration=0.5)
    pyautogui.drag(-distance, 3, duration=0.5)
    distance -= 7
    pyautogui.drag(4, -distance, duration=0.5)