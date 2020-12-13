from pydub import AudioSegment
import sys
import os
from subprocess import Popen

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QMainWindow, QDialog, QLineEdit, QPushButton, QStatusBar, QWidget, QAction, QKeySequenceEdit, QMenuBar, QMenu, QSizePolicy, QDesktopWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PySide2.QtGui import QIcon, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title = 'MP3Convert'
        self.width = 300
        self.height = 250
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('img/logo.png'))
        self.display()
    
    def display(self):
        choosefolder = QPushButton('choose file...', self)
        choosefolder.resize(100,32)
        choosefolder.move(150, 50)

        text1 = QTextEdit('', self)
        text1.move(50, 50)

        self.convert = QPushButton('convert', self)
        self.convert.resize(100,32)
        self.convert.move(150, 120)
        self.converttomp3 = QAction( QIcon('img/csv.png'), 'csv', self, statusTip="file..", triggered=self.convertmp3())

        text2 = QTextEdit('newname', self)
        text2.move(50, 120)

        return text1, text2
    
    def convertmp3(self):
        wav_audio = AudioSegment.from_file("noah.mp4", format="mp4")
        wav_audio.export("output4.mp3", format="mp3")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())