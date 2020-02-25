from PyQt5 import QtCore, QtGui, QtWidgets

from paymentwidget import PaymentWidget
from selectionwidget import SelectionWidget


class MainView(QtWidgets.QWidget):
    def __init__(self, conf, products):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("MainView")

        self._conf = conf
        self._products = products

        self.balance = self._conf["VENDING_DATA"]["CURRENT_BALANCE"]

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.paymentWidget = PaymentWidget()

        self.selectionWidget = SelectionWidget(self._products, self.balance)
        self.selectionWidget.signals.purchase_signal.connect(self.new_purchase_signal)

        self.centralWidgets = QtWidgets.QStackedWidget()
        self.centralWidgets.setObjectName("centralWidgets")
        self.centralWidgets.addWidget(self.selectionWidget)
        self.centralWidgets.addWidget(self.paymentWidget)
        self.verticalLayout.addWidget(self.centralWidgets)

        self.balanceLabel = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.balanceLabel.sizePolicy().hasHeightForWidth())
        self.balanceLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.balanceLabel.setObjectName("balanceLabel")
        self.balanceLabel.setText("${:0.2f}".format(self.balance))
        self.verticalLayout.addWidget(self.balanceLabel)

        self.controlButton = QtWidgets.QPushButton()
        self.controlButton.setMaximumWidth(self.width() * 0.75)
        self.controlButton.setObjectName("ControlButton")
        self.controlButton.setText("Check Payment")
        self.controlButton.clicked.connect(self.change_window)
        self.verticalLayout.addWidget(self.controlButton)

    # ============================== SLOTS ==============================
    @QtCore.pyqtSlot()
    def change_window(self):
        if self.centralWidgets.currentIndex() == 0:
            self.centralWidgets.setCurrentWidget(self.paymentWidget)
        else:
            self.centralWidgets.setCurrentWidget(self.selectionWidget)

    @QtCore.pyqtSlot(float)
    def new_purchase_signal(self, purchase_price):
        self.balance -= purchase_price
        self.balanceLabel.setText("${:0.2f}".format(self.balance))
        self.selectionWidget.update_balance(self.balance)
        
