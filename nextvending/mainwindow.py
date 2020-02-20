from PyQt5 import QtCore, QtGui, QtWidgets

from mainview import MainView


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config_paths):
        QtWidgets.QMainWindow.__init__(self)
        self.setObjectName("MainWindow")
        self.setWindowTitle("NextVending")
        #self.showFullScreen()

        self._config_paths = config_paths

        # Add shorcut actions
        self.add_window_actions()

        # Initialize the main view
        self.mainView = MainView({}, {})
        self.setCentralWidget(self.mainView)

    # Function to print logs in the console using the correct format
    def printLog(self, message):
        print("[{}] {}".format(datetime.now().strftime(
            "%Y/%b/%d:%H:%m:%S"), message))

    # Function to add the respective action shorcuts of the MainWindow
    def add_window_actions(self):
        # Close action
        self.closeAction = QtWidgets.QAction()
        self.closeAction.setShortcut("Ctrl+Q")
        self.closeAction.triggered.connect(self.close_app)
        self.addAction(self.closeAction)

    #============================== SLOTS ==============================
        
    @QtCore.pyqtSlot()
    def close_app(self):
        self.close()