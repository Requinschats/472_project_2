import numpy as np

import Game.selectors as s


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


def select_is_move_on_board(board, move):
    x, y = move
    try:
        board[int(x)][int(y)]
    except (ValueError, IndexError):
        return False
    else:
        return True


def select_surrounding_moves(x, y):
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


def select_surrounding_moves_from_position_score(board, position_coordinates):
    connection_count = 0
    (x, y) = position_coordinates
    for move in select_surrounding_moves(x, y):
        x_surrounding, y_surrounding = move
        if not select_is_move_on_board(board, move): continue
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
                    game.current_state, (x, y))
            if position_token == max_token:
                max_connected_group_score += select_surrounding_moves_from_position_score(
                    game.current_state, (x, y))
    return max_connected_group_score - min_connected_group_score
