from responce import record_audio, recognize_speech, activate_sound
from functools import lru_cache
from text2num import convert_text_to_number
import numpy as np
import pyautogui
import pyperclip
import webbrowser
import gc
import os

def record_and_recognize():
    '''
    Модуль обработки звукового сигнала и распознавания речи

    :return: None
    '''
    try:
        open_commands(recognize_speech(record_audio()))
        gc.collect()
        lru_cache(maxsize=None)

    except Exception as e:
        activate_sound('data/errorwave.wav')
        print(e)

def open_commands(sentence):
    '''
    Модуль обработки запросов предложения сформированного голосом
    :param sentence: предложение
    :return: None
    '''

    with open('data/abbrs.txt', 'r', encoding='utf-8') as f:
        command = f.read().rstrip().replace('\n', '\t').split('\t')

    if sentence.split(' ')[0] == 'напиши':
        pyperclip.copy(' '.join(sentence.split(' ')[1:]))

        if pyautogui.onScreen(pyautogui.position()):
            pyautogui.hotkey('ctrl', 'v')

    elif 'заверши сеанс' in sentence or 'завершить сеанс' in sentence:
        os.system(
            f'shutdown /s /t {int(convert_text_to_number(" ".join(sentence[sentence.find("через") + len("через") + 1:sentence.find("минут") - 1].split(" ")))) * 60}')

    elif 'найди' in sentence:
        url = f"https://www.google.com/search?q={' '.join(sentence[sentence.find('найди') + len('найди') + 1:].split(' '))}"
        webbrowser.open_new_tab(url)

    elif list(set(command).intersection(set(sentence.split()))) != []:
        words = np.array([0]*len(list(set(command).intersection(set(sentence.split())))), dtype=tuple)

        for i, word in enumerate(list(set(command).intersection(set(sentence.split())))):
            words[i] = (command.index(word), word)

        if len(list(set(command).intersection(set(sentence.split())))) == 1:
            promt = command[words[0][0]+1]

        else:
            promt = command[command.index(words[1][1], words[0][0])+1]

            if len(promt.split(' ')) == 1:
                promt = command[command.index(words[0][1], words[1][0]) + 1]

        if promt.split(' ')[0] == 'str':
            os.system(f"{' '.join(promt.split(' ')[1:])}")

        elif promt.split(' ')[0] == 'htk':
            pyautogui.hotkey(f"{promt.split(' ')[1]}", f"{promt.split(' ')[2]}")

        elif promt.split(' ')[0] == 'web':
            webbrowser.open_new_tab(' '.join(promt.split(' ')[1:]))


    else: activate_sound('data/errorwave.wav')