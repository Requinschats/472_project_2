import time
import Game.selectors as s


def output_x_board_letters(board_size):
    print("  ", end="")
    for letter in range(97, 97 + board_size):
        print(chr(letter).upper(), end="")
    print()
    print("  ", end="")
    for letter in range(97, 97 + board_size):
        print("-", end="")


def draw_game_board(game, board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    output_x_board_letters(board_size)
    print()
    for y in range(board_size):
        print(F'{y}|', end="")
        for x in range(board_size):
            print(F'{game.current_state[y][x]}', end="")
        print()
    print()


def input_coordonates(game):
    print(F'Player {game.player_turn}, enter your move:')
    px = int(input('enter the x coordinate: '))
    py = int(input('enter the y coordinate: '))
    return px, py


def output_evaluation_time(start):
    print(F'Evaluation time: {round(time.time() - start, 7)}s')


def output_human_turn_recommend(should_recommend, start, x, y):
    if not should_recommend:
        return
    output_evaluation_time(start)
    print(F'Recommended move: x = {x}, y = {y}')


def output_ai_turn_recommend(start, game, x, y):
    output_evaluation_time(start)
    print(F'Player {game.player_turn} under AI control plays: x = {x}, y = {y}')


def input_block_coordinates(block_id, board_size):
    while True:
        x_coordinate = int(input("enter the x coordinate of block " + str(block_id) + ": "))
        y_coordinate = int(input("enter the y coordinate of block " + str(block_id) + ": "))
        if x_coordinate > board_size or y_coordinate > board_size:
            print("Invalid input")
        else:
            return x_coordinate, y_coordinate


def input_blocks_count():
    blocks_count = -1
    while blocks_count < 0 or blocks_count % 2 != 0:
        blocks_count = int(input("Enter the number of blocks: "))
        if blocks_count < 0 or blocks_count % 2 != 0:
            print("Invalid blocks count")
    return blocks_count


def input_blocks(board_size):
    blocks_count = input_blocks_count()
    blocks = []
    for block_id in range(blocks_count):
        block_coordinates = input_block_coordinates(block_id, board_size)
        blocks.append(block_coordinates)
    return blocks


def input_board_size():
    board_size = 0
    while board_size < 3 or board_size > 10:
        board_size = int(input("Enter board size: "))
        if board_size < 3 or board_size > 10:
            print("Invalid size")
    return board_size


def input_winning_line_size():
    winning_line_size = 0
    while winning_line_size < 3:
        winning_line_size = int(input("Enter winning line size: "))
        if winning_line_size < 3:
            print("Invalid size")
    return winning_line_size


def input_maximum_depths():
    p1_maximum_depth = int(input("Enter p1 search maximum depth: "))
    p2_maximum_depth = int(input("Enter p2 search maximum depth: "))
    return p1_maximum_depth, p2_maximum_depth


def input_maximum_computing_time():
    maximum_computing_time = int(input("Enter maximum computing time (in seconds): "))
    return maximum_computing_time


def input_game_settings():
    board_size = input_board_size()
    blocks = input_blocks(board_size)
    winning_line_size = input_winning_line_size()
    maximum_depths = input_maximum_depths()
    maximum_computing_time = input_maximum_computing_time()
    return board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time
