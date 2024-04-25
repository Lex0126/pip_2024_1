import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_Combobox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_equipo = {
            1: ["Lexiss", "Dibujar", 21, "O-", ":/Imagenes/Media/lesis.jpg"],
            2: ["Nati", "Streamear", 20, "O-", ":/Imagenes/Media/nati.jpg"],
            3: ["Dodigo", "ValoPlayer", 20, "O-", ":/Imagenes/Media/dodigo.jpg"],
            4: ["Victorin", "Formula", 20, "O-", ":/Imagenes/Media/vicky.jpg"],
            5: ["Voyager", "Violin", 18, "O-",
                ":/Imagenes/Media/__voyager_reverse_1999_drawn_by_konohana_weibo__c0e7302d2c1ba8e61c6305cb504bed5e.jpg"],

        }
        self.CBO_persona.addItem("Lex",1)
        self.CBO_persona.addItem("Nati", 2)
        self.CBO_persona.addItem("Dodigo", 3)
        self.CBO_persona.addItem("Vic", 4)
        self.CBO_persona.addItem("Voyager", 5)

        self.CBO_persona.currentIndexChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        print("Text"+self.CBO_persona.currentText())
        print("index"+str(self.CBO_persona.currentIndex()))
        print("Data" + str(self.CBO_persona.currentData()))

        dataclave =self.CBO_persona.currentData()
        imagen=self.datos_equipo[dataclave][-1]
        self.Img_Persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())