import sys
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from View import View
from Model import Model
from Presenter import Presenter


class Restaurante(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        view = View()
        model = Model()
        self.presenter = Presenter(view, model)
        self.setCentralWidget(view)
        self.setWindowTitle('Lista De Compra')
        self.setFont(QFont("EB Garamond 12 All SC"))
        self.setWindowIcon(QtGui.QIcon(":/img/icono"))


def principal():
    app = QApplication(sys.argv)
    app.setFont(QFont("EB Garamond 12 All SC"), "QLabel")
    app.setFont(QFont("EB Garamond 12 All SC"), "QPushButton")
    app.setFont(QFont("EB Garamond 12 All SC"), "QLineEdit")
    app.setFont(QFont("EB Garamond 12 All SC"), "QComboBox")
    app.setFont(QFont("EB Garamond 12 All SC"), "QListWidget")

    MyWindow = Restaurante()
    MyWindow.show()
    app.exec()


if __name__ == '__main__':
    principal()
