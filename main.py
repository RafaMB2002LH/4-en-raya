#Imports
import random
import math
import os
import time

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
        self.move_times = []

    #Esta funcion muestra el tablero
    def show_board(self):
        print("")
        for i in range(4):
            print("  ", self.board[0 + (i * 4)], " | ", self.board[1 + (i * 4)], " | ", self.board[2 + (i * 4)], " | ",
                  self.board[3 + (i * 4)])
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
            print(f"   El jugador {self.humanPlayer} gana la partida!")
            return True

        if self.is_player_win(self.board, self.botPlayer):
            os.system("cls")
            print(f"   El jugador {self.botPlayer} gana la partida!")
            return True

        # Comprobar si el juego está empatado o no
        if self.is_board_filled(self.board):
            os.system("cls")
            print("   Empate!")
            return True
        return False

    #En esta funcion comienzo el programa
    def start(self):
        bot = ComputerPlayer(self.botPlayer)
        human = HumanPlayer(self.humanPlayer)
        while True:
            os.system("cls")
            print(f"   Turno del jugador {self.humanPlayer}")
            self.show_board()

            # Humano
            square = human.human_move(self.board)
            self.board[square] = self.humanPlayer
            if self.check_winner():
                break

            # IA
            start_time = time.time()
            if self.count_empty_squares() > 10:
                # Aleatorio cuando hay más de 10 casillas vacías
                empty_squares = [i for i, x in enumerate(self.board) if x == "-"]
                square = random.choice(empty_squares)
            else:
                # Minimax cuando quedan 10 o menos casillas vacías
                square = bot.machine_move(self.board)

            end_time = time.time()  # Registrar el tiempo de finalización
            move_time = end_time - start_time
            self.move_times.append(move_time)

            self.board[square] = self.botPlayer
            if self.check_winner():
                break

        # Mostrar la vista final del tablero
        print()
        self.show_board()

        # Mostrar los tiempos de movimiento de la IA al finalizar
        print("\nTiempos de movimiento de la IA:")
        for i, move_time in enumerate(self.move_times, start=1):
            print(f"Movimiento {i}: {move_time:.5f} segundos")

    #En esta funcion cuento las casillas vacias
    def count_empty_squares(self):
        return self.board.count('-')

#Esta clase define el jugador humano
class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    #Esta funcion pide los movimientos al humano
    def human_move(self, state):
        # Entrada del usuario
        while True:
            square = int(input("Ingrese la casilla(1-16): "))
            print()
            if state[square - 1] == "-":
                break
        return square - 1

#Esta clase define la IA
class ComputerPlayer(TicTacToe):
    def __init__(self, letter):
        self.botPlayer = letter
        self.humanPlayer = "X" if letter == "O" else "O"

    #Esta funcion guarda los jugadores
    def players(self, state):
        n = len(state)
        x = 0
        o = 0
        for i in range(16):
            if state[i] == "X":
                x = x + 1
            if state[i] == "O":
                o = o + 1

        if self.humanPlayer == "X":
            return "X" if x == o else "O"
        if self.humanPlayer == "O":
            return "O" if x == o else "X"

    #Esta funcion realiza las acciones
    def actions(self, state):
        return [i for i, x in enumerate(state) if x == "-"]

    #Esta funcion va guardando el estado del tablero
    def result(self, state, action):
        new_state = state.copy()
        player = self.players(state)
        new_state[action] = player
        return new_state

    #Esta funcion determina cuando termina la partida
    def terminal(self, state):
        if self.is_player_win(state, "X"):
            return True
        if self.is_player_win(state, "O"):
            return True
        return False

    #Algoritmo MINIMAX para colocar las fichas en la mejor casilla para mayor posibilidad de victoria para la IA
    def minimax(self, state, player):
        max_player = self.humanPlayer  # Tu mismo
        other_player = 'O' if player == 'X' else 'X'

        if self.terminal(state):
            return {'position': None, 'score': 1 * (len(self.actions(state)) + 1) if other_player == max_player else -1 * (
                        len(self.actions(state)) + 1)}
        elif self.is_board_filled(state):
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for possible_move in self.actions(state):
            new_state = self.result(state, possible_move)
            sim_score = self.minimax(new_state, other_player)

            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

    #Esta funcion coloca las fichas a la IA
    def machine_move(self, state):
        return self.minimax(state, self.botPlayer)['position']


#Inicio de programa
if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()