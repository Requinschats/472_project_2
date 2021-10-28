import time


def draw_game_board(game):
    print()
    for y in range(0, 3):
        for x in range(0, 3):
            print(F'{game.current_state[x][y]}', end="")
        print()
    print()


def input_coordonates(game):
    print(F'Player {game.player_turn}, enter your move:')
    px = int(input('enter the x coordinate: '))
    py = int(input('enter the y coordinate: '))
    return px, py


def output_evaluation_time(start):
    print(F'Evaluation time: {round(time.time() - start, 7)}s')


def output_human_turn_recommend(start, x, y):
    output_evaluation_time(start)
    print(F'Recommended move: x = {x}, y = {y}')


def output_ai_turn_recommend(start, game, x, y):
    output_evaluation_time(start)
    print(F'Player {game.player_turn} under AI control plays: x = {x}, y = {y}')
