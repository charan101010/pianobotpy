from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:  429 Y:  700 RGB: ( 77,  80, 115)
#Tile 2 Position: X:  551 Y:  700 RGB: (  0,   0,   0)
#Tile 3 Position: X:  686 Y:  700 RGB: ( 79,  82, 116)
#Tile 4 Position: X:  813 Y:  700 RGB: ( 80,  83, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(429, 700)[0] == 0:
        click(429, 700)
    if pyautogui.pixel(551, 700)[0] == 0:
        click(551, 700)
    if pyautogui.pixel(686, 700)[0] == 0:
        click(686, 700)
    if pyautogui.pixel(813, 700)[0] == 0:
        click(813, 700)
