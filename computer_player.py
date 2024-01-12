import random
import math

class ComputerPlayer():
    def __init__(self, letter):
        self.botPlayer = letter
        self.humanPlayer = "X" if letter == "O" else "O"

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

    def actions(self, state):
        return [i for i, x in enumerate(state) if x == "-"]

    def result(self, state, action):
        new_state = state.copy()
        player = self.players(state)
        new_state[action] = player
        return new_state

    def terminal(self, state):
        if self.is_player_win(state, "X"):
            return True
        if self.is_player_win(state, "O"):
            return True
        return False

    def minimax(self, state, player):
        max_player = self.humanPlayer
        other_player = 'O' if player == 'X' else 'X'

        if self.terminal(state):
            return {'position': None,
                    'score': 1 * (len(self.actions(state)) + 1) if other_player == max_player else -1 * (
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

    def machine_move(self, state):
        return self.minimax(state, self.botPlayer)['position']