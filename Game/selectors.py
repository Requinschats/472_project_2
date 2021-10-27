def select_vertical_win(game):
    for i in range(0, 3):
        if (game.current_state[0][i] != '.' and
                game.current_state[0][i] == game.current_state[1][i] and
                game.current_state[1][i] == game.current_state[2][i]):
            return game.current_state[0][i]


def select_horizontal_win(game):
    for i in range(0, 3):
        if game.current_state[i] == ['X', 'X', 'X']:
            return 'X'
        elif game.current_state[i] == ['O', 'O', 'O']:
            return 'O'


def select_main_diagonal_win(game):
    if (game.current_state[0][0] != '.' and
            game.current_state[0][0] == game.current_state[1][1] and
            game.current_state[0][0] == game.current_state[2][2]):
        return game.current_state[0][0]


def select_second_diagonal_win(game):
    if (game.current_state[0][2] != '.' and
            game.current_state[0][2] == game.current_state[1][1] and
            game.current_state[0][2] == game.current_state[2][0]):
        return game.current_state[0][2]


def select_is_board_full(game):
    for i in range(0, 3):
        for j in range(0, 3):
            if game.current_state[i][j] == '.':
                return True
    return False


def select_next_player(game):
    if game.player_turn == 'X':
        game.player_turn = 'O'
    elif game.player_turn == 'O':
        game.player_turn = 'X'
    return game.player_turn


def select_initial_state():
    return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


def select_inital_player():
    return 'X'


def select_end_game(is_end, x, y):
    if is_end == 'X':
        return (-1, x, y)
    if is_end == 'O':
        return (1, x, y)
    if is_end == '.':
        return (0, x, y)
