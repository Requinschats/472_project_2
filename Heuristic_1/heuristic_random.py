import time

import Heuristic_1.selectors as s
import Game.selectors as gs


class HeuristicRandom:
    RANGE = (-100, 100)

    def __init__(self, game, board_parameters):
        self.start_time = time.time()
        self.value = self.evaluate_state(game, board_parameters)

    def get_computing_time(self):
        return time.time() - self.start_time

    def evaluate_state(self, game, board_parameters):
        # print(game.)
        # if s.select_player_has_winning_move(game, board_parameters, game.player_turn):
        #     return self.RANGE[1]
        if s.select_player_has_winning_move(game, board_parameters,
                                            gs.select_opposite_player(game.player_turn)):
            return self.RANGE[0]

        max_center_score = s.select_min_max_center_score_differential(game, board_parameters)
        max_connected_group_score = s.select_connect_groups_score_differential(game,
                                                                               board_parameters)
        return max_center_score + max_connected_group_score
