from PyQt5 import QtCore, QtGui, QtWidgets


class PaymentWidget(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setObjectName("PaymentWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.QRCode = QtWidgets.QGraphicsView()
        self.QRCode.setStyleSheet("background-image: url(nextvending/assets/img/venmo.jpg);")
        self.QRCode.setObjectName("QRCode")
        self.verticalLayout.addWidget(self.QRCode)
        self.setLayout(self.verticalLayout)
