import Game.constants as c
import Game.outputs as o
import numpy as np
import time

from Heuristic.heuristic import Heuristic


def select_rows(board, board_size):
    rows = []
    row = []
    for x in range(board_size):
        for y in range(board_size):
            row.append(board[y][x])
        rows.append(row)
        row = []
    return rows


def select_columns(board, board_size):
    columns = []
    column = []
    for x in range(board_size):
        for y in range(board_size):
            column.append(board[x][y])
        columns.append(column)
        column = []
    return columns


def select_board_diagonals(board):
    diagonals = [board[::-1, :].diagonal(i) for i in range(-board.shape[0] + 1, board.shape[1])]
    diagonals.extend(board.diagonal(i) for i in range(board.shape[1] - 1, -board.shape[0], -1))
    return diagonals


def select_winning_token_by_winning_lines(line_list, diagonal_size):
    for line in line_list:
        token_to_match = None
        matching_count = 1
        for index, token in enumerate(line):
            if index == 0:
                token_to_match = token
            elif token == c.EMPTY_TOKEN or token == c.BLOCK_TOKEN:
                matching_count = 1
                token_to_match = None
            elif token == token_to_match:
                matching_count += 1
            elif token != token_to_match:
                matching_count = 1
                token_to_match = token
            if matching_count == diagonal_size:
                return token_to_match
    return None


