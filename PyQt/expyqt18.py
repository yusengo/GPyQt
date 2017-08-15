import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.MyFun)
        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self,event):
        self.c.closeApp.emit()

    def MyFun(self):
        self.statusBar().showMessage('r u ok')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())