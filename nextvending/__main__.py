import os, sys
from PyQt5 import QtCore, QtWidgets

from mainwindow import MainWindow

# Request all configuration files paths
def get_conf_paths():
    paths = dict()

    global_path = os.path.join(os.getcwd(), "nextvending", "config")
    for path in os.listdir(global_path):
        paths[path] = os.path.join(global_path, path)

    return paths

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    main = MainWindow(get_conf_paths())
    main.show()

    sys.exit(app.exec_())
