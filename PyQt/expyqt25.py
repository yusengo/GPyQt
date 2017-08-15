import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('./icon/fire'))
        self.label.setGeometry(160,40,400,400)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self,value):
        if value == 0:
            self.label.setPixmap(QPixmap('./icon/fire'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('./icon/wings'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('./icon/setting'))
        else:
            self.label.setPixmap(QPixmap('./icon/icon'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())