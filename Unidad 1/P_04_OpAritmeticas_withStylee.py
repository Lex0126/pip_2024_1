import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpAritmeticas_withStylee.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_restar.clicked.connect(self.restar)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_division.clicked.connect(self.div)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def sumar(self):
        a = float(self.txt_A.text())
        b = float(self.txt_B.text())
        cadena=str(a+b)

        self.txt_result.setText(cadena)
    def restar(self):
        a = float(self.txt_A.text())
        b = float(self.txt_B.text())
        cadena=str(a-b)

        self.txt_result.setText(cadena)
    def mult(self):
        a = float(self.txt_A.text())
        b = float(self.txt_B.text())
        cadena=str(a*b)

        self.txt_result.setText(cadena)
    def div(self):
        a = float(self.txt_A.text())
        b = float(self.txt_B.text())
        cadena=str(a/b)

        self.txt_result.setText(cadena)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())