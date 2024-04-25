import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P13_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signal
        self.Lexiss.clicked.connect(self.clicklex)
        self.Lexiss.toggled.connect(self.toggle_lex)
        self.Lexiss_2.clicked.connect(self.clicklex_2)
        self.Lexiss_2.toggled.connect(self.toggle_lex_2)
        self.Lexiss_3.clicked.connect(self.clicklex_3)
        self.Lexiss_3.toggled.connect(self.toggle_lex_3)
        self.Lexiss_4.clicked.connect(self.clicklex_4)
        self.Lexiss_4.toggled.connect(self.toggle_lex_4)


    # Área de los Slots
    def clicklex(self):
        self.txt_esclavo.setText("Why are u touching my chilito")

    def toggle_lex(self):
        estado= self.Lexiss.isChecked
        print(f"lex cambio de estado, nuevo estado:{estado}")

    def clicklex_2(self):
        self.txt_esclavo.setText("Streams los sabados")

    def toggle_lex_2(self):
        estado= self.Lexiss.isChecked
        print(f"nati cambio de estado, nuevo estado:{estado}")
    def clicklex_3(self):
        self.txt_esclavo.setText("Diamanco pa")

    def toggle_lex_3(self):
        estado= self.Lexiss.isChecked
        print(f"dodigo cambio de estado, nuevo estado:{estado}")

    def clicklex_4(self):
        self.txt_esclavo.setText("Valo wey")

    def toggle_lex_4(self):
        estado= self.Lexiss.isChecked
        print(f"vicky cambio de estado, nuevo estado:{estado}")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())