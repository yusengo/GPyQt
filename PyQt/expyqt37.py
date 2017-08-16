import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,280,270)
        self.setWindowTitle('Pen Styles')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self,qp):
        pen = QPen(Qt.black,2,Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(20,200,250,200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,40,5,4])
        qp.setPen(pen)
        qp.drawLine(20,240,250,240)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())