import pyautogui as p
from time import sleep
a = int(input('no. of times you want to send:\n'))
b = input('\n message you want to send:\n')
sleep(3)

for i in range(a):
    p.typewrite(b)
    p.press('enter')
    sleep(1)
