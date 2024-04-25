import sys
from PyQt5 import uic, QtWidgets, QtCore, QtMultimedia
qtCreatorFile = "E_02_Simulacion de una alarma.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizar)
        self.timer.start(1000)

        self.Btn_set_alarm.clicked.connect(self.establecer_alarma)
        self.Btn_status_alarm.clicked.connect(self.Status_alarma)

        self.alarma_activa = False

        self.sonido= QtMultimedia.QSoundEffect()
        self.sonido.setSource(QtCore.QUrl.fromLocalFile("C:/Users/lexis/OneDrive/Escritorio/pip_2024_1/Unidad 1/Media(1)/kuru-kuru-herta-made-with-Voicemod.wav"))

    # Área de los Slots
    def actualizar(self):
        tiempo_actual = QtCore.QTime.currentTime().toString("hh:mm")
        self.label_hora.setText(tiempo_actual)

        if self.alarma_activa:
            alarma_actual = self.timeEdit_alarm.time().toString("hh:mm")
            if tiempo_actual == alarma_actual:
                self.sonido.play()
                self.mostrar("¡Alarma!")
                self.Status_alarma()


    def establecer_alarma(self):
        tiempo_alarma = self.timeEdit_alarm.time().toString("hh:mm")
        self.mostrar(f"Alarma establecida a las {tiempo_alarma}")

    def Status_alarma(self):
        self.alarma_activa = not self.alarma_activa
        if self.alarma_activa:
            self.Btn_status_alarm.setText("Desactivar Alarma")
        else:
            self.Btn_status_alarm.setText("Activar Alarma")

    def mostrar(self, mensaje):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Alarma")
        msgBox.setText(mensaje)
        msgBox.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())