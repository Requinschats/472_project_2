import Game.constants as c
import numpy as np
import Game.utils as u


def select_board_diagonals(board):
    board = np.array(board)
    return [board[::-1, :].diagonal(i) for i in range(-board.shape[0] + 1, board.shape[1])] \
        .extend(board.diagonal(i) for i in range(board.shape[1] - 1, -board.shape[0], -1)) \
        .tolist()


def select_is_winning_diagonal(diagonal, diagonal_size):
    token_to_match = diagonal[0]
    matching_count = 1
    for index, token in diagonal:
        if index == 0:
            continue
        elif token == c.EMPTY_TOKEN or token == c.BLOCK_TOKEN:
            matching_count = 1
            token_to_match = None
        elif token == token_to_match:
            matching_count += 1
        elif token != token_to_match:
            matching_count = 1
            token_to_match = token
        if matching_count == diagonal_size:
            return True
    return False


def select_diagonal_win(board, diagonal_size):
    diagonals = select_board_diagonals(board)
    possibly_winning_diagonals = list(filter(lambda d: len(d) >= diagonal_size, diagonals))

    if len(possibly_winning_diagonals) == 0:
        return False

    return any(select_is_winning_diagonal, possibly_winning_diagonals)


def select_vertical_win(game, board_parameters):
    return False


def select_horizontal_win(game, board_parameters):
    return False


def select_is_board_full(game, board_parameters):
    for i in range(0, 3):
        for j in range(0, 3):
            if game.current_state[i][j] == c.EMPTY_TOKEN:
                return True
    return False


def select_next_player(game):
    if game.player_turn == c.MIN_TOKEN:
        game.player_turn = c.MAX_TOKEN
    elif game.player_turn == c.MAX_TOKEN:
        game.player_turn = c.MIN_TOKEN
    return game.player_turn


def select_initial_state(board_parameters):
    board_size, blocks, winning_line_size = board_parameters
    board_range = range(board_size)
    board = [[None for y in board_range] for x in board_range]
    for y_coordinate in board_range:
        for x_coordinate in board_range:
            if (y_coordinate, x_coordinate) in blocks:
                board[y_coordinate][x_coordinate] = c.BLOCK_TOKEN
            else:
                board[y_coordinate][x_coordinate] = c.EMPTY_TOKEN
    return board


def select_initial_player():
    return c.MIN_TOKEN


def select_end_game(is_end, x, y):
    if is_end == c.MIN_TOKEN:
        return (-1, x, y)
    if is_end == c.MAX_TOKEN:
        return (1, x, y)
    if is_end == c.EMPTY_TOKEN:
        return (0, x, y)


def select_end_game_output(game):
    if game.result != None:
        if game.result == c.MIN_TOKEN:
            return 'The winner is X!'
        if game.result == c.MAX_TOKEN:
            return 'The winner is O!'
        if game.result == c.EMPTY_TOKEN:
            return "It's a tie!"


def select_is_end(game, board_parameters):
    vertical_win = select_vertical_win(game, board_parameters)
    if vertical_win:
        return vertical_win

    horizontal_win = select_horizontal_win(game, board_parameters)
    if vertical_win:
        return horizontal_win

    diagonal_win = select_diagonal_win(game, board_parameters)
    if diagonal_win:
        return diagonal_win

    if select_is_board_full(game, board_parameters):
        return None

    return c.EMPTY_TOKEN


def select_is_valid_move(game, px, py):
    is_outside_board = px < 0 or px > 2 or py < 0 or py > 2
    if is_outside_board:
        return False

    is_non_empty_space = game.current_state[px][py] != c.EMPTY_TOKEN
    if is_non_empty_space:
        return False

    return True


def select_is_empty_position(position):
    return position == c.EMPTY_TOKEN


def select_is_ai_turn(game, player_x, player_o):
    return (game.player_turn == 'X' and player_x == game.AI) or (
            game.player_turn == 'O' and player_o == game.AI)


def select_is_human_turn(game, player_x, player_o):
    return (game.player_turn == c.MIN_TOKEN and player_x == game.HUMAN) or (
            game.player_turn == c.MAX_TOKEN and player_o == game.HUMAN)


def select_is_max(game):
    return False if game.player_turn == c.MIN_TOKEN else True


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
        (_, x, y) = game.minimax(max=select_is_max(game), board_parameters=board_parameters)
        move = (_, x, y)
    elif algo == game.ALPHABETA:
        (m, x, y) = game.alphabeta(max=select_is_max(game), board_parameters=board_parameters)
        move = (m, x, y)
    return move
