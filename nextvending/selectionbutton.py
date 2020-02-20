import os
from PyQt5 import Qt, QtCore, QtGui, QtWidgets


class SelectionButton(QtWidgets.QWidget):
    def __init__(self, selection_item):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("SelectionButton")
        self.resize(225, 225)
        self.setMinimumSize(self.width(), self.height())
        self.setMaximumSize(self.width(), self.height())

        self.selection_item = selection_item
        #self.quantity_left = self.selection_item["quantity"]

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.coverLabel = QtWidgets.QLabel()
        self.coverLabel.setObjectName("coverLabel")
        self.verticalLayout.addWidget(self.coverLabel)
        
        self.nameLabel = QtWidgets.QLabel()
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel, 0, QtCore.Qt.AlignHCenter)
        
        self.priceLabel = QtWidgets.QLabel()
        self.priceLabel.setObjectName("priceLabel")
        self.verticalLayout.addWidget(self.priceLabel, 0, QtCore.Qt.AlignHCenter)

        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setBlurRadius(4)
        shadow.setColor(QtGui.QColor("#888"))
        self.setGraphicsEffect(shadow)

        self.setupButtonLabels()

    def setupButtonLabels(self):
        self.coverImage = QtGui.QPixmap(os.path.join(os.getcwd(), "nextvending", "assets", "img","logos","test.png"))
        self.coverLabel.setPixmap(self.coverImage)
        self.nameLabel.setText("ItemName")
        self.priceLabel.setText("$0.00")
