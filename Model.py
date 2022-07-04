from PyQt5 import QtCore
import random


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


class Bebida:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes[:-1]

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
        with open("primeros.txt", 'r') as f:
            for line in f.readlines():
                self.Primeros.append(Primero(line.split(':')[0], line.split(':')[1]))

        with open("segundos.txt", 'r') as f:
            for line in f.readlines():
                self.Segundos.append(Segundo(line.split(':')[0], line.split(':')[1]))

        with open("postres.txt", 'r') as f:
            for line in f.readlines():
                self.Postres.append(Postre(line.split(':')[0], line.split(':')[1]))

        with open("bebidas.txt", 'r') as f:
            for line in f.readlines():
                self.Bebidas.append(Bebida(line.split(':')[0], line.split(':')[1]))

    def mostrarPlatos(self, view, menu=0):
        view.primeros.clear()
        view.segundos.clear()
        view.postres.clear()
        view.bebidas.clear()

        view.mprimeros.clear()
        view.msegundos.clear()
        view.mpostres.clear()
        view.mbebidas.clear()
        if menu == 0:
            for primero in self.Primeros:
                view.primeros.addItem(primero.nombre)
            for segundo in self.Segundos:
                view.segundos.addItem(segundo.nombre)
            for postre in self.Postres:
                view.postres.addItem(postre.nombre)
            for bebida in self.Bebidas:
                view.bebidas.addItem(bebida.nombre)
        else:
            for primero in self.Primeros:
                view.mprimeros.addItem(primero.nombre)
            for segundo in self.Segundos:
                view.msegundos.addItem(segundo.nombre)
            for postre in self.Postres:
                view.mpostres.addItem(postre.nombre)
            for bebida in self.Bebidas:
                view.mbebidas.addItem(bebida.nombre)


def alea(b, n):
    lista = []
    while len(lista) < n:
        a = random.randint(0, b-1)
        if a not in lista:
            lista.append(a)
    return lista


class Menu(Receta):
    def listaDeCompra(self, view):
        ingredientes = {}

        def guardar(categoria):
            for primero in categoria:
                for ingrediente in primero.ingredientes.split(','):
                    if not ingrediente:
                        continue
                    nombre = ingrediente.split('-')[0]
                    unidad = ""
                    _ = ingrediente.split('-')[1]
                    cantidadUnidad = _.split('|')
                    valor = float(cantidadUnidad[0])
                    if len(cantidadUnidad) > 1:
                        unidad = cantidadUnidad[1]
                    if not ingredientes.get(nombre):
                        ingredientes[nombre] = [valor, unidad]
                    else:
                        ingredientes[nombre][0] += valor

        guardar(self.Primeros)
        guardar(self.Segundos)
        guardar(self.Postres)
        guardar(self.Bebidas)

        view.listaDeCompra.clear()
        for key in ingredientes:
            view.listaDeCompra.addItem(f"{key} -> {round(ingredientes[key][0], 3)} {ingredientes[key][1]}")

    def elegirPlatos(self, view):
        lista = [self.Primeros[i] for i in alea(len(self.Primeros), min(5, len(self.Primeros)))]
        self.Primeros = lista

        lista = [self.Segundos[i] for i in alea(len(self.Segundos), min(5, len(self.Segundos)))]
        self.Segundos = lista

        lista = [self.Postres[i] for i in alea(len(self.Postres), min(5, len(self.Postres)))]
        self.Postres = lista

        lista = [self.Bebidas[i] for i in alea(len(self.Bebidas), min(5, len(self.Bebidas)))]
        self.Bebidas = lista

        self.mostrarPlatos(view, menu=1)
        self.listaDeCompra(view)


class Model(object):
    def __init__(self):
        self.ingredientes = {}
        self.unidades = {'Litros': [1, 'Litros'], 'Kilogramos': [1, 'Kilogramos'], 'Unidades': [1, 'Unidades'],
                         'Dientes': [1, 'Dientes'], 'Mililitros': [1000, 'Litros'], 'Gramos': [1000, 'Kilogramos']}

    def add_tolist(self, ing, cant, tod_ing, tod_cant, unidad):
        if self.ingredientes.get(ing) is None:
            self.ingredientes[ing] = cant
            tod_ing.addItem(ing)
            tod_cant.addItem(f'{round(cant/self.unidades[unidad][0],3)} {self.unidades[unidad][1]}')
        else:
            self.ingredientes[ing] += round(float(cant/self.unidades[unidad][0]), 3)
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
        view.btnBorrarIngrediente.setEnabled(False)

    def finalizar(self, view):
        ingredientes = ''
        for i in range(view.lista_ing.count()):
            cantidadUnidad = view.lista_cant.item(i).text().split(' ')
            ingredientes += view.lista_ing.item(i).text()
            ingredientes += '-'
            ingredientes += cantidadUnidad[0]
            ingredientes += '|'
            ingredientes += cantidadUnidad[1]
            ingredientes += ','

        if view.tipoDePlato.currentText().lower() == "primero":
            platoNuevo = Primero(view.input_nombre.text(), ingredientes)

        elif view.tipoDePlato.currentText().lower() == "segundo":
            platoNuevo = Segundo(view.input_nombre.text(), ingredientes)

        elif view.tipoDePlato.currentText().lower() == "bebida":
            platoNuevo = Bebida(view.input_nombre.text(), ingredientes)

        else:
            platoNuevo = Postre(view.input_nombre.text(), ingredientes)

        platoNuevo.guardar()

    def anadirIngrediente(self, view):
        ingredienteNuevo = Ingrediente(view.nombreIngrediente.text().lower(), view.precioIngrediente.text())
        ingredienteNuevo.guardar('ingredientes.txt')
        view.nombreIngrediente.setText("")
        view.precioIngrediente.setText("")

    def exportar(self, view):
        from PyQt5.QtWidgets import QMessageBox
        from fpdf import FPDF
        from datetime import date
        pdf = FPDF()
        pdf.set_margins(20, 20, 20)
        pdf.set_font("Arial", size=15)
        texto = [f"{view.listaDeCompra.item(i).text()}" for i in range(view.listaDeCompra.count())]
        for i, el in enumerate(texto):
            a = i % 25
            if a == 0:
                pdf.add_page()
                print(a)
            pdf.set_xy(20, 20+a*10)
            pdf.multi_cell(80, 10, txt=el.split(' -> ')[0].capitalize(), align='C')
            pdf.set_xy(100, 20+a * 10)
            pdf.multi_cell(10, 10, txt="->")
            pdf.set_xy(110, 20 + a * 10)
            pdf.multi_cell(80, 10, txt=el.split(' -> ')[1], align='C')

        pdf.output(f"ListaDeCompra_{date.today()}.pdf")
        msg = QMessageBox()
        msg.setText("Enviado al PDF.")
        msg.setIcon(1)
        msg.exec()
