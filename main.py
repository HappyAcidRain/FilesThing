import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import mainUI


class MainWindow(QMainWindow): #mainUI.Ui_MainWindow
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
    def getList(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec())