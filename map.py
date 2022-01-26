import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
form_class = uic.loadUiType("map.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec()