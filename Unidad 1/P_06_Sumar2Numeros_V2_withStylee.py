import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_06_Sum_v2_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_result.setEnabled(False)

    # Área de los Slots
    def sumar(self):
        numeros = self.txt_numeros.text()
        lista=numeros.split(" ")
        print(lista)
        lista_en_numeros = [int (i) for i in lista]
        print(lista_en_numeros)
        suma=sum(lista_en_numeros)
        self.txt_result.setText(str(suma))
        self.txt_numeros.clear()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())