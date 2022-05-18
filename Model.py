import random

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
    def guardar(self, file='segundos.txt'):
        with open(file, 'a') as f:
            f.write(self.nombre + ':' + self.ingredientes + '\n')


class Postre(Plato):
    def guardar(self, file='postres.txt'):
        with open(file, 'a') as f:
            f.write(self.nombre + ':' + self.ingredientes + '\n')


class Bebida(Plato):
    def guardar(self, file='bebidas.txt'):
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


class Receta:
    def __init__(self):
        self.Primeros = []
        self.Segundos = []
        self.Postres = []
        self.Bebidas = []

        with open('primeros.txt') as f:
            for line in f.readlines():
                self.Primeros.append(Primero(line.split(':')[0], line.split(':')[1]))

        with open('segundos.txt') as f:
            for line in f.readlines():
                self.Segundos.append(Segundo(line.split(':')[0], line.split(':')[1]))

        with open('postres.txt') as f:
            for line in f.readlines():
                self.Postres.append(Postre(line.split(':')[0], line.split(':')[1]))

        with open('bebidas.txt') as f:
            for line in f.readlines():
                self.Bebidas.append(Bebida(line.split(':')[0], line.split(':')[1]))

    def mostrarRecetas(self, view, menu=0):

        if not menu:
            view.primeros.clear()
            view.segundos.clear()
            view.postres.clear()
            view.bebidas.clear()
            for el in self.Primeros:
                view.primeros.addItem(el.nombre)
            for el in self.Segundos:
                view.segundos.addItem(el.nombre)
            for el in self.Postres:
                view.postres.addItem(el.nombre)
            for el in self.Bebidas:
                view.bebidas.addItem(el.nombre)
        else:
            view.mPrimeros.clear()
            view.mSegundos.clear()
            view.mPostres.clear()
            view.mBebidas.clear()
            for el in self.Primeros:
                view.mPrimeros.addItem(el.nombre)
            for el in self.Segundos:
                view.mSegundos.addItem(el.nombre)
            for el in self.Postres:
                view.mPostres.addItem(el.nombre)
            for el in self.Bebidas:
                view.mBebidas.addItem(el.nombre)

class Menu(Receta):

    def elegirPlatos(self, view):
        Recetas = Receta()
        self.Primeros = []
        self.Segundos = []
        self.Postres = []
        self.Bebidas = []

        primero = Recetas.Primeros[random.randint(0, 2000) % len(Recetas.Primeros)]
        while len(self.Primeros) < min(5, len(Recetas.Primeros)):
            if primero not in self.Primeros:
                self.Primeros.append(primero)
            primero = Recetas.Primeros[random.randint(0, 2000) % len(Recetas.Primeros)]

        segundo = Recetas.Segundos[random.randint(0, 2000) % len(Recetas.Segundos)]
        while len(self.Segundos) < min(5, len(Recetas.Segundos)):
            if Segundo not in self.Segundos:
                self.Segundos.append(segundo)
            segundo = Recetas.Segundos[random.randint(0, 2000) % len(Recetas.Segundos)]

        postre = Recetas.Postres[random.randint(0, 2000) % len(Recetas.Postres)]
        while len(self.Postres) < min(5, len(Recetas.Postres)):
            if postre not in self.Postres:
                self.Postres.append(postre)
            postre = Recetas.Postres[random.randint(0, 2000) % len(Recetas.Postres)]

        bebida = Recetas.Bebidas[random.randint(0, 2000) % len(Recetas.Bebidas)]
        while len(self.Bebidas) < min(5, len(Recetas.Bebidas)):
            if bebida not in self.Bebidas:
                self.Bebidas.append(bebida)
            bebida = Recetas.Bebidas[random.randint(0, 2000) % len(Recetas.Bebidas)]

        self.mostrarRecetas(view, menu=1)

class ListaDeCompra:
    def __init__(self, view):
        self.Primeros = [view.mPrimeros.item(i).text() for i in range(view.mPrimeros.count())]
        self.Segundos = [view.mSegundos.item(i).text() for i in range(view.mSegundos.count())]
        self.Postres = [view.mPostres.item(i).text() for i in range(view.mPostres.count())]
        self.Bebidas = [view.mBebidas.item(i).text() for i in range(view.mBebidas.count())]
        self.ingredientes = {}

        with open('primeros.txt', 'r') as f:
            for line in f.readlines():
                if line.split(':')[0] in self.Primeros:
                    ingredientes = line.split(':')[1]
                    for ingrediente in ingredientes.split(','):
                        if not self.ingredientes.get(ingrediente.split('-')[0]):
                            self.ingredientes[ingrediente.split('-')[0]] = 0
                        self.ingredientes[ingrediente.split('-')[0]] += int(self.ingredientes[ingrediente.split('-')[0]])
        for k in self.ingredientes:
            view.listaDeCompra.addItem(f'{k} -> {self.ingredientes[k]}')


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

        if view.tipoDePlato.currentText().lower() == 'primero':
            platoNuevo = Primero(view.input_nombre.text(), ingredientes)
        elif view.tipoDePlato.currentText().lower() == 'segundo':
            platoNuevo = Segundo(view.input_nombre.text(), ingredientes)

        elif view.tipoDePlato.currentText().lower() == 'postre':
            platoNuevo = Postre(view.input_nombre.text(), ingredientes)
        else:
            platoNuevo = Bebida(view.input_nombre.text(), ingredientes)

        platoNuevo.guardar()

        # platoNuevo.guardar('platos.txt')
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


