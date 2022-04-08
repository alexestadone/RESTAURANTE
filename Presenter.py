import sys


class Presenter ():
    def __init__(self, view, model):
        self.model = model
        self.view = view

        self.view.platoSignal.connect(self.anadirPlato)
        self.view.addToListSignal.connect(self.addToList)
        self.view.atrasSignal.connect(self.irAtras)
        self.view.cerrarSignal.connect(sys.exit)



    def anadirPlato(self):
        self.view.pantallas.setCurrentIndex(1)
        self.view.btnAdd.setEnabled(False)

    def addToList(self):
        ingredientes = self.view.get_ingredientes()
        cantidades = self.view.get_cantidades()
        todos_ingredientes = self.view.get_todos_ingredientes()
        todos_cantidades = self.view.get_todos_cantidades()

        # llamar la función para añadir un ingrediente a la lista
        self.model.add_tolist(ingredientes, cantidades, todos_ingredientes, todos_cantidades)

        self.view.input_ingredientes.setText('')
        self.view.input_cantidades.setText('')

    def irAtras(self):
        self.view.pantallas.setCurrentIndex(0)






