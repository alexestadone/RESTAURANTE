import sys
from Model import Receta
from Model import Menu
from PyQt5.QtWidgets import QMessageBox


class Presenter:
    def __init__(self, view, model):
        self.model = model
        self.view = view

        self.view.platoSignal.connect(self.anadirPlato)
        self.view.ingrSignal.connect(self.anadirIngrediente)
        self.view.recetaSignal.connect(self.mostrarRecetas)
        self.view.finIngSignal.connect(self.finalizarIngrediente)
        self.view.borrarIngredienteSignal.connect(self.borrarIngrediente)
        self.view.btnActivarSignal.connect(self.activarBtnBorrar)
        self.view.menuSignal.connect(self.mostrarMenu)
        self.view.addToListSignal.connect(self.addToList)
        self.view.atrasSignal.connect(self.irAtras)
        self.view.cerrarSignal.connect(sys.exit)
        self.view.confirmarSignal.connect(self.confirmarNombre)
        self.view.inputCambiadoSignal.connect(self.nombreCambiado)
        self.view.finalizarSignal.connect(self.finalizar)
        self.view.listaSignal.connect(self.lista)
        self.view.exportarSignal.connect(self.exportar)

    def anadirPlato(self):
        self.view.pantallas.setCurrentIndex(1)
        self.view.frame_2.setEnabled(False)

    def anadirIngrediente(self):
        self.view.pantallas.setCurrentIndex(2)

    def finalizarIngrediente(self):
        self.model.anadirIngrediente(self.view)
        mensajeInfo("El ingrediente ya está añadido.")

    def activarBtnBorrar(self):
        self.view.btnBorrarIngrediente.setEnabled(1)

    def borrarIngrediente(self):
        item = self.view.lista_ing.selectedItems()[0]
        index = self.view.lista_ing.row(item)
        self.view.lista_ing.takeItem(index)
        self.view.lista_cant.takeItem(index)
        self.view.btnBorrarIngrediente.setEnabled(False)

    def mostrarRecetas(self):
        self.view.pantallas.setCurrentIndex(5)
        RecetaNueva = Receta()
        RecetaNueva.mostrarPlatos(self.view)

    def mostrarMenu(self):
        self.view.pantallas.setCurrentIndex(3)
        MenuNuevo = Menu()
        MenuNuevo.elegirPlatos(self.view)

    def addToList(self):
        ingredientes = self.view.get_ingredientes()
        cantidades = self.view.get_cantidades()
        todos_ingredientes = self.view.get_todos_ingredientes()
        todos_cantidades = self.view.get_todos_cantidades()
        unidad = self.view.unidades.currentText()

        self.model.add_tolist(ingredientes, cantidades, todos_ingredientes, todos_cantidades, unidad)

        self.view.btnAdd.setEnabled(0)
        self.view.input_ingredientes.setText('')
        self.view.input_cantidades.setText('')

        if not self.view.btnConfirmar.isEnabled():
            self.view.btnFinalizar.setEnabled(True)
        else:
            self.view.btnFinalizar.setEnabled(False)

    def irAtras(self):
        self.view.pantallas.setCurrentIndex(0)
        self.model.clean(self.view)

    def confirmarNombre(self):
        texto = self.view.input_nombre.text()
        texto += f' ({self.view.tipoDePlato.currentText()})'
        self.view.labelNombre.setText(f"{texto}")
        self.view.btnConfirmar.setEnabled(False)
        self.view.input_nombre.setEnabled(False)
        self.view.frame_2.setEnabled(True)
        if self.view.tipoDePlato.currentText() == "Bebida":
            self.view.btnFinalizar.setEnabled(True)

    def nombreCambiado(self):
        texto1 = self.view.input_ingredientes.text()
        texto2 = self.view.input_cantidades.text()
        valorLogico = self.model.valida(texto1, texto2)
        self.view.btnAdd.setEnabled(valorLogico)

    def finalizar(self):
        self.model.finalizar(self.view)
        self.model.clean(self.view)
        self.view.frame_2.setEnabled(0)
        self.view.pantallas.setCurrentIndex(0)
        mensajeInfo("Se ha añadido el plato.")

    def lista(self):
        self.view.pantallas.setCurrentIndex(4)

    def exportar(self):
        self.model.exportar(self.view)
        self.view.pantallas.setCurrentIndex(0)


def mensajeInfo(texto):
    msg = QMessageBox()
    msg.setText(texto)
    msg.setIcon(1)
    msg.exec()

