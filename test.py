import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("widget.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 버튼에 기능 연결
        self.btn1.clicked.connect(self.btn1Function)

        # 라디오버튼 연결
        self.radio1.clicked.connect(self.radioFunction)
        self.radio2.clicked.connect(self.radioFunction)
        self.radio3.clicked.connect(self.radioFunction)
        
        # 체크박스 연결
        self.checkBox1.stateChanged.connect(self.checkFunction)
        self.checkBox2.stateChanged.connect(self.checkFunction)
        self.checkBox2.stateChanged.connect(self.checkFunction)


    def btn1Function(self):
        print("버튼1 클릭")

    def radioFunction(self):
        if self.radio1.isChecked() : print("라디오버튼1 클릭")
        elif self.radio2.isChecked() : print("라디오버튼2 클릭")
        elif self.radio3.isChecked() : print("라디오버튼2 클릭")
        
    def checkFunction(self):
        if self.checkBox1.isChecked() : print("체크박스1 클릭")
        if self.checkBox2.isChecked() : print("체크박스2 클릭")
        if self.checkBox3.isChecked() : print("체크박스3 클릭")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec()