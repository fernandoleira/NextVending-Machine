import os
import sys
from PyQt5 import QtCore, QtWidgets

from mainwindow import MainWindow


# Request all configuration files paths
def get_conf_paths():
    paths = dict()

    global_path = os.path.join(os.getcwd(), "nextvending", "config")
    for path in os.listdir(global_path):
        paths[path] = os.path.join(global_path, path)

    return paths

# Configure stylesheet for the QApplication
def get_stylesheet():
    qss_path = os.path.join(os.getcwd(), "nextvending", "assets", "style", "main.qss")
    qss = QtCore.QFile(qss_path)
    qss.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    ts = QtCore.QTextStream(qss)

    return ts.readAll()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    stylesheet = get_stylesheet()
    app.setStyleSheet(stylesheet)

    main = MainWindow(get_conf_paths())
    main.show()

    sys.exit(app.exec_())
