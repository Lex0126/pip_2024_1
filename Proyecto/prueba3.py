import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

qtCreatorFile3 = "Personalizar.ui"
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialogP(QtWidgets.QDialog, Ui_dialog):
    color_signal = pyqtSignal(str)
    dificultad_signal = pyqtSignal(int)

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Conectar los botones a sus respectivos métodos
        self.btn_aceptar.clicked.connect(self.enviar)
        self.rbtn_amarillo.clicked.connect(self.color)
        self.rbtn_rojo.clicked.connect(self.color)
        self.rbtn_naranja.clicked.connect(self.color)
        self.rbtn_morado.clicked.connect(self.color)
        self.rbtn_facil.clicked.connect(self.dificultad)
        self.rbtn_normal.clicked.connect(self.dificultad)
        self.rbt_dificil.clicked.connect(self.dificultad)

        # Valores iniciales
        self.color = "yellow"
        self.dificultad = 400

    def color(self):
        # Determinar el color según el botón presionado
        objeto = self.sender()
        nombre = objeto.objectName()

        if nombre == "rbtn_amarillo":
            self.color = "yellow"
        elif nombre == "rbtn_rojo":
            self.color = "red"
        elif nombre == "rbtn_naranja":
            self.color = "orange"
        else:
            self.color = "purple"

        print(f"Color seleccionado: {self.color}")

    def dificultad(self):

        objeto = self.sender()
        nombre = objeto.objectName()

        if nombre == "rbtn_facil":
            self.dificultad = 400
        elif nombre == "rbtn_normal":
            self.dificultad = 200
        else:
            self.dificultad = 25

        print(f"Dificultad seleccionada: {self.dificultad}")  # Depuración

    def enviar(self):
        # Emitir las señales con los valores seleccionados
        self.color_signal.emit(self.color)
        self.dificultad_signal.emit(self.dificultad)
        self.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialogP()
    dialog.show()
    sys.exit(app.exec_())




