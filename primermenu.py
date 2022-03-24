import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

form_class = uic.loadUiType('restaurante_intro_ingredientes.ui')[0]


class MyWindowClass(QtWidgets.QMainWindow, form_class):

    def __init__(self, parent=None):
        global distrolist
        distrolist = []
        QtWidgets.QMainWindow.__init__(self, parent)  # Constructor Clase QWidget
        self.setupUi(self)  # Constructor Formulario Designer Cargamos el formulario
        self.unidades.clear() # vaciamos lista de unidades x si futuro cambio
        distrolist = ['Kilogramos', 'Litros', 'Docenas'] # lista predeterminada, se puede intentar hacer input de las unidades en un futuro
        self.unidades.addItems(distrolist) #añadir lista al combobox de unidades
        self.unidades.setCurrentIndex(0) # hace que la unidad a mostrar sea la primera

    def add_tolist(self):
        lista = self.input_cantidades.text() + ' ' + self.input_ingredientes.text()

        self.todalalista.addItem(lista)

    def valida(self): #nose seguro si hace falta para los lineedit
        pass


def principal():
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()


if __name__ == '__main__':
    principal()
