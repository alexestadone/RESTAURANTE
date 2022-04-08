import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QDialog

form_class = uic.loadUiType('Interfaz.ui')[0]

stylesheet = """
    #page
    {
        background-image: url(:/img/img/pizza.jpg);
        background-repeat:no-repeat;
    }

    #label, #label_2
    {
        color: white;
    }

    #btnCerrar:hover
    {
        background-color: red;
    }

"""


class View(QMainWindow, form_class):
    platoSignal = QtCore.pyqtSignal()
    addToListSignal = QtCore.pyqtSignal()
    atrasSignal = QtCore.pyqtSignal()
    cerrarSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)  # Constructor Formulario Designer Cargamos el formulario
        self.pantallas.setCurrentIndex(0)
        self.setStyleSheet(stylesheet)
        # global distrolist
        # distrolist = []
        # self.unidades.clear()  # vaciamos lista de unidades x si futuro cambio
        # distrolist = ['Kilogramos', 'Litros', 'Docenas',
        #               'Unidades']  # lista predeterminada, se puede intentar hacer input de las unidades en un futuro
        # self.unidades.addItems(distrolist)  # añadir lista al combobox de unidades
        # self.unidades.setCurrentIndex(0)  # hace que la unidad a mostrar sea la primera

        # self.ingredientes = {}

    # def calc(self, value1, operation, value2):
    #     if operation == "+":
    #         self.result = value1 + value2
    #     elif operation == "-":
    #         self.result = value1 - value2
    #     return self.result
    #

    #
    #
    # def valida(self): #nose seguro si hace falta para los lineedit
    #     texto1 = self.input_cantidades.text()
    #     texto_cambiado = self.sender().text()
    #
    #     if texto1 and texto_cambiado == texto1:
    #         for letra in texto_cambiado:
    #             if not letra.isdigit() and letra != '.':
    #                 self.btnAdd.setEnabled(False)
    #                 return
    #         self.btnAdd.setEnabled(True)
    #
    # def irAtras(self):  # poner aquí el nombre del slot  y a continuación su código
    #     self.pantallas.setCurrentIndex(0)
    #
    def anadirPlato(self):  # poner aquí el nombre del slot  y a continuación su código
        self.platoSignal.emit()

    def add_tolist(self):
        self.addToListSignal.emit()

    def irAtras(self):
        self.atrasSignal.emit()

    def cerrar(self):
        self.cerrarSignal.emit()

    def mostrarRecetas(self):
        pass

    def crearMenu(self):
        pass

    def valida(self):
        pass

    def get_ingredientes(self):
        return self.input_ingredientes.text()

    def get_cantidades(self):
        return float(self.input_cantidades.text())

    def get_todos_ingredientes(self):
        return self.lista_ing

    def get_todos_cantidades(self):
        return self.lista_cant

    #
    #
    # def mostrarRecetas(self):
    #     pass
    #
    # def crearMenu(self):
    #     pass
