# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(557, 561)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.selectButton_1 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_1.sizePolicy().hasHeightForWidth())
        self.selectButton_1.setSizePolicy(sizePolicy)
        self.selectButton_1.setObjectName("selectButton_1")
        self.gridLayout.addWidget(self.selectButton_1, 0, 0, 1, 1)
        self.selectButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_2.sizePolicy().hasHeightForWidth())
        self.selectButton_2.setSizePolicy(sizePolicy)
        self.selectButton_2.setObjectName("selectButton_2")
        self.gridLayout.addWidget(self.selectButton_2, 0, 1, 1, 1)
        self.selectButton_3 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_3.sizePolicy().hasHeightForWidth())
        self.selectButton_3.setSizePolicy(sizePolicy)
        self.selectButton_3.setObjectName("selectButton_3")
        self.gridLayout.addWidget(self.selectButton_3, 1, 0, 1, 1)
        self.selectButton_4 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_4.sizePolicy().hasHeightForWidth())
        self.selectButton_4.setSizePolicy(sizePolicy)
        self.selectButton_4.setObjectName("selectButton_4")
        self.gridLayout.addWidget(self.selectButton_4, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.selectButton_1.setText(_translate("Form", "Select1"))
        self.selectButton_2.setText(_translate("Form", "Select2"))
        self.selectButton_3.setText(_translate("Form", "Select3"))
        self.selectButton_4.setText(_translate("Form", "Select4"))
