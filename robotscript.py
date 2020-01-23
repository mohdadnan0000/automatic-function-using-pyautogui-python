import pyautogui
import time
pyautogui.click(856,51)
pyautogui.click(856,51)
pyautogui.typewrite(['backspace'])
time.sleep(2)
for i in range(1,11):
    string=str(i)
    pyautogui.typewrite(string)
    time.sleep(2)
    pyautogui.typewrite(['enter'])
    time.sleep(5)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    pyautogui.typewrite(['backspace'])
    string='N-'+string
    pyautogui.typewrite(string)
    time.sleep(2)
    pyautogui.typewrite(['enter'])
    time.sleep(2)
    pyautogui.click(856,51)
    pyautogui.click(856,51)
    pyautogui.typewrite(['backspace'])
    #pyautogui.typewrite(['backspace'])
    time.sleep(2)

 #n ka 88

