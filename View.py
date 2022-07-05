from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow

# estilo de las ventanas
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
        background-image: url(:/img/img/crearmenu_fondo.jpg);
    }
    
    #page_6
    {
        background-image: url(:/img/img/ingredientes.jpg);
    }
    
    #page_5
    {
        background-image: url(:/img/img/receta-2.jpg);
    }
    
    #page_4
    {
        background-image: url(:/img/img/listadecompra_fondo.jpg);
    }

"""

# cargar el interfaz de Qt Designer
form_class = uic.loadUiType('Interfaz.ui')[0]


class View(QMainWindow, form_class):
    # señales usadas
    platoSignal = QtCore.pyqtSignal()
    ingrSignal = QtCore.pyqtSignal()
    finIngSignal = QtCore.pyqtSignal()
    btnActivarSignal = QtCore.pyqtSignal()
    recetaSignal = QtCore.pyqtSignal()
    menuSignal = QtCore.pyqtSignal()
    addToListSignal = QtCore.pyqtSignal()
    atrasSignal = QtCore.pyqtSignal()
    cerrarSignal = QtCore.pyqtSignal()
    confirmarSignal = QtCore.pyqtSignal()
    inputCambiadoSignal = QtCore.pyqtSignal()
    finalizarSignal = QtCore.pyqtSignal()
    listaSignal = QtCore.pyqtSignal()
    exportarSignal = QtCore.pyqtSignal()
    borrarIngredienteSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        # cargar el formulario
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # especificar el estilo
        self.setStyleSheet(stylesheet)

        # configuraciones iniciales
        self.pantallas.setCurrentIndex(0)
        self.btnBorrarIngrediente.setEnabled(0)
        self.distrolist = ['Kilogramos', 'Gramos', 'Litros', 'Mililitros', 'Unidades', 'Dientes']
        self.unidades.addItems(self.distrolist)
        self.unidades_ingr.addItems(self.distrolist)

    def anadirPlato(self):
        self.platoSignal.emit()

    def anadirIngrediente(self):
        self.ingrSignal.emit()

    def finalizarIngrediente(self):
        self.finIngSignal.emit()

    def borrarIngrediente(self):
        self.borrarIngredienteSignal.emit()

    def mostrarMenu(self):
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

    def valida(self):
        self.inputCambiadoSignal.emit()

    def validaBorrar(self):
        self.btnActivarSignal.emit()

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

    def exportar(self):
        self.exportarSignal.emit()
