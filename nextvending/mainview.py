from PyQt5 import QtCore, QtGui, QtWidgets

from paymentwidget import PaymentWidget
from selectionwidget import SelectionWidget


class MainView(QtWidgets.QWidget):
    def __init__(self, conf, products):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("MainView")

        self._conf = conf
        self._products = products

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.titleLabel = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("TitleLabel")
        self.titleLabel.setText("Select Item")
        self.verticalLayout.addWidget(self.titleLabel)

        self.paymentWidget = PaymentWidget()
        self.selectionWidget = SelectionWidget(self._products)

        self.centralWidgets = QtWidgets.QStackedWidget()
        self.centralWidgets.setObjectName("centralWidgets")
        self.centralWidgets.addWidget(self.selectionWidget)
        self.centralWidgets.addWidget(self.paymentWidget)
        self.verticalLayout.addWidget(self.centralWidgets)

        self.balanceLabel = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.balanceLabel.sizePolicy().hasHeightForWidth())
        self.balanceLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(28)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.balanceLabel.setObjectName("balanceLabel")
        self.balanceLabel.setText("$0.00")
        self.verticalLayout.addWidget(self.balanceLabel)

        self.controlButton = QtWidgets.QPushButton()
        self.controlButton.setObjectName("ControlButton")
        self.controlButton.setText("Check Payment")
        self.controlButton.clicked.connect(self.change_window)
        self.verticalLayout.addWidget(self.controlButton)

    #============================== SLOTS ==============================

    @QtCore.pyqtSlot()
    def change_window(self):
        if self.centralWidgets.currentIndex() == 0:
            self.titleLabel.setText("Add funds")
            self.centralWidgets.setCurrentWidget(self.paymentWidget)
        else:
            self.titleLabel.setText("Select Item")
            self.centralWidgets.setCurrentWidget(self.selectionWidget)