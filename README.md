# VOSK Voice Offline Windows Assistant

(Временно!)Поддержка только на русском языке
## Как использовать?
### Установка необходимых библиотек
```bash
pip install requierements.txt
```
### Включение голосового помощника
```bash
python __main__.py
```
После чего появится иконка в трее, зажмите shift+ctrl и говорите
## Функционал 
- Для написания сообщения скажите "Напиши <ПРЕДЛОЖЕНИЕ>"
- Для управления программами скажите "Открой <ПРИЛОЖЕНИЕ>" или аналогично "Закрой это окно"
- Скажите "Заверши сеанс через <ВРЕМЯ>" чтобы задать таймер завершения
- Для управления браузером скажите "Новая страница" или "Открой <САЙТ>"
- "Найди <ПРЕДЛОЖЕНИЕ>" и включится поиск в Google
- Управление громкостью "Сделай тише на <ЗНАЧЕНИЕ>"
## Команды 
Команды прописаны в строку, в data/abbrs.txt
### Пример построения команды
```bash
наименование\tкоманды\tтип(формат: три буквы, например htk) код выполнения (через пробел)
```
Команды(расширяемо):
- str, выполняемые системные утилиты через cmd start
- cmd, выаолняемые системные команды через cmd
- htm, hotkey сочетания клавиш
- pro, установленные программы
- web, веб ресусры, ссылки
