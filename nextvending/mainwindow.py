from PyQt5 import QtCore, QtGui, QtWidgets

from paymentwidget import PaymentWidget
from selectionwidget import SelectionWidget

class MainWindow(QtWidgets.QWidget):
    def __init__(self, config_paths, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setObjectName("MainWindow")
        self.setWindowTitle("NextVending")
        self.resize(500, 750)

        self.config_paths = config_paths

        # Add shorcut actions
        self.add_window_actions()

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.TitleLabel = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.TitleLabel.setText("Select Item")
        self.verticalLayout.addWidget(self.TitleLabel)

        self.paymentWidget = PaymentWidget()
        self.selectionWidget = SelectionWidget()

        self.centralWidgets = QtWidgets.QStackedWidget()
        self.centralWidgets.setObjectName("centralWidgets")
        self.centralWidgets.addWidget(self.selectionWidget)
        self.centralWidgets.addWidget(self.paymentWidget)
        self.verticalLayout.addWidget(self.centralWidgets)

        self.controlButton = QtWidgets.QPushButton()
        self.controlButton.setObjectName("ControlButton")
        self.controlButton.setText("Check Payment")
        self.controlButton.clicked.connect(self.change_window)
        self.verticalLayout.addWidget(self.controlButton)
        self.setLayout(self.verticalLayout)

    def add_window_actions(self):
        # Close action
        self.closeAction = QtWidgets.QAction()
        self.closeAction.setShortcut("Ctrl+Q")
        self.closeAction.triggered.connect(self.close_app)
        self.addAction(self.closeAction)

    #============================== SLOTS ==============================

    @QtCore.pyqtSlot()
    def change_window(self):
        if self.centralWidgets.currentIndex() == 0:
            self.TitleLabel.setText("Add funds")
            self.centralWidgets.setCurrentWidget(self.paymentWidget)
        else:
            self.TitleLabel.setText("Select Item")
            self.centralWidgets.setCurrentWidget(self.selectionWidget)
        
    @QtCore.pyqtSlot()
    def close_app(self):
        self.close()