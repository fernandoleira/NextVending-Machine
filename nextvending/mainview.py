from PyQt5 import QtCore, QtGui, QtWidgets

from mailclient import MailClient
from paymentwidget import PaymentWidget
from selectionwidget import SelectionWidget

class MainViewSignals(QtCore.QObject):
    log = QtCore.pyqtSignal(dict)

class MainView(QtWidgets.QWidget):
    def __init__(self, conf, products):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("MainView")
        self.signals = MainViewSignals()

        self._conf = conf
        self._products = products

        self.mail_client = MailClient(self._conf)

        self.balance = self._conf["TRANSACTIONS_DATA"]["CURRENT_BALANCE"]

        self.paymentWidget = PaymentWidget()
        self.selectionWidget = SelectionWidget(self._products, self.balance)

        self.selectionWidget.signals.new_purchase.connect(self.new_purchase_event)

        self._init_layout()

    def _init_layout(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        
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

    def transactions_to_balance(self, new_transactions):
        for transaction in new_transactions:
            self.balance += transaction["amount"]
        
        self.balanceLabel.setText("${:0.2f}".format(self.balance))
        self.selectionWidget.update_balance(self.balance)

    # ============================== SLOTS ==============================
    @QtCore.pyqtSlot()
    def change_window(self):
        if self.centralWidgets.currentIndex() == 0:
            print("Trying to connect to mail server...")
            status = self.mail_client.open_mail_connection()
            print(status[1])
            if status[0]:
                self.centralWidgets.setCurrentWidget(self.paymentWidget)
            else:
                exit()

        else:
            print("Reading last transactions...")
            transaction_req = self.mail_client.get_last_transactions()
            if transaction_req[0] and len(transaction_req[1]) > 0:
                self.transactions_to_balance(transaction_req[1])
            else:
                if transaction_req[0] == 0:
                    print(transaction_req[1])

            print("Closing connection with mail server...")
            self.mail_client.close_mail_connection()

            self.centralWidgets.setCurrentWidget(self.selectionWidget)

    @QtCore.pyqtSlot(dict)
    def new_purchase_event(self, purchase_info):
        self.balance -= purchase_info['price']
        self.balanceLabel.setText("${:0.2f}".format(self.balance))
        self.selectionWidget.update_balance(self.balance)
        
