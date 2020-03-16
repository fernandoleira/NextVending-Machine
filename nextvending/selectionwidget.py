import os
from PyQt5 import QtCore, QtGui, QtWidgets

from selectionbutton import SelectionButton

class SelectionSignals(QtCore.QObject):
    purchase_signal = QtCore.pyqtSignal(float) 

class SelectionWidget(QtWidgets.QWidget):
    def __init__(self, products, current_balance):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("SelectionWidget")

        self.signals = SelectionSignals()
        self.current_balance = 0

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

        self.update_balance(current_balance)
        self.connect_button_signals()
        

    def connect_button_signals(self):
        self.selectButton_1.signals.purchase_request.connect(self.send_new_purchase)
        self.selectButton_2.signals.purchase_request.connect(self.send_new_purchase)
        self.selectButton_3.signals.purchase_request.connect(self.send_new_purchase)
        self.selectButton_4.signals.purchase_request.connect(self.send_new_purchase)

    def update_balance(self, new_balance):
        self.current_balance = new_balance
        self.selectButton_1.check_price_available(self.current_balance)
        self.selectButton_2.check_price_available(self.current_balance)
        self.selectButton_3.check_price_available(self.current_balance)
        self.selectButton_4.check_price_available(self.current_balance)

    @QtCore.pyqtSlot(float)
    def send_new_purchase(self, purchase_price):
        self.signals.purchase_signal.emit(purchase_price)