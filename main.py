#Imports
import random
import os
from human_player import HumanPlayer
from computer_player import ComputerPlayer

#Clase del 4 en raya
class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(16)]
        if random.randint(0, 1) == 1:
            self.humanPlayer = 'X'
            self.botPlayer = "O"
        else:
            self.humanPlayer = "O"
            self.botPlayer = "X"

    #Esta funcion muestra el tablero
    def show_board(self):
        print("")
        for i in range(4):
            print("  ", self.board[0 + (i * 4)], " | ", self.board[1 + (i * 4)], " | ", self.board[2 + (i * 4)], " | ",self.board[3 + (i * 4)])
            print("")

    #Esta funcion te dice si el tablero esta lleno    
    def is_board_filled(self, state):
        return not "-" in state

    #En esta funcion defino como estan colocadas las casillas para ver si ha ganado algun jugador
    def is_player_win(self, state, player):
        # Ganar horizontal
        if state[0] == state[1] == state[2] == state[3] == player: return True
        if state[4] == state[5] == state[6] == state[7] == player: return True
        if state[8] == state[9] == state[10] == state[11] == player: return True
        if state[12] == state[13] == state[14] == state[15] == player: return True

        # Ganar vertical
        if state[0] == state[4] == state[8] == state[12] == player: return True
        if state[1] == state[5] == state[9] == state[13] == player: return True
        if state[2] == state[6] == state[10] == state[14] == player: return True
        if state[3] == state[7] == state[11] == state[15] == player: return True

        # Ganar diagonal
        if state[0] == state[5] == state[10] == state[15] == player: return True
        if state[12] == state[9] == state[6] == state[3] == player: return True

        return False

    #En esta funcion chequeo el ganador y muestro los mensajes
    def check_winner(self):
        if self.is_player_win(self.board, self.humanPlayer):
            os.system("cls")
            print(f"   ¡Jugador Humano ({self.humanPlayer}) gana el juego!")
            return True

        if self.is_player_win(self.board, self.botPlayer):
            os.system("cls")
            print(f"   ¡Jugador IA ({self.botPlayer}) gana el juego!")
            return True

        # Comprobar si el juego está empatado o no
        if self.is_board_filled(self.board):
            os.system("cls")
            print("   ¡Empate!")
            return True
        return False
    
    #En esta funcion comienzo el programa
    def start(self):
        bot = ComputerPlayer(self.botPlayer)
        human = HumanPlayer(self.humanPlayer)
        while True:
            os.system("cls")
            print(f"   Turno del Jugador Humano ({self.humanPlayer})")
            self.show_board()

            # Humano
            square = human.human_move(self.board)
            self.board[square] = self.humanPlayer
            if self.check_winner():
                break

            # IA
            if self.count_empty_squares() > 10:
                # Aleatorio cuando hay más de 10 casillas vacías
                empty_squares = [i for i, x in enumerate(self.board) if x == "-"]
                square = random.choice(empty_squares)
                print(f"   Jugador IA ({self.botPlayer}) elige aleatoriamente la casilla {square + 1}")
            else:
                # Minimax cuando quedan 10 o menos casillas vacías
                square = bot.machine_move(self.board)
                print(f"   Jugador IA ({self.botPlayer}) elige la casilla {square + 1} con Minimax")

            self.board[square] = self.botPlayer
            if self.check_winner():
                break

        # Mostrar la vista final del tablero
        print()
        self.show_board()

    #En esta funcion cuento las casillas vacias
    def count_empty_squares(self):
        return self.board.count('-')

#Inicio de programa
if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
