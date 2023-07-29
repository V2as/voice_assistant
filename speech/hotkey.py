import keyboard
from request import record_and_recognize


def hotkey():

    keyboard.add_hotkey('ctrl+shift', record_and_recognize)

