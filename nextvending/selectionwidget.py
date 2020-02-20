import os
from PyQt5 import QtCore, QtGui, QtWidgets

from selectionbutton import SelectionButton


class SelectionWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("SelectionWidget")
        self.resize(557, 561)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.selectButton_1 = SelectionButton({})
        self.gridLayout.addWidget(self.selectButton_1, 0, 0, 1, 1)

        self.selectButton_2 = SelectionButton({})
        self.gridLayout.addWidget(self.selectButton_2, 0, 1, 1, 1)

        self.selectButton_3 = SelectionButton({})
        self.gridLayout.addWidget(self.selectButton_3, 1, 0, 1, 1)

        self.selectButton_4 = SelectionButton({})
        self.gridLayout.addWidget(self.selectButton_4, 1, 1, 1, 1)
        
