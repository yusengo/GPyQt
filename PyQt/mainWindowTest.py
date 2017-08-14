import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.center()
        self.setWindowTitle('hhhhhhhaaa')
        self.setWindowIcon(QIcon('../icon.jpg'))
        self.setToolTip('NIHENSHUAI')
        QToolTip.setFont(QFont('new times',12))
        menuControl = self.menuBar().addMenu('Control')
        actQuit = menuControl.addAction('quit')
        actQuit.triggered.connect(self.close)

        menuHelp = self.menuBar().addMenu('Help')
        actAbout = menuHelp.addAction('author of the software')
        actAbout.triggered.connect(self.about)
        actAboutQt = menuHelp.addAction('AboutQt')
        actAboutQt.triggered.connect(self.aboutqt)
        self.statusBar().showMessage('p has been loaded')
        self.show()

    def about(self):
        QMessageBox.about(self,'author of the software','yusengo')

    def aboutqt(self):
        QMessageBox.aboutQt(self)

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'info','r u sure to quit?',QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,(screen.height() - size.height())/2)

myapp = QApplication(sys.argv)
mainwindow = MainWindow()
#mainwindow.show()
#mainwindow.statusBar().showMessage('program is ready')
sys.exit(myapp.exec_())