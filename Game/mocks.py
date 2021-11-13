def input_mock_game_settings():
    board_size = 5
    blocks = []
    winning_line_size = 4
    maximum_depths = 2, 2
    maximum_computing_time = 100
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_fast_game_settings():
    board_size = 3
    blocks = [(0, 0)]
    winning_line_size = 3
    maximum_depths = 2, 2
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
    maximum_depths = 100, 100
    maximum_computing_time = 2
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def large_game_settings():
    board_size = 5
    blocks = [(0, 0)]
    winning_line_size = 4
    maximum_depths = 2, 2
    maximum_computing_time = 100
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_1():
    board_size = 4
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 3
    maximum_depths = 6, 6
    maximum_computing_time = 1
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_2():
    board_size = 4
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 3
    maximum_depths = 6, 6
    maximum_computing_time = 5
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_3():
    board_size = 5
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 4
    maximum_depths = 2, 6
    maximum_computing_time = 1
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_4():
    board_size = 5
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 4
    maximum_depths = 6, 6
    maximum_computing_time = 5
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_5():
    board_size = 8
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 5
    maximum_depths = 2, 6
    maximum_computing_time = 1
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_6():
    board_size = 8
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 5
    maximum_depths = 2, 6
    maximum_computing_time = 5
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_7():
    board_size = 8
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 1
    maximum_depths = 6, 6
    maximum_computing_time = 100
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time


def input_mock_game_trace_8():
    board_size = 8
    blocks = [(0, 0), (0, 4), (4, 0), (4, 4)]
    winning_line_size = 6
    maximum_depths = 6, 6
    maximum_computing_time = 5
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time
