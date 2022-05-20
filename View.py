import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QDialog
from PyQt5.QtGui import QFont

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
    
    #page_2
    {
        background-image: url(:/img/img/plato-2.jpg);
        background-repeat:no-repeat;
    }
    
    #page_3
    {
        background-image: url(:/img/img/menu.jpg);
    }
    
    #page_6
    {
        background-image: url(:/img/img/ingredientes.jpg);
    }
    
    #page_5
    {
        background-image: url(:/img/img/receta-2.jpg);
    }

"""


class View(QMainWindow, form_class):
    platoSignal = QtCore.pyqtSignal()
    ingrSignal = QtCore.pyqtSignal()
    finIngSignal = QtCore.pyqtSignal()
    recetaSignal = QtCore.pyqtSignal()
    menuSignal = QtCore.pyqtSignal()
    addToListSignal = QtCore.pyqtSignal()
    atrasSignal = QtCore.pyqtSignal()
    cerrarSignal = QtCore.pyqtSignal()
    confirmarSignal = QtCore.pyqtSignal()
    inputCambiadoSignal = QtCore.pyqtSignal()
    finalizarSignal = QtCore.pyqtSignal()
    listaSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)  # Constructor Formulario Designer Cargamos el formulario
        self.pantallas.setCurrentIndex(0)
        self.setStyleSheet(stylesheet)
        self.distrolist = ['Kilogramos', 'Litros', 'Docenas', 'Unidades']
        self.unidades.addItems(self.distrolist)  # añadir lista al combobox de unidades
        self.frame_2.setEnabled(False)

    def anadirPlato(self):  # poner aquí el nombre del slot  y a continuación su código
        self.platoSignal.emit()

    def anadirIngrediente(self):  # poner aquí el nombre del slot  y a continuación su código
        self.ingrSignal.emit()

    def finalizarIngrediente(self):
        self.finIngSignal.emit()

    def mostrarMenu(self):  # poner aquí el nombre del slot  y a continuación su código
        self.menuSignal.emit()

    def add_tolist(self):
        self.addToListSignal.emit()

    def irAtras(self):
        self.atrasSignal.emit()

    def cerrar(self):
        self.cerrarSignal.emit()

    def confirmar(self):
        self.confirmarSignal.emit()

    def mostrarRecetas(self):
        self.recetaSignal.emit()

    def crearMenu(self):
        pass

    def valida(self):
        self.inputCambiadoSignal.emit()

    def finalizar(self):
        self.finalizarSignal.emit()

    def get_ingredientes(self):
        return self.input_ingredientes.text()

    def get_cantidades(self):
        return float(self.input_cantidades.text())

    def get_todos_ingredientes(self):
        return self.lista_ing

    def get_todos_cantidades(self):
        return self.lista_cant

    def lista(self):
        self.listaSignal.emit()

    #
    #
    # def mostrarRecetas(self):
    #     pass
    #
    # def crearMenu(self):
    #     pass
