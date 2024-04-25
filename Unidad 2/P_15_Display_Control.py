import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer, QTime

qtCreatorFile = "P15_Display_control.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signal
        self.lcdNumber.setNumDigits(8)
        self.update_time()
        self.SetAlarm.clicked.connect(self.setalarm)
        self.CancelAlarm.clicked.connect(self.cancelalarm)

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.checkalarm)

    # Área de los Slots
    def setalarm(self):
        self.alarm_time = self.timeEdit_alarm.time()
        self.timer.start(1000)
        self.SetAlarm.setEnabled(False)
        self.CancelAlarm.setEnabled(True)

    def cancelalarm(self):
        self.timer.stop()
        self.SetAlarm.setEnabled(True)
        self.CancelAlarm.setEnabled(False)

    def checkalarm(self):
        current_time = QTime.currentTime()
        self.update_time()

        if current_time.hour() == self.alarm_time.hour() and current_time.minute() == self.alarm_time.minute():
            QtWidgets.QMessageBox.information(self, "Alarma", "¡Ya es la hora de la alarma!")
            self.cancelalarm()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm")
        self.lcdNumber.display(current_time)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
