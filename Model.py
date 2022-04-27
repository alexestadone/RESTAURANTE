from PyQt5 import QtCore
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class Prueba:
    def __init__(self):
        print("Parece bien")


class Model(object):
    def __init__(self):
        self.ingredientes = {}

    def add_tolist(self, ing, cant, tod_ing, tod_cant, unidad):
        if self.ingredientes.get(ing) is None:
            self.ingredientes[ing] = cant
            tod_ing.addItem(ing)
            tod_cant.addItem(f'{cant} {unidad}')
        else:
            self.ingredientes[ing] += float(cant)
            fila = tod_ing.findItems(ing, QtCore.Qt.MatchExactly)
            numeroDeFila = tod_ing.row(*fila)

            filaActual = tod_cant.currentRow()
            tod_cant.setCurrentRow(numeroDeFila-1)
            tod_cant.insertItem(numeroDeFila, f'{self.ingredientes[ing]} {unidad}')
            tod_cant.takeItem(numeroDeFila+1)
            tod_cant.setCurrentRow(filaActual)

        return [tod_ing, tod_cant]

    def valida(self, texto1, texto2):
        if texto1 and texto2:
            for letra in texto2:
                if not letra.isdigit() and letra != '.':
                    return 0
            return 1
        return 0

    def clean(self, view):
        view.lista_ing.clear()
        view.lista_cant.clear()
        view.input_ingredientes.clear()
        view.input_cantidades.clear()
        view.input_nombre.clear()
        view.btnAdd.setEnabled(False)
        view.labelNombre.setText('')
        view.btnConfirmar.setEnabled(True)
        view.input_nombre.setEnabled(True)
        view.btnFinalizar.setEnabled(False)

    def finalizar(self, view):
        c = canvas.Canvas('prueba.pdf', pagesize=A4)
        w, h = A4

        c.drawString(50, h-50, view.input_nombre.text())
        c.showPage()
        c.save()


