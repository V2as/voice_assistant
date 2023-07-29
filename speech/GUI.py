import sys
from PyQt5 import QtWidgets, QtGui
import gc

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    '''
    Класс Qt для иконки в трее. При нажатии на иконку имеет выпадающее меню с функцией "выйти".
    '''
    def __init__(self, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, parent)
        self.setIcon(QtGui.QIcon("data/scaled-cat.ico"))  # Путь к иконке в трее
        self.setToolTip("Cat-helper") # Подсказка при наведении на иконку
        self.menu = QtWidgets.QMenu(parent) # Создаем контекстное меню
        exit_action = self.menu.addAction("Exit:)")
        exit_action.triggered.connect(self.exit)
        self.setContextMenu(self.menu) # Устанавливаем контекстное меню

    def exit(self):
        QtWidgets.qApp.quit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    tray_icon = SystemTrayIcon() # Создаем объект иконки в трее
    tray_icon.show()
    gc.collect()
    sys.exit(app.exec_())


