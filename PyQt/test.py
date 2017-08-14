import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,800,600)
        self.setWindowTitle('woshiahhh')
        self.setWindowIcon(QIcon('../icon.jpg'))
        self.setToolTip('不要说话')
        QToolTip.setFont(QFont('幼圆',22))

def closeEvent(self,event):
    replay = QMessageBox.question(self,'信息','are u sure?',QMessageBox.Yes,QMessageBox.No)
    if replay == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()

def center(self):
    screen = QDesktopWidget().screenGeometry()
    size = self.geometry()
    self.move((screen.width() - size.width())/2,(screen.height() - size.height())/2)

testone = QApplication(sys.argv)
testwidget = MyWidget()
screen1 = QDesktopWidget().screenGeometry()
testwidget.show()
#closeEvent(testwidget,testwidget.close())
center(testwidget)
testwidget.resize(screen1.width(),screen1.height())
sys.exit(testone.exec_())