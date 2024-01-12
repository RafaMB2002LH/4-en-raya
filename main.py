import random
import math
import os

class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(16)]
        if random.randint(0, 1) == 1:
            self.humanPLayer = 'X'
            self.botPlayer = "O"
        else:
            self.humanPLayer = "O"
            self.botPlayer = "X"

    def show_board(self):
        print("")
        for i in range(4):
            print("  ",self.board[0+(i*4)]," | ",self.board[1+(i*4)]," | ",self.board[2+(i*4)], " | ", self.board[3+(i*4)])
            print("")
            
    def is_board_filled(self,state):
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

    def checkWinner(self):
        if self.is_player_win(self.board,self.humanPLayer):
            os.system("cls")
            print(f"   Player {self.humanPLayer} wins the game!")
            return True
            
        if self.is_player_win(self.board,self.botPlayer):
            os.system("cls")
            print(f"   Player {self.botPlayer} wins the game!")
            return True

        if self.is_board_filled(self.board):
            os.system("cls")
            print("   Match Draw!")
            return True
        return False

    def start(self):
        bot = ComputerPlayer(self.botPlayer)
        human = humanPLayer(self.humanPLayer)
        while True:
            os.system("cls")
            print(f"   Player {self.humanPLayer} turn")
            self.show_board()
            
            #Human
            square = human.human_move(self.board)
            self.board[square] = self.humanPLayer
            if self.checkWinner():
                break
            
            #Bot
            square = bot.machine_move_alpha_beta(self.board)
            self.board[square] = self.botPlayer
            if self.checkWinner():
                break

        print()
        self.show_board()

class humanPLayer:
    def __init__(self,letter):
        self.letter = letter
    
    def human_move(self,state):
        while True:
            square =  int(input("Enter the square to fix spot(1-16): "))
            print()
            if state[square-1] == "-":
                break
        return square-1

class ComputerPlayer(TicTacToe):
    def __init__(self,letter):
        self.botPlayer = letter
        self.humanPlayer = "X" if letter == "O" else "O"

    def players(self,state):
        n = len(state)
        x = 0
        o = 0
        for i in range(16):
            if(state[i] == "X"):
                x = x+1
            if(state[i] == "O"):
                o = o+1
        
        if(self.humanPlayer == "X"):
            return "X" if x==o else "O"
        if(self.humanPlayer == "O"):
            return "O" if x==o else "X"
    
    def actions(self,state):
        return [i for i, x in enumerate(state) if x == "-"]
    
    def result(self,state,action):
        newState = state.copy()
        player = self.players(state)
        newState[action] = player
        return newState
    
    def terminal(self,state):
        if(self.is_player_win(state,"X")):
            return True
        if(self.is_player_win(state,"O")):
            return True
        return False

    def minimax_alpha_beta(self, state, player, alfa, beta):
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
            newState = self.result(state, possible_move)
            sim_score = self.minimax_alpha_beta(newState, other_player, alfa, beta)

            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                alfa = max(alfa, best['score'])
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, best['score'])

            if beta <= alfa:
                break

        return best

    def machine_move_alpha_beta(self, state):
        square = self.minimax_alpha_beta(state, self.botPlayer, -math.inf, math.inf)['position']
        return square

tic_tac_toe = TicTacToe()
tic_tac_toe.start()