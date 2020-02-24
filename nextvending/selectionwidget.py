import os
from PyQt5 import QtCore, QtGui, QtWidgets

from selectionbutton import SelectionButton


class SelectionWidget(QtWidgets.QWidget):
    def __init__(self, products):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("SelectionWidget")

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.selectButton_1 = SelectionButton(products["PRODUCT_1"])
        self.gridLayout.addWidget(self.selectButton_1, 0, 0, 1, 1)

        self.selectButton_2 = SelectionButton(products["PRODUCT_2"])
        self.gridLayout.addWidget(self.selectButton_2, 0, 1, 1, 1)

        self.selectButton_3 = SelectionButton(products["PRODUCT_3"])
        self.gridLayout.addWidget(self.selectButton_3, 1, 0, 1, 1)

        self.selectButton_4 = SelectionButton(products["PRODUCT_4"])
        self.gridLayout.addWidget(self.selectButton_4, 1, 1, 1, 1)
        