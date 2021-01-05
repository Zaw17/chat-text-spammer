import pyautogui, time
import os


dir_path = os.path.dirname(os.path.realpath(__file__))

print("What text would you like to spam")

f = open(dir_path + "/" + input("File that's in the same folder as this program:") + ".txt",'r')

time.sleep(10)

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('return')

