import sys


from PyQt5 import uic, QtWidgets

from Graficacion import Plantilla_Grafica as interfaz
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.pushButton_2.clicked.connect(self.graficar)
        self.pushButton.clicked.connect(self.titulo)
        self.pushButton_3.clicked.connect(self.grilla)
        self.pushButton_4.clicked.connect(self.limpiar)

        self.comboBox_2.addItem("Estilo: :",":")
        self.comboBox_2.addItem("Estilo: -", "-")
        self.comboBox_2.addItem("Estilo: --", "--")
        self.comboBox_2.addItem("Estilo: -.", "-.")
        self.comboBox_2.currentIndexChanged.connect(self.estiloLinea)

        self.comboBox.addItem("Negro","Black")
        self.comboBox.addItem("Rojo", "Red")
        self.comboBox.addItem("Azul", "Blue")
        self.comboBox.addItem("Verde", "green")
        self.comboBox.currentIndexChanged.connect(self.colorLinea)

        self.spinBox_5.setValue(1)
        self.spinBox_5.setMaximum(10)
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setSingleStep(1)
        self.spinBox_5.valueChanged.connect(self.anchoLinea)







    # Área de los Slots
    def  graficar(self):
        pass
    def  titulo(self):
        pass
    def  grilla(self):
        pass
    def  limpiar(self):
        pass
    def  colorLinea(self):
        pass
    def  anchoLinea(self):
        pass
    def  estiloLinea(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())