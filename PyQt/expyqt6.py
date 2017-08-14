import sys
from PyQt5.QtWidgets import *
#can not run
class Example(QWidget):
    def __int__(self):
        print(3)
        super().__init__()
        print(3)
        self.initUI()

    def initUI(self):
        self.resize(250,150)
        self.center()
        print(4)
        self.setWindowTitle('center')

        self.show()

    def center(self):
        qr = self.frameGeometry()
        print(qr)
        cp = QDesktopWidget().availableGeometry().center()
        print(cp)
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    print(0)
    app = QApplication(sys.argv)
    print(1)
    ex = Example()
    print(2)
    sys.exit(app.exec_())