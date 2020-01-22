from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setObjectName("MainWindow")
        self.setWindowTitle("NextVending")

        self.MainLayout = QtWidgets.QWidget()
        self.MainLayout.setObjectName("MainLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainLayout)
        self.verticalLayout.setObjectName("verticalLayout")

        self.TitleLabel = QtWidgets.QLabel(self.MainLayout)
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
        self.TitleLabel.setText("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel)

        self.centralWidget = QtWidgets.QWidget(self.MainLayout)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout.addWidget(self.centralWidget)
        self.setCentralWidget(self.MainLayout)
