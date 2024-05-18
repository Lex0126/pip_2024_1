import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtMultimedia import QSound
from Proyecto import prueba, prueba3

qtCreatorFile3 = "Menu.ui"
Ui_MainWindow, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.color_jugador = "yellow"
        self.dificultad_juego = 400

        self.btn_Jugar.clicked.connect(self.iniciar)
        self.btn_Personalizar.clicked.connect(self.pers)
        self.Sonido()


    def iniciar(self):
        self.dialog = prueba.MyDialog(color_jugador=self.color_jugador , dificultad_juego=self.dificultad_juego)
        self.dialog.setModal(True)
        self.dialog.show()

    def pers(self):
        self.dialog = prueba3.MyDialogP()
        self.dialog.color_signal.connect(self.recibir_color)
        self.dialog.dificultad_signal.connect(self.recibir_dificultad)
        self.dialog.setModal(True)
        self.dialog.show()

    def recibir_color(self, color):
        self.color_jugador = color

    def recibir_dificultad(self, dificultad):
        self.dificultad_juego = dificultad
    def Sonido(self):
        sound_file = "C:/Users/lexis/OneDrive/Escritorio/pip_2024_1/Unidad 1/Media(1)/Enemy Attack - Reverse： 1999 Soundtrack Extended.wav"
        try:
            QSound.play(sound_file)
            print("reproduciendo audio")
        except Exception as e:
            print("Error al reproducir el sonido:", e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


###################################################3

