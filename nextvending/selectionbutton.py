import os
from PyQt5 import Qt, QtCore, QtGui, QtWidgets


class SelectionButtonSignals(QtCore.QObject):
    purchase_request = QtCore.pyqtSignal(float) 

class SelectionButton(QtWidgets.QFrame):
    def __init__(self, selection_item):
        QtWidgets.QFrame.__init__(self)
        self.setObjectName("SelectionButton")
        self.resize(225, 225)
        self.setMinimumSize(self.width(), self.height())
        self.setMaximumSize(self.width(), self.height())

        self.signals = SelectionButtonSignals()

        # Parse the information in the selection_item object
        self.available = True
        self.coverPath = selection_item["cover"]
        self.name = selection_item["title"]
        self.price = selection_item["price"]
        self.quantity = selection_item["quantity"]

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        # Labels setup
        self.coverLabel = QtWidgets.QLabel()
        self.coverLabel.setObjectName("coverLabel")
        self.coverLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.coverLabel)
        
        self.nameLabel = QtWidgets.QLabel()
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.nameLabel)
        
        self.priceLabel = QtWidgets.QLabel()
        self.priceLabel.setObjectName("priceLabel")
        self.priceLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.priceLabel)

        # Shadow effect for the button frame
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setXOffset(5)
        self.shadow.setYOffset(5)
        self.shadow.setBlurRadius(12)
        self.shadow.setColor(QtGui.QColor("#888"))

        # Mouse events
        self.mousePressEvent = self.button_pressed
        self.mouseReleaseEvent = self.button_released

        self.setup_button_labels()
        self.check_quantity_available()
        self.setGraphicsEffect(self.shadow)

    def setup_button_labels(self):
        self.coverImage = QtGui.QPixmap(os.path.join(os.getcwd(), "nextvending", "assets", "img", "logos", "test.png"))
        self.coverLabel.setPixmap(self.coverImage)
        self.nameLabel.setText(self.name)
        self.priceLabel.setText("${:0.2f}".format(self.price))

    def check_quantity_available(self):
        if self.quantity == 0:
            self.setStyleSheet('background-color: #D01F3B; color: #FFFFFF;')
    
    def check_price_available(self, balance):
        if self.price > balance or self.quantity == 0:
            self.available = False
            self.setStyleSheet('background-color: #D01F3B; color: #FFFFFF;') 
        else:
            self.available = True
            self.setStyleSheet('background-color: #FFFFFF; color: #000000;') 

    def button_pressed(self, event):
        self.shadow_setup(0)
        print("Hello")

    def button_released(self, event):
        self.shadow_setup(1)
        if self.available:
            print(self.price)
            self.signals.purchase_request.emit(self.price)

    def shadow_setup(self, flag):
        self.shadow.setXOffset(flag*5)
        self.shadow.setYOffset(flag*5)
        self.shadow.setBlurRadius(flag*12)