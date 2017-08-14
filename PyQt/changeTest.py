import sys
import urllib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

class Form(QDialog):
    def __init__(self,parent = None):
        super().__init__(parent)
        print(111)
        #date = self.getdata()
        rates = sorted(self.rates.keys())

        #dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01,1000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(self.fromComboBox,0,0)
        grid.addWidget(self.fromComboBox,1,0)
        grid.addWidget(self.fromSpinBox,1,1)
        grid.addWidget(self.toComboBox,2,0)
        grid.addWidget(self.toLabel,2,1)
        self.setLayout(grid)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    findDialog = Form()

    findDialog.show()

    sys.exit(app.exec_())

