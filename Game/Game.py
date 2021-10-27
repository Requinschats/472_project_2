import time

import Game.selectors as s
import Game.outputs as o
import Game.constants as c


class Game:
    MINIMAX, ALPHABETA = 0, 1
    HUMAN, AI = 2, 3

    def __init__(self, recommend=True):
        self.initialize_game()
        self.recommend = recommend

    def initialize_game(self):
        self.current_state = s.select_initial_state()
        self.player_turn = s.select_inital_player()

    def draw_board(self):
        o.draw_game_board(self)

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != c.EMPTY_TOKEN:
            return False
        else:
            return True

    def is_end(self):
        return s.select_is_end(self)

    def check_end(self):
        self.result = self.is_end()
        end_game_output = s.select_end_game_output(self)
        print(end_game_output)
        if self.result is not None:
            self.initialize_game()
        return self.result

    def input_move(self):
        while True:
            print(F'Player {self.player_turn}, enter your move:')
            px = int(input('enter the x coordinate: '))
            py = int(input('enter the y coordinate: '))
            if self.is_valid(px, py):
                return (px, py)
            else:
                print('The move is not valid! Try again.')

    def switch_player(self):
        return s.select_next_player(self)

    # Minimizing for 'X' and maximizing for 'O'
    def minimax(self, max=False):
        game_result = 2 if not max else -2  # -1 = X wins, 1 = X loss
        x, y = None, None
        end_game = s.select_end_game(self.is_end(), x, y)

        if end_game:
            return end_game

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        (minimax_result, _, _) = self.minimax(max=False)
                        if minimax_result > game_result:
                            game_result = minimax_result
                            x = i
                            y = j
                    else:
                        self.current_state[i][j] = 'X'
                        (minimax_result, _, _) = self.minimax(max=True)
                        if minimax_result < game_result:
                            game_result = minimax_result
                            x = i
                            y = j
                    self.current_state[i][j] = '.'
        return game_result, x, y

    # Minimizing for 'X' and maximizing for 'O'
    def alphabeta(self, alpha=-2, beta=2, max=False):
        value = 2 if not max else -2
        x, y = None, None
        end_game = s.select_end_game(self.is_end(), x, y)

        if end_game:
            return end_game

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        (alphabeta_result, _, _) = self.alphabeta(alpha, beta, max=False)
                        if alphabeta_result > value:
                            value = alphabeta_result
                            x, y = i, j
                    else:
                        self.current_state[i][j] = 'X'
                        (alphabeta_result, _, _) = self.alphabeta(alpha, beta, max=True)
                        if alphabeta_result < value:
                            value = alphabeta_result
                            x, y = i, j
                    self.current_state[i][j] = '.'
                    if max:
                        if value >= beta:
                            return (value, x, y)
                        if value > alpha:
                            alpha = value
                    else:
                        if value <= alpha:
                            return (value, x, y)
                        if value < beta:
                            beta = value
        return (value, x, y)

    def play(self, algo=None, player_x=None, player_o=None):
        if algo == None:
            algo = self.ALPHABETA
        if player_x == None:
            player_x = self.HUMAN
        if player_o == None:
            player_o = self.HUMAN
        while True:
            self.draw_board()
            if self.check_end():
                return
            start = time.time()
            if algo == self.MINIMAX:
                if self.player_turn == 'X':
                    (_, x, y) = self.minimax(max=False)
                else:
                    (_, x, y) = self.minimax(max=True)
            else:  # algo == self.ALPHABETA
                if self.player_turn == 'X':
                    (m, x, y) = self.alphabeta(max=False)
                else:
                    (m, x, y) = self.alphabeta(max=True)
            end = time.time()
            if (self.player_turn == 'X' and player_x == self.HUMAN) or (
                    self.player_turn == 'O' and player_o == self.HUMAN):
                if self.recommend:
                    print(F'Evaluation time: {round(end - start, 7)}s')
                    print(F'Recommended move: x = {x}, y = {y}')
                (x, y) = self.input_move()
            if (self.player_turn == 'X' and player_x == self.AI) or (
                    self.player_turn == 'O' and player_o == self.AI):
                print(F'Evaluation time: {round(end - start, 7)}s')
                print(F'Player {self.player_turn} under AI control plays: x = {x}, y = {y}')
            self.current_state[x][y] = self.player_turn
            self.switch_player()
