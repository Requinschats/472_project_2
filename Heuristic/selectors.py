import numpy as np

import Game.selectors as s
import Game.constants as c


def select_is_player_token_winning_line(list_of_winning_lines, winning_line_size, player_token):
    for winning_lines in list_of_winning_lines:
        winning_token = s.select_winning_token_by_winning_lines(winning_lines, winning_line_size)
        if winning_token == player_token: return True
    return False


def select_player_has_winning_move(game, board_parameters, player_token):
    board_size, _, winning_line_size, _, _ = board_parameters
    for y in range(board_size):
        for x in range(board_size):
            if not s.select_is_empty_position(game.current_state[y][x]): continue
            future_game_state = game.current_state.copy()
            future_game_state[y][x] = player_token
            columns = s.select_columns(future_game_state, board_size)
            rows = s.select_rows(future_game_state, board_size)
            diagonals = s.select_board_diagonals(future_game_state)
            if select_is_player_token_winning_line([columns, rows, diagonals], winning_line_size,
                                                   player_token):
                return True
    return False


def select_player_is_winning(game, board_parameters, player_token):
    board_size, _, winning_line_size, _, _ = board_parameters
    columns = s.select_columns(game.current_state, board_size)
    rows = s.select_rows(game.current_state, board_size)
    diagonals = s.select_board_diagonals(game.current_state)
    if select_is_player_token_winning_line([columns, rows, diagonals], winning_line_size,
                                           player_token):
        return True
    return False


def select_distance_between_coordinates(p1, p2):
    distance = np.linalg.norm(np.array(p1) - np.array(p2))
    return distance


def select_min_max_center_score_differential(game, board_parameters):
    board_size, _, _, _, _ = board_parameters
    max_token, min_token = s.select_max_min_tokens_from_player_turn(game.player_turn)
    max_center_score = 0
    min_center_score = 0
    center_position = (board_size / 2, board_size / 2)
    for y in range(board_size):
        for x in range(board_size):
            position_token = game.current_state[y][x]
            if position_token != min_token and position_token != max_token: continue
            distance_from_center = select_distance_between_coordinates((x, y), center_position)
            if position_token == min_token:
                min_center_score += 1 / distance_from_center if distance_from_center != 0 else 1
            if position_token == max_token:
                max_center_score += 1 / distance_from_center if distance_from_center != 0 else 1
    max_center_score_differential = max_center_score - min_center_score
    return max_center_score_differential


def select_is_move_on_board(board_size, move):
    x, y = move
    if -1 < y < board_size and -1 < x < board_size: return True
    return False


def select_surrounding_moves(x, y):
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


def select_surrounding_moves_from_position_score(board, position_coordinates, board_size):
    connection_count = 0
    (x, y) = position_coordinates
    for move in select_surrounding_moves(x, y):
        x_surrounding, y_surrounding = move
        if not select_is_move_on_board(board_size, move): continue
        if board[y_surrounding][x_surrounding] == board[y][x]:
            connection_count += 1
    return connection_count


def select_connect_groups_score_differential(game, board_parameters):
    board_size, _, _, _, _ = board_parameters
    max_token, min_token = s.select_max_min_tokens_from_player_turn(game.player_turn)
    min_connected_group_score = 0
    max_connected_group_score = 0
    for y in range(board_size):
        for x in range(board_size):
            position_token = game.current_state[y][x]
            if position_token == min_token:
                min_connected_group_score += select_surrounding_moves_from_position_score(
                    game.current_state, (x, y), board_size)
            if position_token == max_token:
                max_connected_group_score += select_surrounding_moves_from_position_score(
                    game.current_state, (x, y), board_size)
    return max_connected_group_score - min_connected_group_score


def select_player_heuristic_id_from_player_turn(game):
    player_turn = game.player_turn
    if player_turn == c.X_TOKEN:
        return game.heuristics[0]
    else:
        return game.heuristics[1]


def select_surrounding_position_cardinality_contribution(game_board, move, player_token,
                                                         other_player_token, board_size):
    x_surrounding, y_surrounding = move
    if not select_is_move_on_board(board_size, move): return -3
    surrounding_position_token = game_board[y_surrounding][x_surrounding]
    if surrounding_position_token == c.BLOCK_TOKEN: return -1
    if surrounding_position_token == other_player_token: return 0
    if surrounding_position_token == c.EMPTY_TOKEN: return 1
    if surrounding_position_token == player_token: return 3


def select_position_cardinality_score(game_board, coordinate, token, board_size):
    (x, y) = coordinate
    cardinality_score = 0
    other_player_token = s.select_opposite_player(token)
    for move in select_surrounding_moves(x, y):
        cardinality_score += select_surrounding_position_cardinality_contribution(game_board, move,
                                                                                  token,
                                                                                  other_player_token,
                                                                                  board_size)
    return cardinality_score


def select_max_move_cardinalities_differential(game, board_parameters):
    board_size, _, _, _, _ = board_parameters
    max_token, min_token = s.select_max_min_tokens_from_player_turn(game.player_turn)
    game_board = game.current_state
    max_cardinality_score, min_cardinality_score = 0, 0
    for y in range(board_size):
        for x in range(board_size):
            position_token = game_board[y][x]
            if position_token == c.EMPTY_TOKEN or position_token == c.BLOCK_TOKEN: continue
            if position_token == max_token:
                position_score = select_position_cardinality_score(game_board, (x, y), max_token,
                                                                   board_size)
                max_cardinality_score += position_score
            if position_token == min_token:
                position_score = select_position_cardinality_score(game_board, (x, y), min_token,
                                                                   board_size)
                min_cardinality_score += position_score
    return max_cardinality_score - min_cardinality_score
