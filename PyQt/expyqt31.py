import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('ubuntu',self)

        combo = QComboBox(self)
        combo.addItem('ubuntu')
        combo.addItem('mandriva')
        combo.addItem('fedora')
        combo.addItem('arch')
        combo.addItem('gentoo')

        combo.move(50,50)
        self.lbl.move(50,150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())