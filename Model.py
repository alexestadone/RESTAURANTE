from PyQt5 import QtCore
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class Plato:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes[:-1]

    def guardar(self, file):
        with open(file, 'a') as f:
            f.write(self.nombre + ':' + self.ingredientes + '\n')


class Primero(Plato):
    def guardar(self, file='primeros.txt'):
        with open(file, 'a') as f:
            f.write(self.nombre + ':' + self.ingredientes + '\n')


class Segundo(Plato):
    def guardar(self, file='primeros.txt'):
        with open(file, 'a') as f:
            f.write(self.nombre + ':' + self.ingredientes + '\n')


class Postre(Plato):
    def guardar(self, file='primeros.txt'):
        with open(file, 'a') as f:
            f.write(self.nombre + ':' + self.ingredientes + '\n')


class Bebida(Plato):
    def guardar(self, file='primeros.txt'):
        with open(file, 'a') as f:
            f.write(self.nombre + ':' + self.ingredientes + '\n')


class Ingrediente:
    def __init__(self, nombre='Sin nombre', precio=0):
        self.nombre = nombre
        self.precio = precio

    def guardar(self, file):
        a = 0
        with open(file, 'r') as f:
            new_lines = []
            for line in f.readlines():
                nombre = line.split(':')[0]
                if nombre == self.nombre:
                    linea = nombre+':'+str(self.precio)+'\n'
                    new_lines.append(linea)
                    a = 1
                else:
                    new_lines.append(line)

        if a == 0:
            with open(file, 'a') as f:
                f.write(self.nombre + ':' + str(self.precio)+'\n')
        else:
            with open(file, 'w') as f:
                for line in new_lines:
                    f.write(line)


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
        ingredientes = ''
        print(view.lista_ing.count())
        for i in range(view.lista_ing.count()):
            ingredientes += view.lista_ing.item(i).text()
            ingredientes += '-'
            ingredientes += view.lista_cant.item(i).text().split(' ')[0]
            ingredientes += ','

        platoNuevo = Plato(view.input_nombre.text(), ingredientes)
        platoNuevo.guardar('platos.txt')
        # c = canvas.Canvas('prueba.pdf', pagesize=A4)
        # w, h = A4
        #
        #
        #
        # c.drawString(50, h-50, view.input_nombre.text())
        # c.showPage()
        # c.save()

    def anadirIngrediente(self, view):
        ingredienteNuevo = Ingrediente(view.nombreIngrediente.text().lower(), view.precioIngrediente.text())
        ingredienteNuevo.guardar('ingredientes.txt')

# TODO: borrar ingrediente (lecha, lehe - błędy)


