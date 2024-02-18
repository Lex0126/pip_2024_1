import sys
import statistics
from PyQt5 import uic, QtWidgets
from PyQt5.QtMultimedia import QSound
qtCreatorFile = "Proyecto_Programacion de puerto_U1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_valor_mayor.clicked.connect(self.Operacion)
        self.btn_valor_menor.clicked.connect(self.Operacion)
        self.btn_media.clicked.connect(self.Operacion)
        self.btn_mediana.clicked.connect(self.Operacion)
        self.btn_moda.clicked.connect(self.Operacion)
        self.btn_desviacion.clicked.connect(self.Operacion)
        self.btn_varianza.clicked.connect(self.Operacion)
        self.btn_clean.clicked.connect(self.Clean)
        self.btn_easter_egg.clicked.connect(self.close)

    # Área de los Slots
    def Clean(self):
        self.txt_numeros.clear()
        self.txt_result.clear()

    def Operacion(self):
        try:
            objeto = self.sender()
            nombre= objeto.objectName()
            numeros = self.txt_numeros.text()
            lista = numeros.split(" ")
            'print(lista)'
            lista_en_numeros = [int(i) for i in lista]
            'print(lista_en_numeros)'


            if nombre== "btn_valor_mayor":
                cadena ="el numero de valor mayor es: "+str(max(lista_en_numeros))
            elif nombre== "btn_valor_menor":
                cadena = "el numero de valor mayor es: "+str(min(lista_en_numeros))
            elif nombre== "btn_media":
                cadena = "la media es: "+str(statistics.mean(lista_en_numeros))
            elif nombre== "btn_mediana":
                mediana = statistics.median(lista_en_numeros)
                mediana_redondeada= round(mediana,2)
                cadena="la mediana es: "+str(mediana_redondeada)
            elif nombre== "btn_moda":
                cadena="la moda es :"+str(statistics.mode(lista_en_numeros))
            elif nombre== "btn_desviacion":
                desviacion_estandar = statistics.stdev(lista_en_numeros)
                desviacion_estandar_redondeada = round(desviacion_estandar, 2)
                cadena = "La desviación estándar es: " + str(desviacion_estandar_redondeada)
            elif nombre== "btn_varianza":
                cadena="la varianza es :"+str(statistics.variance(lista_en_numeros))

            self.txt_result.setText(cadena)
        except Exception as error:
         print(error)

    def close(self):
        sound_file = "C:/Users/lexis/OneDrive/Escritorio/pip_2024_1/Unidad 1/Media(1)/kuru-kuru-herta-made-with-Voicemod.wav"
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