import random
import os

class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(16)]
        if random.randint(0, 1) == 1:
            self.humanPlayer = 'X'
            self.botPlayer = 'O'
        else:
            self.humanPlayer = 'O'
            self.botPlayer = 'X'
        
    def show_board(self):
        print("")
        for i in range(4):
            print(" ",self.board[0+(i*4)], " | ", self.board[1+(i*4)], " | ", self.board[2+(i*4)], " | ",self.board[3+(i*4)])
            print("")
    
    def is_board_filled(self, state):
        return not "-" in state
    
    def is_player_win(self, state, player):
        #Gana horizontal
        if state[0]==state[1]==state[2]==state[3]== player: return True
        if state[4]==state[5]==state[6]==state[7]== player: return True
        if state[8]==state[9]==state[10]==state[11]== player: return True
        if state[12]==state[13]==state[14]==state[15]== player: return True
        #Gana vertical
        if state[0]==state[4]==state[8]==state[12]== player: return True
        if state[1]==state[5]==state[9]==state[13]== player: return True
        if state[2]==state[6]==state[10]==state[14]== player: return True
        if state[3]==state[7]==state[11]==state[15]== player: return True
        #Gana diagonal
        if state[0]==state[5]==state[10]==state[15]== player: return True
        if state[12]==state[9]==state[6]==state[3]== player: return True

        return False
    
    def check_winner(self):
        if self.is_player_win(self.board, self.humanPlayer):
            os.system("cls")
            print(f" Player {self.humanPlayer} wins the game!")
            return True
        
        if self.is_player_win(self.board, self.botPlayer):
            os.system("cls")
            print(f" Player {self.botPlayer} wins the game!")
            return True
        
        if self.is_board_filled(self.board):
            os.system("cls")
            print(" Match Draw!")
            return True
        
        return False
    
    def start(self):
        human = humanPlayer(self.humanPlayer)

        while True:
            print(f" Player {self.humanPlayer} turn")
            self.show_board()

            square = human.human_move(self.board)
            self.board[square] = self.humanPlayer

            if self.check_winner():
                break

class humanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def human_move(self, state):
        while True:
            square = int(input("Enter the square to fix spot(1-16): "))
            print()
            if state[square-1] == "-":
                break

        return square-1
    

tictactoe = TicTacToe()
tictactoe.start()
