from PyQt5 import QtCore


class Model(object):
    def __init__(self):
        self.ingredientes = {}

    def add_tolist(self, ing, cant, tod_ing, tod_cant):
        if self.ingredientes.get(ing) is None:
            self.ingredientes[ing] = cant
            tod_ing.addItem(ing)
            tod_cant.addItem(str(cant))
        else:
            self.ingredientes[ing] += float(cant)
            fila = tod_ing.findItems(ing, QtCore.Qt.MatchExactly)
            numeroDeFila = tod_ing.row(*fila)

            filaActual = tod_cant.currentRow()
            tod_cant.setCurrentRow(numeroDeFila-1)
            tod_cant.insertItem(numeroDeFila, str(self.ingredientes[ing]))
            tod_cant.takeItem(numeroDeFila+1)
            tod_cant.setCurrentRow(filaActual)

        return [tod_ing, tod_cant]

