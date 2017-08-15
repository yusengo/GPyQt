import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit  = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('./icon/fire'),'Exit',self)
        exitAction.setShortcut('Alt+Q')
        exitAction.setStatusTip('Exit App')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('XiaoZhuGe')
        self.setWindowIcon(QIcon('./icon/wings'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())