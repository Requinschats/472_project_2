import Game.constants as c


def select_vertical_win(game):
    for i in range(0, 3):
        if (game.current_state[0][i] != c.EMPTY_TOKEN and
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
    if (game.current_state[0][0] != c.EMPTY_TOKEN and
            game.current_state[0][0] == game.current_state[1][1] and
            game.current_state[0][0] == game.current_state[2][2]):
        return game.current_state[0][0]


def select_second_diagonal_win(game):
    if (game.current_state[0][2] != c.EMPTY_TOKEN and
            game.current_state[0][2] == game.current_state[1][1] and
            game.current_state[0][2] == game.current_state[2][0]):
        return game.current_state[0][2]


def select_is_board_full(game):
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


def select_initial_state():
    return [[c.EMPTY_TOKEN, c.EMPTY_TOKEN, c.EMPTY_TOKEN],
            [c.EMPTY_TOKEN, c.EMPTY_TOKEN, c.EMPTY_TOKEN],
            [c.EMPTY_TOKEN, c.EMPTY_TOKEN, c.EMPTY_TOKEN]]


def select_inital_player():
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


def select_is_end(game):
    vertical_win = select_vertical_win(game)
    if vertical_win:
        return vertical_win

    horizontal_win = select_horizontal_win(game)
    if vertical_win:
        return horizontal_win

    main_diagonal_win = select_main_diagonal_win(game)
    if main_diagonal_win:
        return main_diagonal_win

    second_diagonal_win = select_second_diagonal_win(game)
    if second_diagonal_win:
        return second_diagonal_win

    if select_is_board_full(game):
        return None

    return c.EMPTY_TOKEN


def select_is_valid_move(game, px, py):
    is_non_empty_space = game.current_state[px][py] != c.EMPTY_TOKEN
    is_outside_board = px < 0 or px > 2 or py < 0 or py > 2
    if is_outside_board or is_non_empty_space:
        return False
    else:
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
