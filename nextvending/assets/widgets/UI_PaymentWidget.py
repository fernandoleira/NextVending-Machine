# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaymentWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_paymentForm(object):
    def setupUi(self, paymentForm):
        paymentForm.setObjectName("paymentForm")
        paymentForm.resize(355, 464)
        self.verticalLayout = QtWidgets.QVBoxLayout(paymentForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QRCode = QtWidgets.QGraphicsView(paymentForm)
        self.QRCode.setStyleSheet("background-image: url(:/images/venmo.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;")
        self.QRCode.setObjectName("QRCode")
        self.verticalLayout.addWidget(self.QRCode)
        self.CheckPayment = QtWidgets.QPushButton(paymentForm)
        self.CheckPayment.setObjectName("CheckPayment")
        self.verticalLayout.addWidget(self.CheckPayment)

        self.retranslateUi(paymentForm)
        QtCore.QMetaObject.connectSlotsByName(paymentForm)

    def retranslateUi(self, paymentForm):
        _translate = QtCore.QCoreApplication.translate
        paymentForm.setWindowTitle(_translate("paymentForm", "Form"))
        self.QRCode.setToolTip(_translate("paymentForm", "<html><head/><body><p><br/></p></body></html>"))
        self.CheckPayment.setText(_translate("paymentForm", "Check Payment"))
import ImagesResources_rc
