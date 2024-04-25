import sys

from Ui_to_PY import  P2_EJEMPLO as interfaz
from PyQt5 import uic, QtWidgets,QtCore


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lista_nuevo = QtWidgets.QPushButton(self.centralwidget)
        self.lista_nuevo.setGeometry(QtCore.QRect(230,30,200,60))
        self.lista_nuevo.setObjectName("btn_nuevo")

        

        self.lista_nuevo.setText("Nuevo saludo")


    # Área de los Slots
    def saludar(self):
        try:
            self.lineEdit.setText("Hola Mundo")

            self.lista_nuevo.hide()
        except Exception as e :
            print(e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())