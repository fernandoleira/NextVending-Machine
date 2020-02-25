import json
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

from mainview import MainView


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config_paths):
        QtWidgets.QMainWindow.__init__(self)
        self.setObjectName("MainWindow")
        self.setWindowTitle("NextVending")
        #self.showFullScreen()
        self.resize(550, 800)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        self._config_paths = config_paths

        # Add shorcut actions
        self.add_window_actions()

        # Initialize the main view
        self.mainView = MainView(self.parse_file(
            'config.json'), self.parse_file('products.json'))
        self.setCentralWidget(self.mainView)

    # Function to add the respective action shorcuts of the MainWindow
    def add_window_actions(self):
        # Close action
        self.closeAction = QtWidgets.QAction()
        self.closeAction.setShortcut("Ctrl+Q")
        self.closeAction.triggered.connect(self.close_app)
        self.addAction(self.closeAction)

    # Function to print logs in the console with the correct format
    def print_log(self, message):
        print("[{}] {}".format(datetime.now().strftime(
            "%Y/%b/%d:%H:%m:%S"), message))

    # Function to retreive data from an external config file
    def parse_file(self, conf_fn):
        if conf_fn not in self._config_paths:
            self.print_log("Configuration file {} not founded".format(
                conf_fn.split('/')[-1]))
            exit()

        rd = open(self._config_paths[conf_fn], "r+")
        data = json.load(rd)
        rd.close()

        return data

    # ============================== SLOTS ==============================

    @QtCore.pyqtSlot()
    def close_app(self):
        self.close()
