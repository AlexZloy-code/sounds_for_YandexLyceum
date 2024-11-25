import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtMultimedia


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.btns = [self.pushButton,
                self.pushButton_2,
                self.pushButton_3,
                self.pushButton_4,
                self.pushButton_5,
                self.pushButton_6,
                self.pushButton_7,
                self.pushButton_8,
                self.pushButton_9,
                self.pushButton_10,
                self.pushButton_11,
                self.pushButton_12
               ]
        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(self.run)

    
    def play_sound_11(self, inx):
        notes_file = ['do.mp3', 'do#.mp3', 're.mp3', 're#.mp3', 'mi.mp3', 'fa.mp3', 'fa#.mp3', 'sol.mp3', 'sol#.mp3', 'lya.mp3', 'lya#.mp3', 'si.mp3']
        
        filename = notes_file[inx]
        media = QtCore.QUrl.fromLocalFile(filename)
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player = QtMultimedia.QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        if '#' in filename:
            self._audio_output.setVolume(1)
        else:
            self._audio_output.setVolume(50)
        self._player.setSource(media)
        self._player.play()


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_A:
            inx = 0
        elif event.key() == QtCore.Qt.Key.Key_W:
            inx = 1
        elif event.key() == QtCore.Qt.Key.Key_S:
            inx = 2
        elif event.key() == QtCore.Qt.Key.Key_E:
            inx = 3
        elif event.key() == QtCore.Qt.Key.Key_D:
            inx = 4
        elif event.key() == QtCore.Qt.Key.Key_F:
            inx = 5
        elif event.key() == QtCore.Qt.Key.Key_T:
            inx = 6
        elif event.key() == QtCore.Qt.Key.Key_G:
            inx = 7
        elif event.key() == QtCore.Qt.Key.Key_Y:
            inx = 8
        elif event.key() == QtCore.Qt.Key.Key_H:
            inx = 9
        elif event.key() == QtCore.Qt.Key.Key_U:
            inx = 10
        elif event.key() == QtCore.Qt.Key.Key_J:
            inx = 11
        else:
            return
        self.play_sound_11(inx)


    def run(self):
        notes = ['До', 'До#', 'Ре', 'Ре#', 'Ми', 'Фа', 'Фа#', 'Соль', 'Соль#', 'Ля', 'Ля#', 'Си']
        self.play_sound_11(notes.index(self.sender().text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())