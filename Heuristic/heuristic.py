import time
from random import randrange

import Heuristic.selectors as s
import Game.selectors as gs


class Heuristic:
    RANGE = (-100, 100)
    WINNING_LINE_SCORE = RANGE[1] - 1
    LOOSING_LINE_SCORE = RANGE[0] + 1
    WINNING_MOVE_SCORE = RANGE[1] - 10
    LOOSING_MOVE_SCORE = RANGE[0] + 10
    HEURISTIC_1_ID = 1
    HEURISTIC_2_ID = 2
    HEURISTIC_ID_RANDOM = 3

    def __init__(self, game, board_parameters):
        heuristic_id = s.select_player_heuristic_id_from_player_turn(game)
        heuristic_evaluation_function = self.select_heuristic_function_from_id(heuristic_id)
        self.start_time = time.time()
        self.value = heuristic_evaluation_function(game, board_parameters)

    def select_heuristic_function_from_id(self, heuristic_id=1):
        if heuristic_id == self.HEURISTIC_ID_RANDOM:
            return self.evaluate_state_random
        if heuristic_id == self.HEURISTIC_2_ID:
            return self.evaluate_state_h2
        return self.evaluate_state_h1

    def get_computing_time(self):
        return time.time() - self.start_time

    def select_is_winning_state(self, game, board_parameters):
        if s.select_player_is_winning(game, board_parameters, game.player_turn):
            return self.WINNING_LINE_SCORE

        if (s.select_player_is_winning(game, board_parameters,
                                       gs.select_opposite_player(game.player_turn))):
            return self.LOOSING_LINE_SCORE

    def select_is_winning_move(self, game, board_parameters):
        if s.select_player_has_winning_move(game, board_parameters, game.player_turn):
            return self.WINNING_MOVE_SCORE

        if s.select_player_has_winning_move(game, board_parameters,
                                            gs.select_opposite_player(game.player_turn)):
            return self.LOOSING_MOVE_SCORE

    def evaluate_state_h1(self, game, board_parameters):
        winning_state = self.select_is_winning_state(game, board_parameters)
        if winning_state: return winning_state

        winning_move = self.select_is_winning_move(game, board_parameters)
        if winning_move: return winning_move

        max_center_score = s.select_min_max_center_score_differential(game, board_parameters)
        max_connected_group_score = s.select_connect_groups_score_differential(game,
                                                                               board_parameters)
        return max_center_score * 10 + max_connected_group_score * 5

    def evaluate_state_h2(self, game, board_parameters):
        return 0

    def evaluate_state_random(self, game, board_parameters):
        return randrange(10)
