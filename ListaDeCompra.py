import sys
from PyQt5 import uic
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


def principal():
    app = QApplication(sys.argv)
    MyWindow = Restaurante()
    MyWindow.show()
    app.exec()


if __name__ == '__main__':
    principal()
