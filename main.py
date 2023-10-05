import pyautogui
from pynput import keyboard
from form import show_form
import time

COMBINATION = {keyboard.Key.shift, keyboard.Key.cmd, keyboard.Key.space}

current_keys = set()


def copy_to_clipboard_and_show_form():
    time.sleep(0.1)
    pyautogui.typewrite('"+y')
    time.sleep(0.2)
    show_form()


def on_press(key):
    if key in COMBINATION:
        current_keys.add(key)


def on_release(key):
    if key in COMBINATION and key in current_keys:
        if all(k in current_keys for k in COMBINATION):
            copy_to_clipboard_and_show_form()
        current_keys.remove(key)


# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
