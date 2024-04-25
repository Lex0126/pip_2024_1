import sys
from PyQt5 import uic, QtWidgets, QtCore , QtGui
qtCreatorFile = "P12_CompararImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.Btn_Iniciar.clicked.connect(self.iniciar)
        self.Btn_Atras.clicked.connect(self.atras)
        self.Btn_Siguiente.clicked.connect(self.siguiente)
        self.index_control = 0
        self.Btn_Atras.setEnabled(False)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.carrussel)

        self.Btn_validar.clicked.connect(self.validar)

        self.lista_imagenes =[
            ":/Imagenes/Media/lesis.jpg",
            ":/Imagenes/Media/nati.jpg",
            ":/Imagenes/Media/dodigo.jpg",
            ":/Imagenes/Media/vicky.jpg",
            ":/Imagenes/Media/__voyager_reverse_1999_drawn_by_konohana_weibo__c0e7302d2c1ba8e61c6305cb504bed5e.jpg"
        ]




    # Área de los Slots
    def validar(self):
        res= self.index_control == self.idx
        msj= QtWidgets.QMessageBox()
        msj.setText(str(res))
        msj.exec_()
    def iniciar(self):
        t = self.Btn_Iniciar.text()
        if t =="Iniciar":
            self.Btn_Iniciar.setText("Detener")
            self.idx = 0
            self.segundoPlano.start(80)
        else:
            self.Btn_Iniciar.setText("Iniciar")
            self.segundoPlano.stop()

    def carrussel(self):
        self.idx = (self.idx + 1) % len(self.lista_imagenes)
        self.Imagenes_PC.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.idx]))

    def atras(self):
        if self.index_control > -1:
            self.index_control -= 1
            self.Btn_Siguiente.setEnabled(True)
            self.Imagenes_Usuario.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.index_control]))

        if self.index_control == 0:
            self.Btn_Atras.setEnabled(False)
    def siguiente(self):
        if self.index_control < len(self.lista_imagenes)-1:
            self.Btn_Atras.setEnabled(True)
            self.index_control += 1

            self.Imagenes_Usuario.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.index_control]))

        if self.index_control== len(self.lista_imagenes)-1:
            self.Btn_Siguiente.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())