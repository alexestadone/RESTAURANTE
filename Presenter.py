import sys


class Presenter:
    def __init__(self, view, model):
        self.model = model
        self.view = view

        self.view.platoSignal.connect(self.anadirPlato)
        self.view.addToListSignal.connect(self.addToList)
        self.view.atrasSignal.connect(self.irAtras)
        self.view.cerrarSignal.connect(sys.exit)
        self.view.confirmarSignal.connect(self.confirmarNombre)
        self.view.inputCambiadoSignal.connect(self.nombreCambiado)
        self.view.finalizarSignal.connect(self.finalizar)

    def anadirPlato(self):
        self.view.pantallas.setCurrentIndex(1)

    def addToList(self):
        ingredientes = self.view.get_ingredientes()
        cantidades = self.view.get_cantidades()
        todos_ingredientes = self.view.get_todos_ingredientes()
        todos_cantidades = self.view.get_todos_cantidades()
        unidad = self.view.unidades.currentText()

        # llamar la función para añadir un ingrediente a la lista
        self.model.add_tolist(ingredientes, cantidades, todos_ingredientes, todos_cantidades, unidad)

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
        self.view.labelNombre.setText(f"Plato: {texto}")
        self.view.btnConfirmar.setEnabled(False)
        self.view.input_nombre.setEnabled(False)

        if self.view.lista_ing.count() == 0:
            self.view.btnFinalizar.setEnabled(False)
        else:
            self.view.btnFinalizar.setEnabled(True)

    def nombreCambiado(self):
        texto1 = self.view.input_ingredientes.text()
        texto2 = self.view.input_cantidades.text()
        valorLogico = self.model.valida(texto1, texto2)
        self.view.btnAdd.setEnabled(valorLogico)

    def finalizar(self):
        self.model.finalizar(self.view)
        self.model.clean(self.view)
        self.view.pantallas.setCurrentIndex(0)







