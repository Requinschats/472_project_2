import time

import Game.selectors as s
import Game.outputs as o
import Game.constants as c


class Game:
    MINIMAX, ALPHABETA = 0, 1
    HUMAN, AI = 2, 3

    def __init__(self, board_size, blocks, recommend=True):
        self.initialize_game(board_size=board_size, blocks=blocks)
        self.recommend = recommend

    def initialize_game(self, board_size, blocks):
        self.current_state = s.select_initial_state(board_size, blocks)
        print(self.current_state)
        self.player_turn = s.select_initial_player()

    def draw_board(self):
        o.draw_game_board(self)

    def is_valid_move(self, px, py):
        return s.select_is_valid_move(self, px, py)

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
            px, py = o.input_coordonates(self)
            if self.is_valid_move(px, py):
                return (px, py)
            else:
                print('The move is not valid! Try again.')

    def switch_player(self):
        return s.select_next_player(self)

    def minimax(self, max=False):
        game_result = 2 if not max else -2  # -1 = X wins, 1 = X loss
        x, y = None, None
        end_game = s.select_end_game(self.is_end(), x, y)
        if end_game:
            return end_game

        for y_coordinate in range(0, 3):
            for x_coordinate in range(0, 3):
                if s.select_is_empty_position(self.current_state[y_coordinate][x_coordinate]):
                    if max:
                        self.current_state[y_coordinate][x_coordinate] = c.MAX_TOKEN
                        (minimax_result, _, _) = self.minimax(max=False)
                        if minimax_result > game_result:
                            game_result = minimax_result
                            x, y = y_coordinate, x_coordinate
                    else:
                        self.current_state[y_coordinate][x_coordinate] = c.MIN_TOKEN
                        (minimax_result, _, _) = self.minimax(max=True)
                        if minimax_result < game_result:
                            game_result = minimax_result
                            x, y = y_coordinate, x_coordinate

                    self.current_state[y_coordinate][x_coordinate] = c.EMPTY_TOKEN
        return game_result, x, y

    # Minimizing for 'X' and maximizing for 'O'
    def alphabeta(self, alpha=-2, beta=2, max=False):
        value = 2 if not max else -2
        x, y = None, None
        end_game = s.select_end_game(self.is_end(), x, y)

        if end_game:
            return end_game

        for y_coordinate in range(0, 3):
            for x_coordinate in range(0, 3):
                current_position = self.current_state[y_coordinate][x_coordinate]
                is_empty = s.select_is_empty_position(current_position)
                if is_empty:
                    if max:
                        self.current_state[y_coordinate][x_coordinate] = c.MAX_TOKEN
                        (alphabeta_result, _, _) = self.alphabeta(alpha, beta, max=False)
                        if alphabeta_result > value:
                            value = alphabeta_result
                            x, y = y_coordinate, x_coordinate
                    else:
                        self.current_state[y_coordinate][x_coordinate] = c.MIN_TOKEN
                        (alphabeta_result, _, _) = self.alphabeta(alpha, beta, max=True)
                        if alphabeta_result < value:
                            value = alphabeta_result
                            x, y = y_coordinate, x_coordinate
                    self.current_state[y_coordinate][x_coordinate] = c.EMPTY_TOKEN
                    if max:
                        if value >= beta:
                            return value, x, y
                        if value > alpha:
                            alpha = value
                    else:
                        if value <= alpha:
                            return value, x, y
                        if value < beta:
                            beta = value
        return value, x, y

    def finish_turn(self, x, y):
        self.current_state[x][y] = self.player_turn
        self.switch_player()

    def play(self, algo=None, player_x=None, player_o=None):
        algo, player_x, player_o = s.select_play_initial_values(self, algo, player_x, player_o)
        while True:
            self.draw_board()

            if self.check_end():
                return

            if algo == self.MINIMAX:
                (_, x, y) = self.minimax(max=s.select_is_max(self))
            elif algo == self.ALPHABETA:
                (m, x, y) = self.alphabeta(max=s.select_is_max(self))

            if s.select_is_human_turn(self, player_x, player_o):
                if self.recommend:
                    o.output_human_turn_recommend(time.time(), x, y)
                (x, y) = self.input_move()
            if s.select_is_ai_turn(self, player_x, player_o):
                o.output_ai_turn_recommend(time.time(), self, x, y)

            self.finish_turn(x=x, y=y)
