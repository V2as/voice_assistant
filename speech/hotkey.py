import keyboard
from request import record_and_recognize


def hotkey():

    keyboard.add_hotkey('ctrl+shift+h', record_and_recognize)

