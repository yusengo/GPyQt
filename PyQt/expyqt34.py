import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = u'\u041b\u0435\u0432\u041d\u0438\u043a'

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Draw text')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        qp.end()

    def drawText(self,event,qp):
        qp.setPen(QColor(168,34,3))
        qp.setFont(QFont('Decorative',10))
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())