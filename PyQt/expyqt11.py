import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('nidaye1',self)
        label1.move(15,10)

        label2 = QLabel('AHHHAA2',self)
        label2.move(35,40)

        label3 = QLabel('adadfa3',self)
        label3.move(55,70)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('绝对')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())