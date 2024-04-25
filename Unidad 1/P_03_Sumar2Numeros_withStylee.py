import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_Sumar2Numeros_withStylee.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_Suma.setEnabled(False)

    # Área de los Slots
    def sumar(self):
        a = float(self.txt_A.text())
        b = float(self.txt_B.text())
        cadena=str(a+b)

        self.txt_Suma.setText(cadena)
        self.txt_A.clear()
        self.txt_B.clear()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())