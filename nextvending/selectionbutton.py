from os import path, getcwd
from datetime import datetime
from PyQt5 import Qt, QtCore, QtGui, QtWidgets


class SelectionSignals(QtCore.QObject):
    purchase_request = QtCore.pyqtSignal(dict)


class SelectionButton(QtWidgets.QFrame):
    def __init__(self, selection_item):
        QtWidgets.QFrame.__init__(self)
        self.setObjectName("SelectionButton")
        self.resize(225, 225)
        self.setMinimumSize(self.width(), self.height())
        self.setMaximumSize(self.width(), self.height())

        self.signals = SelectionSignals()

        # Parse the information in the selection_item object
        self.available = True
        self.id = selection_item["product_id"]
        self.coverPath = selection_item["cover"]
        self.name = selection_item["name"]
        self.price = selection_item["price"]
        self.quantity = selection_item["quantity"]

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        # Labels setup
        self.coverLabel = QtWidgets.QLabel()
        self.coverLabel.setObjectName("coverLabel")
        self.coverLabel.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.coverLabel)

        self.nameLabel = QtWidgets.QLabel()
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.nameLabel)

        self.priceLabel = QtWidgets.QLabel()
        self.priceLabel.setObjectName("priceLabel")
        self.priceLabel.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
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
        self.setGraphicsEffect(self.shadow)

    def setup_button_labels(self):
        self.coverImage = QtGui.QPixmap(
            path.join(getcwd(), "nextvending", self.coverPath))
        self.coverLabel.setPixmap(self.coverImage)
        self.nameLabel.setText(self.name)
        self.priceLabel.setText("${:0.2f}".format(self.price))

    def check_price_available(self, balance):
        if self.price > balance or self.quantity == 0:
            self.available = False
            self.setStyleSheet('background-color: #D01F3B; color: #FFFFFF;')
        else:
            self.available = True
            self.setStyleSheet('background-color: #FFFFFF; color: #000000;')

    def shadow_setup(self, flag):
        self.shadow.setXOffset(flag*5)
        self.shadow.setYOffset(flag*5)
        self.shadow.setBlurRadius(flag*12)

    # ============================== EVENTS ==============================
    def button_pressed(self, event):
        self.shadow_setup(0)

    def button_released(self, event):
        self.shadow_setup(1)
        if self.available:
            self.quantity -= 1
            if self.quantity == 0:
                self.available = False
                self.setStyleSheet(
                    'background-color: #D01F3B; color: #FFFFFF;')

            purchase_info = dict(
                timestamp=int(datetime.timestamp(datetime.now())), 
                product_id=self.id, 
                price=self.price, 
                quantity_remaining=self.quantity
            )

            self.signals.purchase_request.emit(purchase_info)
