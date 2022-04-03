import sys
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

form_class = uic.loadUiType('restaurante_intro_ingredientes.ui')[0]


class MyWindowClass(QtWidgets.QMainWindow, form_class):

    def __init__(self, parent=None):
        global distrolist
        distrolist = []
        QtWidgets.QMainWindow.__init__(self, parent)  # Constructor Clase QWidget
        self.setupUi(self)  # Constructor Formulario Designer Cargamos el formulario
        self.unidades.clear() # vaciamos lista de unidades x si futuro cambio
        distrolist = ['Kilogramos', 'Litros', 'Docenas', 'Unidades'] # lista predeterminada, se puede intentar hacer input de las unidades en un futuro
        self.unidades.addItems(distrolist) #añadir lista al combobox de unidades
        self.unidades.setCurrentIndex(0) # hace que la unidad a mostrar sea la primera
        self.pantallas.setCurrentIndex(0)
        self.ingredientes = {}

    def add_tolist(self):
        lista = [self.input_ingredientes.text(), self.input_cantidades.text()] # falta pulirlo y añadir las unidadse, esto es muy cutre

        if self.ingredientes.get(lista[0]) is None:
            self.ingredientes[lista[0]] = float(lista[1])
            self.lista_ing.addItem(lista[0])
            self.lista_cant.addItem(lista[1])
        else:
            self.ingredientes[lista[0]] += float(lista[1])
            print(lista[0], self.ingredientes[lista[0]])
            fila = self.lista_ing.findItems(lista[0], QtCore.Qt.MatchExactly)
            numeroDeFila = self.lista_ing.row(*fila)

            filaActual = self.lista_cant.currentRow()
            self.lista_cant.setCurrentRow(numeroDeFila-1)
            self.lista_cant.insertItem(numeroDeFila, str(self.ingredientes[lista[0]]))
            self.lista_cant.takeItem(numeroDeFila+1)
            self.lista_cant.setCurrentRow(filaActual)



        self.input_ingredientes.setText('')
        self.input_cantidades.setText('')


    def valida(self): #nose seguro si hace falta para los lineedit
        texto1 = self.input_cantidades.text()
        texto_cambiado = self.sender().text()

        if texto1 and texto_cambiado == texto1:
            for letra in texto_cambiado:
                if not letra.isdigit() and letra != '.':
                    self.btnAdd.setEnabled(False)
                    return
            self.btnAdd.setEnabled(True)

    def irAtras(self):  # poner aquí el nombre del slot  y a continuación su código
        self.pantallas.setCurrentIndex(0)

    def anadirPlato(self):  # poner aquí el nombre del slot  y a continuación su código
        self.pantallas.setCurrentIndex(1)
        self.btnAdd.setEnabled(False)


    def mostrarRecetas(self):
        pass

    def crearMenu(self):
        pass


def principal():
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()


if __name__ == '__main__':
    principal()
