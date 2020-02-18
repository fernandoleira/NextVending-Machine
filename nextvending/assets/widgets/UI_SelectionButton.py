# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectionButton.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(238, 231)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel, 0, QtCore.Qt.AlignHCenter)
        self.priceLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.verticalLayout.addWidget(self.priceLabel, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><img src=\":/images/logos/test.png\"/></p></body></html>"))
        self.nameLabel.setText(_translate("Form", "ItemName"))
        self.priceLabel.setText(_translate("Form", "$0.00"))
import ImagesResources_rc
