import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.CB_lex.toggled.connect(self.sel_lex)
        self.CB_Nat.toggled.connect(self.sel_nat)
        self.CB_dodigo.toggled.connect(self.sel_dodigo)
        self.CB_vic.toggled.connect(self.sel_vic)

        self.lex =""
        self.nat =""
        self.dodigo = ""
        self.vic =""



    # Área de los Slots

    def sel_lex(self):
        if self.CB_lex.isChecked():
            print("Lex true")
            self.lex= "lex me gusta el mole\n"
        else:
            print("lex false")
            self.lex =""
        self.Txt_Equipo.setPlainText(self.lex+self.nat+self.dodigo+self.vic)
    def sel_nat(self):
        if self.CB_Nat.isChecked():
            print("nati true")
            self.nat= "Nati le gusta las quesadillas de choriqueso\n"
        else:
            print("nati false")
            self.nat =""
        self.Txt_Equipo.setPlainText(self.lex+self.nat+self.dodigo+self.vic)

    def sel_dodigo(self):
        if self.CB_dodigo.isChecked():
            print("dodigo true")
            self.dodigo ="dodigo no le gustan las empanadas\n"
        else:
            print("dodigo false")
            self.dodigo= ""
        self.Txt_Equipo.setPlainText(self.lex+self.nat+self.dodigo+self.vic)
    def sel_vic(self):
        if self.CB_vic.isChecked():
            print("vic true")
            self.vic ="vicky le gustan las empanadas\n"
        else:
            print("vicky false")
            self.vic= ""
        self.Txt_Equipo.setPlainText(self.lex+self.nat+self.dodigo+self.vic)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())