import sys
from os import path, getcwd
from PyQt5 import QtCore, QtGui, QtWidgets

class SuccessWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("SuccessWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        
        self.loadingMovie = QtGui.QMovie(path.join(getcwd(), "nextvending", "assets", "img", "gifs", "loading.gif"))
        size = self.loadingMovie.scaledSize()

        self.successMovie = QtGui.QMovie(path.join(getcwd(), "nextvending", "assets", "img", "gifs", "checkmark.gif"))
        self.successMovie.setScaledSize(size)

        self.label = QtWidgets.QLabel()
        self.label.setMovie(self.loadingMovie)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)
        self.setLayout(self.verticalLayout)
        
        self.loadingMovie.start()

        self.animationTimer = QtCore.QTimer()
        self.animationTimer.setSingleShot = True
        self.animationTimer.timeout.connect(self.loading_completed)

    def start(self):
        self.animationTimer.start(3000)

    def reset(self):
        self.animationTimer.stop()
        self.successMovie.stop()
        self.label.setMovie(self.loadingMovie)
        self.loadingMovie.start()

    @QtCore.pyqtSlot()
    def loading_completed(self):
        self.loadingMovie.stop()
        self.label.setMovie(self.successMovie)
        self.successMovie.start()