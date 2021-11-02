def input_mock_game_settings():
    board_size = 4
    blocks = []
    winning_line_size = 3
    maximum_depths = 5, 5
    maximum_computing_time = 100
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_fast_game_settings():
    board_size = 3
    blocks = [(0, 0)]
    winning_line_size = 3
    maximum_depths = 5, 5
    maximum_computing_time = 100
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_settings_short_depth():
    board_size = 3
    blocks = []
    winning_line_size = 3
    maximum_depths = 3, 3
    maximum_computing_time = 100
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_settings_short_computing_time():
    board_size = 3
    blocks = []
    winning_line_size = 3
    maximum_depths = 7, 7
    maximum_computing_time = 2
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time
