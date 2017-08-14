import sys
import re
from PyQt5.QtWidgets import *
import IPFirstTest

class FindAndReplaceDlg(QDialog,IPFirstTest.Ui_Kaman):
    def __init__(self,text,parent = None):
        super(FindAndReplaceDlg,self).__init__(parent)
        self.__text = unicode(text)
        self.__index = 0
        self.setupUi(self)
        if not MAC:
            self.find_Button.setFocusPolicy(Qt.NoFocus)
            self.replace_Button.setFocusPolicy(Qt.NoFocus)
            self.OK_Button.setFocusPolicy(Qt.NoFocus)
        self.updateUi()

    def updateUi(self):
        enable = not self.findL


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    findDialog = IPFirstTest.Ui_Kaman()

    findDialog.setupUi(myMainWindow)
    myMainWindow.show()
    #findDialog.retranslateUi(findDialog)

    sys.exit(app.exec_())