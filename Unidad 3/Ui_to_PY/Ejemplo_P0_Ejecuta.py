import sys

from Ui_to_PY import  P1_EJEMPLO
from PyQt5 import uic, QtWidgets


class MyApp(QtWidgets.QMainWindow, P1_EJEMPLO.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        P1_EJEMPLO.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.lineEdit


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())