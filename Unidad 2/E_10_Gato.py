import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_10_Gato.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #estado del tablero actual que es vacio
        self.board = [''] * 9
        #ponemos que nuestro jugador siempre empezara con el X
        self.current_player ='X'
        #creamos funciones anonimas y conectamos a cada boton con su respectivo argumento( osea indicamos la celda a la que pertenece)
        self.PUSH1.clicked.connect(lambda: self.on_click(0))
        self.PUSH2.clicked.connect(lambda: self.on_click(1))
        self.PUSH3.clicked.connect(lambda: self.on_click(2))
        self.PUSH4.clicked.connect(lambda: self.on_click(3))
        self.PUSH5.clicked.connect(lambda: self.on_click(4))
        self.PUSH6.clicked.connect(lambda: self.on_click(5))
        self.PUSH7.clicked.connect(lambda: self.on_click(6))
        self.PUSH8.clicked.connect(lambda: self.on_click(7))
        self.PUSH9.clicked.connect(lambda: self.on_click(8))
        self.PUSHRESET_2.clicked.connect(self.reset_game)

    # Área de los Slots
    def on_click(self, cell_index):
        #checamos si hay celdas vacias
        if not self.board[cell_index]:
            #agregamos al jugador en la celda en la que dimos el click segun la posicion
            self.board[cell_index] = self.current_player
            PUSH = getattr(self, f'PUSH{cell_index + 1}')
            PUSH.setText(self.current_player)
            #checamos si hay un ganador mediante la funcion que tenemos de check winne
            if self.check_winner():
                self.ganador_LB.setText("¡Fin del juego!" f"El jugador {self.current_player} ha ganado.")

                return

           # cambiamos al siguiente jugador diciendo cambia de x a o si es x y si no es X o sea si es O lo cambia a X
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
            (0, 4, 8), (2, 4, 6)  # Diagonales
        ]
        #verificamos si alguna de las combinaciones es posible en el tablero y si si marca un true que significa que hay un ganador y si no no hay ninguno
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    def reset_game(self):
        # Reinicia el estado del tablero y los botones
        self.board = [''] * 9
        for i in range(1, 10):# se ejecutara 9 veces y se accedera a cada boton en este caso son 9
            PUSH = getattr(self, f'PUSH{i}') #getattr funciona para los que siguen un patron de nombre podemos obtenerlos de forma dinamica en un bucle(lo hacemos durante que ejecutamos el codigo y no de forma estatica en el desarrollo)
            PUSH.setText('')
        self.current_player = 'X'
        self.ganador_LB.setText(" ")
    def Clean_Text(self):
        #limpiamos el texto
        self.reset_game()
        self.ganador_LB.setText(" ")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())