#!/usr/bin/python3

"""
When fail-safe mode is True, moving the mouse to the upper-left will raise
a pyautogui.FailSafeException that can abort your program.

Docs: https://pyautogui.readthedocs.io/en/latest/mouse.html

For easy development, run python3 measurement.py in one terminal window
while working on this file. Press enter with the measurement/py window focused to
record that mouse x-y position measurement.
"""
import pyautogui, sys, time
import random
from datetime import datetime
import logging
import threading
import time
import keyboard
import os

# if you set this to true, the program won't wait for your input...
JUST_GO_MODE = True

pyautogui.FAILSAFE = True

def q():
    sys.exit()

def log(x):
    print(x)

def press_enter():
    pyautogui.press('enter')

def exit_safe_key_watcher():
    return
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('Esc'):  # if key 'q' is pressed 
            sys.exit()
    except:
        return

def double_click_wait(wait=0.2):
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(wait)

def wait_for_human_observer_to_press_enter(message):
    """
    in just go mode, we don't wait at all.... be careful
    """
    if JUST_GO_MODE:
        return
    print(message)
    print("Press enter if you want to continue...")
    
    keyboard.wait("Enter")
    print("Gotcha. Proceeding...")

def take_a_screenshot(screenshot_filename='my_screenshot.png'):
    return pyautogui.screenshot(screenshot_filename)

def click_wait(wait=0.1):
    pyautogui.click()
    time.sleep(wait)

def type_a_string(string_to_type):
    pyautogui.write(string_to_type)

def move(x, y=None):
    if y is None:
        pyautogui.moveTo( x[0] ,  x[1], duration = 0.1)
    else:
        pyautogui.moveTo( x ,  y, duration = 0.1)
    
def moveRel(x, y):
    pyautogui.moveRel(x, y, duration=0.1)


def current_timestamp_as_string():
    return str(datetime.now()).replace(':', '-').replace(' ', '-').split('.')[0]




# take a screenshot and then move to the next photo

def take_a_screenshot():
    
    x = 'screenshot-' + str(time.time()) + '.png'
    # return pyautogui.screenshot(x, region = (357, -969, 1237 - 357, -91 + 968 ))  # left top width height . (x of left two points) (y of top two points) l w
    # return pyautogui.screenshot(x, region = (825, 230, 1300, 1300 ))  # left top width height . (x of left two points) (y of top two points) l w
    return pyautogui.screenshot(x, region = (866, 220, 1400, 1400 ))  # left top width height . (x of left two points) (y of top two points) l w
    #  788   359

def next_photo():
    pyautogui.press('right')
    
def get_number_of_photos_in_folder(path):
    x = len([name for name in os.listdir(path) if os.path.isfile(name)])
    print(x)
    exit()
    return x

def screenshot_the_folder(num_photos):
    # move( 167, 862 ) # top left edge of photo when finder window is completely maximized manually by dragging each edge
    move (246,  610)
    pyautogui.click()

    num_right_arrow_presses = 0
    for i in range(num_photos):
        take_a_screenshot()
        next_photo()
        num_right_arrow_presses += 1

if __name__ == "__main__":
    # path = "/Users/zakirgowani/Desktop/FUN_FILES/TECH/neural-net-random-art/results/1"
    number_of_photos = 50
    screenshot_the_folder(number_of_photos)

    

    