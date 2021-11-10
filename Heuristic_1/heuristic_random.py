import time

import Heuristic_1.selectors as s


class HeuristicRandom:
    RANGE = (-100, 100)

    def __init__(self, game, board_parameters):
        self.start_time = time.time()
        self.value = self.evaluate_state(game, board_parameters)

    def get_computing_time(self):
        return time.time() - self.start_time

    def evaluate_state(self, game, board_parameters):
        if s.select_min_has_winning_move(game, board_parameters):
            return self.RANGE[0]

        max_center_score = s.select_min_max_center_score_differential(game, board_parameters)
        max_connected_group_score = s.select_connect_groups_score_differential(game,
                                                                               board_parameters)
        return 10 * max_center_score + 10 * max_connected_group_score
