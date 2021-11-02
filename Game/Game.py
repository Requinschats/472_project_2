import time

import Game.selectors as s
import Game.outputs as o
import Game.constants as c

import game_traces.outputs as go


class Game:
    MINIMAX, ALPHABETA = 0, 1
    HUMAN, AI = 2, 3

    def __init__(self, board_parameters, recommend=True):
        self.initialize_game(board_parameters)
        self.recommend = recommend

    def initialize_game(self, board_parameters):
        self.current_state = s.select_initial_state(board_parameters)
        self.player_turn = s.select_initial_player()

    def is_valid_move(self, px, py, board_parameters):
        return s.select_is_valid_move(self, px, py, board_parameters)

    def check_end(self, board_parameters):
        self.result = s.select_is_end_token(self, board_parameters)
        end_game_output = s.select_end_game_output(self)
        if end_game_output:
            print(end_game_output)
        if self.result is not None:
            self.initialize_game(board_parameters)
        return self.result

    def input_move(self, board_parameters):
        while True:
            px, py = o.input_coordonates(self)
            if self.is_valid_move(px, py, board_parameters):
                return px, py
            else:
                print('The move is not valid! Try again.')

    def switch_player(self):
        return s.select_next_player(self)

    def minimax(self, is_max=False, board_parameters=None, current_depth=0, start_time=None):
        board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
        board_range = range(board_size)

        value = 2 if not is_max else -2  # -1 = X wins, 1 = X loss
        x, y = None, None

        if s.select_is_heuristic_restriction_met(current_depth, maximum_depths[0], start_time,
                                                 maximum_computing_time):
            return value, x, y

        end_game = s.select_end_game(s.select_is_end_token(self, board_parameters), x, y)
        if end_game:
            return end_game

        for y_coordinate in board_range:
            for x_coordinate in board_range:
                if s.select_is_empty_position(self.current_state[y_coordinate][x_coordinate]):
                    if is_max:
                        self.current_state[y_coordinate][x_coordinate] = c.MAX_TOKEN
                        (minimax_result, _, _) = self.minimax(is_max=False,
                                                              board_parameters=board_parameters,
                                                              current_depth=current_depth + 1,
                                                              start_time=start_time)
                        if minimax_result > value:
                            value = minimax_result
                            x, y = y_coordinate, x_coordinate
                    else:
                        self.current_state[y_coordinate][x_coordinate] = c.MIN_TOKEN
                        (minimax_result, _, _) = self.minimax(is_max=True,
                                                              board_parameters=board_parameters,
                                                              current_depth=current_depth + 1,
                                                              start_time=start_time)
                        if minimax_result < value:
                            value = minimax_result
                            x, y = y_coordinate, x_coordinate

                    self.current_state[y_coordinate][x_coordinate] = c.EMPTY_TOKEN
        return value, x, y

    # Minimizing for 'X' and maximizing for 'O'
    def alphabeta(self, alpha=-2, beta=2, is_max=False, board_parameters=None, current_depth=0,
                  start_time=None):
        value = 2 if not is_max else -2
        x, y = None, None
        end_game = s.select_end_game(s.select_is_end_token(self, board_parameters), x, y)
        board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
        board_range = range(board_size)

        if s.select_is_heuristic_restriction_met(current_depth, maximum_depths[0], start_time,
                                                 maximum_computing_time):
            return value, x, y

        if end_game:
            return end_game

        for y_coordinate in board_range:
            for x_coordinate in board_range:
                current_position = self.current_state[y_coordinate][x_coordinate]
                is_empty = s.select_is_empty_position(current_position)
                if is_empty:
                    if is_max:
                        self.current_state[y_coordinate][x_coordinate] = c.MAX_TOKEN
                        (alphabeta_result, _, _) = self.alphabeta(alpha, beta, is_max=False,
                                                                  board_parameters=board_parameters,
                                                                  start_time=start_time)
                        if alphabeta_result > value:
                            value = alphabeta_result
                            x, y = y_coordinate, x_coordinate
                    else:
                        self.current_state[y_coordinate][x_coordinate] = c.MIN_TOKEN
                        (alphabeta_result, _, _) = self.alphabeta(alpha, beta, is_max=True,
                                                                  board_parameters=board_parameters,
                                                                  start_time=start_time)
                        if alphabeta_result < value:
                            value = alphabeta_result
                            x, y = y_coordinate, x_coordinate
                    self.current_state[y_coordinate][x_coordinate] = c.EMPTY_TOKEN
                    if is_max:
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

    def play(self, algo=None, player_x=None, player_o=None, board_parameters=None,
             mock_inputs=None, file=None):
        algo, player_x, player_o = s.select_play_initial_values(self, algo, player_x, player_o)
        x, y = None, None

        go.output_game_trace_initial_values(file, board_parameters, (player_x, player_o, algo),
                                            self)

        while True:
            if not mock_inputs:
                o.draw_game_board(self, board_parameters)

            if self.check_end(board_parameters=board_parameters):
                go.output_game_trace_end(file,)
                return

            if s.select_is_human_turn(self, player_x, player_o):
                if mock_inputs:
                    move = mock_inputs.pop()
                    (x, y) = (move[0], move[1])
                else:
                    o.output_human_turn_recommend(self.recommend, time.time(), x, y)
                    (x, y) = self.input_move(board_parameters=board_parameters)
            if s.select_is_ai_turn(self, player_x, player_o):
                print("waiting for AI move")
                (m, x, y) = s.select_heuristic_move(board_parameters, algo, self)
                o.output_ai_turn_recommend(time.time(), self, x, y)

            go.output_move_to_game_trace(file, (x, y), "1s", self, board_parameters)
            self.finish_turn(x=x, y=y)
