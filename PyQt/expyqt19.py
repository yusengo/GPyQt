import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('input dialog')
        self.show()

    def showDialog(self):
        text,ok = QInputDialog.getText(self,'input dialog','enter your name')
        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())