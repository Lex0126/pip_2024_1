import matplotlib.pyplot as plt
import serial
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import QSound
from Proyecto import DesingGame as grafica

import random as rnd
from Proyecto.prueba3 import MyDialogP

class MyDialog(QtWidgets.QDialog, grafica.Ui_Dialog):
    def __init__(self, color_jugador="yellow",dificultad_juego=400):
        super().__init__()
        self.setupUi(self)

        self.color_jugador = color_jugador
        self.dificultad_juego = dificultad_juego

        self.btn_arriba.clicked.connect(self.arriba)
        self.btn_izquierda.clicked.connect(self.izquierda)
        self.btn_derecha.clicked.connect(self.derecha)
        self.btn_abajo.clicked.connect(self.abajo)


        self.xMin, self.xMax = -5, 5
        self.yMin, self.yMax = -5, 5


        self.personajes = [[0, 0], [rnd.randint(self.xMin, self.xMax), rnd.randint(self.yMin, self.yMax)]]


        self.bolitas = [[rnd.randint(self.xMin, self.xMax), rnd.randint(self.yMin, self.yMax)] for _ in range(5)]
        self.bolitas_recolectadas = 0


        self.vida = 2
        self.actualizar_vida()


        self.limpiar()
        self.graficar()


        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mover_enemigo)
        self.timer.start(self.dificultad_juego)

        self.tiempo_Juego = 60
        self.cuentaAtras= QtCore.QTimer(self)
        self.cuentaAtras.timeout.connect(self.tiempoactualizar)
        self.cuentaAtras.start(1000)

        if self.dificultad_juego ==25:
            self.personajes.append([rnd.randint(self.xMin, self.xMax), rnd.randint(self.yMin, self.yMax)])

        self.Conexion = serial.Serial('COM4', 9600)
        self.serial_timer = QtCore.QTimer(self)
        self.serial_timer.timeout.connect(self.leidopapu)
        self.serial_timer.start(100)

    def leidopapu(self):
        if self.Conexion.in_waiting > 0:
            data = self.Conexion.readline().decode().strip()
            print(data)
            try:
                xValue, yValue = map(int, data.split(','))
                self.monito_Arduino(xValue, yValue)
            except ValueError:
                pass

    def monito_Arduino(self, xValue, yValue):
        if xValue > 620:
            self.derecha()
        elif xValue < 608:
            self.izquierda()
        if yValue > 600:
            self.abajo()
        elif yValue < 580:
            self.arriba()


    def tiempoactualizar(self):
        self.tiempo_Juego -=1
        self.Tiempo.setText(str(self.tiempo_Juego))
        if self.tiempo_Juego==0:
            self.cuentaAtras.stop()
            self.ganaste()



    def arriba(self):
        if self.personajes[0][1] < self.yMax:
            self.personajes[0][1] += 1
            self.actualizar_juego()

    def izquierda(self):
        if self.personajes[0][0] > self.xMin:
            self.personajes[0][0] -= 1
            self.actualizar_juego()


    def derecha(self):
        if self.personajes[0][0] < self.xMax:
            self.personajes[0][0] += 1
            self.actualizar_juego()

    def abajo(self):
        if self.personajes[0][1] > self.yMin:
            self.personajes[0][1] -= 1
            self.actualizar_juego()

    def mover_enemigo(self):
        for i in range(len(self.personajes)):
            if i == 0:
                continue  # Saltamos el movimiento del jugador principal
            direccion = rnd.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
            if direccion == 'arriba' and self.personajes[i][1] < self.yMax:
                self.personajes[i][1] += 1
            elif direccion == 'abajo' and self.personajes[i][1] > self.yMin:
                self.personajes[i][1] -= 1
            elif direccion == 'izquierda' and self.personajes[i][0] > self.xMin:
                self.personajes[i][0] -= 1
            elif direccion == 'derecha' and self.personajes[i][0] < self.xMax:
                self.personajes[i][0] += 1
        self.actualizar_juego()
    def actualizar_juego(self):
        self.limpiar()
        self.graficar()
        self.verificar_recoleccion()
        self.perder()

    def verificar_recoleccion(self):
        for bolita in self.bolitas[:]:
            if self.personajes[0] == bolita:
                self.bolitas_recolectadas += 1
                self.Score.setText(str(self.bolitas_recolectadas))
                self.bolitas.remove(bolita)
                if self.bolitas_recolectadas % 15 == 0:
                    self.vida += 1
                    self.Vidas.setText(str(self.vida))
                if not self.bolitas:
                    self.bolitas = [[rnd.randint(self.xMin, self.xMax), rnd.randint(self.yMin, self.yMax)] for _ in range(5)]

    def perder(self):
        if self.personajes[0] == self.personajes[1]:
            self.perder_vida()

    def perder_vida(self):
        if self.vida >= 1:
            self.vida -= 1
            self.actualizar_vida()

        elif self.vida <= 0:
            self.cuentaAtras.stop()
            m = QtWidgets.QMessageBox()
            m.setText("Ya gg Pa")
            self.timer.stop()
            m.exec_()
            self.close()
    def actualizar_vida(self):
        self.Vidas.setText(str(self.vida))
        if self.vida <=0:
            self.perder_vida()
    def ganaste(self):

        m=QtWidgets.QMessageBox()
        m.setText(f"GANASTE PA SI CORRISTE\n Tu puntaje fue de:{self.bolitas_recolectadas}")
        self.timer.stop()
        m.exec_()

        self.close()

    def limpiar(self):
        plt.clf()


        plt.xlim(self.xMin, self.xMax)
        plt.ylim(self.yMin, self.yMax)

        plt.xticks([])
        plt.yticks([])



    def graficar(self):
        plt.gca().set_facecolor('#55aaff')
        plt.plot(self.personajes[0][0], self.personajes[0][1], marker="o", markersize=8,
                 markerfacecolor=self.color_jugador, markeredgewidth=1, markeredgecolor="black", linestyle="None")
        for i in range(1, len(self.personajes)):

            plt.plot(self.personajes[i][0], self.personajes[i][1], marker="o", markersize=8, markerfacecolor="green",
                     markeredgewidth=1, markeredgecolor="black", linestyle="None")

        for bolita in self.bolitas:
            plt.plot(bolita[0], bolita[1], marker="o", markersize=8, markerfacecolor="blue", markeredgewidth=1,
                     markeredgecolor="black", linestyle="None")
        self.canvas.draw()









