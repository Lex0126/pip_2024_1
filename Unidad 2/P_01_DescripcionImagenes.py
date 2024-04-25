import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QSound
qtCreatorFile = "P1_DescripcionImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_equipo= {
            1:["Lexiss","Dibujar",21,"O-",":/Imagenes/Media/lesis.jpg"],
            2: ["Nati", "Streamear", 20, "O-",":/Imagenes/Media/nati.jpg"],
            3: ["Dodigo", "ValoPlayer", 20, "O-",":/Imagenes/Media/dodigo.jpg"],
            4: ["Victorin", "Formula", 20, "O-",":/Imagenes/Media/vicky.jpg"],
            5: ["Voyager", "Violin", 18, "O-",":/Imagenes/Media/__voyager_reverse_1999_drawn_by_konohana_weibo__c0e7302d2c1ba8e61c6305cb504bed5e.jpg"],

        }
        self.Btn_Atras.clicked.connect(self.atras)
        self.Btn_Adelante.clicked.connect(self.adelante)
        self.index_control= 0
        self.Btn_Atras.setEnabled(False)
        self.Btn_Abrir.clicked.connect(self.abrir_gif_y_sonido)

    # Área de los Slots
    def atras(self):
        if self.index_control >1:
            self.index_control -=1
            datos = self.datos_equipo[self.index_control]
            self.Btn_Adelante.setEnabled(True)
            self.Img_Persona.setPixmap(QtGui.QPixmap(datos[-1]))
            self.Txt_Nombre.setText(datos[0])
            self.Txt_PasaTiempo.setText(datos[1])
            self.Txt_Edad.setText(str(datos[2]))
            self.Txt_TipoSangre.setText(datos[3])

        if self.index_control==1:
            self.Btn_Atras.setEnabled(False)
    def adelante(self):
        if self.index_control <=6:
            self.index_control +=1
            datos = self.datos_equipo[self.index_control]
            self.Btn_Atras.setEnabled(True)
            self.Img_Persona.setPixmap(QtGui.QPixmap(datos[-1]))
            self.Txt_Nombre.setText(datos[0])
            self.Txt_PasaTiempo.setText(datos[1])
            self.Txt_Edad.setText(str(datos[2]))
            self.Txt_TipoSangre.setText(datos[3])
        if self.index_control==5:
            self.Btn_Adelante.setEnabled(False)

    def abrir_gif_y_sonido(self):
        print("Reproduciendo sonido...")
        QSound.play(
            "C:/Users/lexis/OneDrive/Escritorio/pip_2024_1/Unidad 1/Media(1)/gojo-made-with-Voicemod.wav")  # Ruta al archivo de sonido
        print("Sonido terminado.")

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("GIF")
        label = QtWidgets.QLabel()
        movie = QtGui.QMovie(
            "C:/Users/lexis/OneDrive/Escritorio/pip_2024_1/Unidad 1/Media(1)/gojo-satoru-sukuna.gif")  # Ruta al archivo GIF
        label.setMovie(movie)
        movie.start()

        msgBox.layout().addWidget(label)
        msgBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())