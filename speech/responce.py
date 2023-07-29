import vosk
import wave
import json
import pyaudio
import io
import time
import audioop

model = vosk.Model("model/vosk-model-small-ru-0.22") # Загрузка модели для распознавания речи
rec = vosk.KaldiRecognizer(model, 16000) # Создание объекта распознавания

def activate_sound(filename):
    '''
    Функция воспроизводит любой файл в формате wave
    :param filename: файл в формате wave
    :return: None
    '''
    with wave.open(filename, 'rb') as wav_file:
        p = pyaudio.PyAudio() # Создать экземпляр PyAudio
        chunk = 1024
        stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                            channels=wav_file.getnchannels(),
                            rate=wav_file.getframerate(),
                            output=True) # Открыть поток для воспроизведения
        data = wav_file.readframes(chunk) # Читать и воспроизводить данные из файла пакетами

        while data:
            stream.write(data)
            data = wav_file.readframes(chunk)

        stream.stop_stream() # Завершить воспроизведение
        stream.close()
        p.terminate() # Закрыть экземпляр PyAudio

def record_audio():
    '''
    Функция записывает голос с помощью библиотеки pyaudio, параметры настроены под все виды микрофонов.
    Содержит условие: если 2 секунды средняя громкость микрофона ниже громкости "тишины", то микрофон отключится

    :return: Файл формата wave из оперативной памяти
    '''
    global TOTAL_START

    TOTAL_START = time.time()
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 10
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    frames = []
    s = 0

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        frames.append(data)

        if rms < 80:
            s += 1
            if s == 15:
                break

        else: s = 0


    stream.stop_stream()
    stream.close()
    p.terminate()
    output = io.BytesIO()

    with wave.open(output, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    data = output.getvalue()
    wf = wave.open(io.BytesIO(data), "rb")

    return wf

def recognize_speech(wf):
    '''
    В качестве модуля распознавания используется Alpha Cephei vosk
     ⌊документация https://alphacephei.com/vosk/

    :param wf: Аудиофайл в формате wave или записанный голос из оперативной памяти
    :return: str <Распознанный голос> или str <None>
    '''
    sentence = 'None'

    while True:
        data = wf.readframes(4000)

        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            sentence = result['text']

    final_result = json.loads(rec.FinalResult())

    if sentence == '' or sentence == 'None':
        return final_result['text']
    else: return sentence



