import sys
from PyQt5 import uic, QtWidgets, QtCore , QtGui
qtCreatorFile = "P11_SlidersWithtimers.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.Btn_Iniciar.clicked.connect(self.iniciar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.carrussel)

        self.lista_imagenes =[
            ":/Imagenes/Media/lesis.jpg",
            ":/Imagenes/Media/nati.jpg",
            ":/Imagenes/Media/dodigo.jpg",
            ":/Imagenes/Media/vicky.jpg",
            ":/Imagenes/Media/__voyager_reverse_1999_drawn_by_konohana_weibo__c0e7302d2c1ba8e61c6305cb504bed5e.jpg"
        ]




    # Área de los Slots
    def iniciar(self):
        t = self.Btn_Iniciar.text()
        if t =="Iniciar":
            self.Btn_Iniciar.setText("Detener")
            self.idx = 0
            self.segundoPlano.start(1000)
        else:
            self.Btn_Iniciar.setText("Iniciar")
            self.segundoPlano.stop()

    def carrussel(self):
        self.Imagenes.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.idx]))
        self.idx=(self.idx+1)%len(self.lista_imagenes)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())