import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P4_Dial.ui"  # Nombre del archivo aquí.
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
        self.Dial_Personas.setMinimum (1)
        self.Dial_Personas.setMaximum (6)
        self.Dial_Personas.setSingleStep (1)
        self.Dial_Personas.setValue (1)
        self.Dial_Personas.valueChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        dataclave =self.Dial_Personas.value()
        imagen=self.datos_equipo[dataclave][-1]
        self.Img_Personas.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())