def select_diagonal_win(board, board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    diagonals = select_board_diagonals(board)
    possibly_winning_diagonals = list(filter(lambda d: len(d) >= winning_line_size, diagonals))

    if len(possibly_winning_diagonals) == 0:
        return None
    return select_winning_token_by_winning_lines(diagonals, winning_line_size)


def select_vertical_win(game, board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    columns = select_columns(game.current_state, board_size)
    return select_winning_token_by_winning_lines(columns, winning_line_size)


def select_horizontal_win(game, board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    rows = select_rows(game.current_state, board_size)
    return select_winning_token_by_winning_lines(rows, winning_line_size)


def select_is_board_full(game, board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    for y_coordinates in range(0, board_size):
        for x_coordinates in range(0, board_size):
            if game.current_state[y_coordinates][x_coordinates] == c.EMPTY_TOKEN:
                return False
    return True


def select_next_player(game):
    if game.player_turn == c.X_TOKEN:
        game.player_turn = c.O_TOKEN
    elif game.player_turn == c.O_TOKEN:
        game.player_turn = c.X_TOKEN
    return game.player_turn


def select_initial_state(board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    board_range = range(board_size)
    board = np.zeros((board_size, board_size), dtype=str)
    for y_coordinate in board_range:
        for x_coordinate in board_range:
            if (y_coordinate, x_coordinate) in blocks:
                board[y_coordinate][x_coordinate] = c.BLOCK_TOKEN
            else:
                board[y_coordinate][x_coordinate] = c.EMPTY_TOKEN
    return board


def select_initial_player():
    return c.X_TOKEN


# def select_end_game(is_end_token, x, y):
#     if is_end_token == c.X_TOKEN:
#         return c.HEURISTIC_MAX_DEFAULT_VALUE + 1, x, y
#     if is_end_token == c.O_TOKEN:
#         return c.HEURISTIC_MIN_DEFAULT_VALUE - 1, x, y
#     if is_end_token == c.EMPTY_TOKEN:
#         return 0, x, y


def select_end_game_output(game):
    if game.result is not None:
        if game.result == c.X_TOKEN:
            return 'The winner is X!'
        if game.result == c.O_TOKEN:
            return 'The winner is O!'
        if game.result == c.EMPTY_TOKEN:
            return "It's a tie!"


def select_is_end_token(game, board_parameters):
    vertical_win = select_vertical_win(game, board_parameters)
    if vertical_win:
        return vertical_win

    horizontal_win = select_horizontal_win(game, board_parameters)
    if horizontal_win:
        return horizontal_win

    diagonal_win = select_diagonal_win(game.current_state, board_parameters)
    if diagonal_win:
        return diagonal_win

    if select_is_board_full(game, board_parameters):
        return c.EMPTY_TOKEN

    return None


def select_is_valid_move(game, px, py, board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    is_outside_board = px < 0 or px >= board_size or py < 0 or py >= board_size
    if is_outside_board:
        return False

    is_non_empty_space = game.current_state[py][px] != c.EMPTY_TOKEN
    if is_non_empty_space:
        return False

    return True


def select_is_empty_position(position):
    return position == c.EMPTY_TOKEN


def select_is_ai_turn(game, player_x, player_o):
    return (game.player_turn == 'X' and player_x == game.AI) or (
            game.player_turn == 'O' and player_o == game.AI)


def select_is_human_turn(game, player_x, player_o):
    return (game.player_turn == c.X_TOKEN and player_x == game.HUMAN) or (
            game.player_turn == c.O_TOKEN and player_o == game.HUMAN)


def select_is_max(game):
    return True
    # return False if game.player_turn == c.X_TOKEN else True


def select_play_initial_values(game, algo, player_x, player_o):
    if algo is None:
        algo = game.ALPHABETA
    if player_x is None:
        player_x = game.HUMAN
    if player_o is None:
        player_o = game.HUMAN
    return algo, player_x, player_o


def select_heuristic_move(board_parameters, algo, game):
    move = None
    if algo == game.MINIMAX:
        (_, x, y) = game.minimax(is_max=True, board_parameters=board_parameters,
                                 start_time=time.time())
        move = (_, x, y)
    elif algo == game.ALPHABETA:
        (m, x, y) = game.alphabeta(is_max=True, board_parameters=board_parameters,
                                   start_time=time.time())
        move = (m, x, y)
    return move


def select_is_time_elapsed(start_time, maximum_computing_time):
    is_time_elapsed = (time.time() - start_time) >= maximum_computing_time
    return is_time_elapsed


def select_is_second_to_last_move(game_board, board_size):
    empty_move_count = 0
    for y in range(board_size):
        for x in range(board_size):
            if game_board[y][x] == c.EMPTY_TOKEN: empty_move_count += 1
    if empty_move_count == 1: return True
    return False


def select_is_immediate_parent_to_max_depth_leaf(depth_parameters, game_board,
                                                 board_size):
    current_depth, maximum_depths = depth_parameters
    return current_depth + 1 == maximum_depths or select_is_second_to_last_move(game_board,
                                                                                board_size)


def select_initial_statistics():
    return {
        "evaluation_times": [],
        "states_evaluated": {},
        "average_move_depths": [],
        "state_count_per_depth": {},
        "move_count": 0
    }


def select_list_average(array_list):
    if len(array_list) == 0:
        return 0

    return sum(array_list) / len(array_list)


def select_next_move_from_mock_inputs(mock_inputs):
    move = mock_inputs.pop()
    return move[0], move[1]


def select_human_turn_move(game, mock_inputs, board_parameters, recommended_coordinates):
    x, y = recommended_coordinates
    if mock_inputs:
        return select_next_move_from_mock_inputs(mock_inputs)
    else:
        o.output_human_turn_recommend(game.recommend, time.time(), x, y)
        return game.input_move(board_parameters=board_parameters)


def select_is_near_maximum_computing_time(start_time, computing_time):
    time_elapsed = time.time() - start_time
    return time_elapsed / computing_time >= 0.75 or computing_time - time_elapsed <= 0.75


def select_should_evaluate_state(depth_parameters, game, board_size, start_time,
                                 maximum_computing_time):
    is_immediate_parent_to_leaf = select_is_immediate_parent_to_max_depth_leaf(depth_parameters,
                                                                               game.current_state,
                                                                               board_size)
    is_near_max_computing_time = select_is_near_maximum_computing_time(start_time,
                                                                       maximum_computing_time)
    return is_immediate_parent_to_leaf or is_near_max_computing_time


def select_mini_max_child_value(game, next_minimax_params, depth_parameters):
    next_is_max, board_parameters, next_depth, start_time = next_minimax_params
    board_size, _, _, maximum_depths, maximum_computing_time = board_parameters
    current_depth, maximum_depths = depth_parameters

    if select_should_evaluate_state(depth_parameters, game, board_size, start_time,
                                    maximum_computing_time):
        child_value = Heuristic(game, board_parameters).value
        game.update_statistics_after_state_evaluation(start_time, current_depth)
    else:
        (child_value, _, _) = game.minimax(next_is_max, board_parameters, next_depth, start_time)
    return child_value


def select_alpha_beta_child_value(alpha, beta, game, next_minimax_params, depth_parameters):
    next_is_max, board_parameters, next_depth, start_time = next_minimax_params
    board_size, _, _, maximum_depths, maximum_computing_time = board_parameters
    current_depth, maximum_depths = depth_parameters

    if select_should_evaluate_state(depth_parameters, game, board_size, start_time,
                                    maximum_computing_time):
        child_value = Heuristic(game, board_parameters).value
        game.update_statistics_after_state_evaluation(start_time, current_depth)
    else:
        (child_value, _, _) = game.alphabeta(alpha, beta, next_is_max, board_parameters, next_depth,
                                             start_time)
    return child_value


def select_max_min_tokens_from_player_turn(player_turn):
    if player_turn == c.X_TOKEN:
        return c.X_TOKEN, c.O_TOKEN
    else:
        return c.O_TOKEN, c.X_TOKEN


def select_opposite_player(player_token):
    if player_token == c.X_TOKEN:
        return c.O_TOKEN
    if player_token == c.O_TOKEN:
        return c.X_TOKEN


def select_char_input_matching_number(char):
    return ord(char) - 97


def select_coordinate_input_value(coordinate_input):
    if coordinate_input.isalpha(): return select_char_input_matching_number(coordinate_input)
    return int(coordinate_input)
