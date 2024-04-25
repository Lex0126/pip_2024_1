import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_05_v2_OpAritmeticas_withStylee.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.Operacion)
        self.btn_restar.clicked.connect(self.Operacion)
        self.btn_mult.clicked.connect(self.Operacion)
        self.btn_division.clicked.connect(self.Operacion)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def Operacion(self):
        try:
            objeto = self.sender()
            nombre= objeto.objectName()
            print(nombre)

            a = float(self.txt_A.text())
            b = float(self.txt_B.text())

            if nombre== "btn_sumar":
                cadena = str(a + b)
            elif nombre== "btn_restar":
                cadena = str(a - b)
            elif nombre== "btn_mult":
                cadena = str(a * b)
            else:
                cadena = str(a / b)

            self.txt_result.setText(cadena)
        except Exception as error:
         print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())