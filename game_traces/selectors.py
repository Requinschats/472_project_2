import os
import Game.constants as gc


def select_game_traces_file(board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    file_name = "gameTrace" + str(board_size) + str(len(blocks)) + str(winning_line_size) + str(
        maximum_computing_time) + ".text"
    file_path = "game_traces/game_traces/" + file_name

    if os.path.isfile(file_path):
        os.remove(file_path)

    return open(file_path, 'a+')


def select_algo_name_from_token(algo):
    if algo == 0:
        return "MINIMAX"
    if algo == 1:
        return "ALPHABETA"


def select_player_text_from_token(player):
    if player == 2:
        return "HUMAN"
    if player == 3:
        return "AI"


def select_player_from_token(token):
    if token == gc.EMPTY_TOKEN:
        return "Tie"
    if token == gc.O_TOKEN:
        return "X"
    if token == gc.O_TOKEN:
        return "O"


def select_formatted_coordinates(coordinates):
    x, y = coordinates
    return chr(97 + x).upper() + str(y)
