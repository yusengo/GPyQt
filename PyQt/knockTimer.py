import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import IPFirstTest

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    findDialog = IPFirstTest.Ui_Kaman()

    findDialog.setupUi(myMainWindow)
    myMainWindow.show()
    #findDialog.retranslateUi(findDialog)

    sys.exit(app.exec_())