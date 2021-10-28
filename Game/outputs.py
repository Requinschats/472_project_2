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


def input_block_coordinates(block_id, board_size):
    while True:
        x_coordinate = int(input("enter the x coordinate of block " + str(block_id) + ": "))
        y_coordinate = int(input("enter the y coordinate of block " + str(block_id) + ": "))
        if x_coordinate > board_size or y_coordinate > board_size:
            print("Invalid input")
        else:
            return x_coordinate, y_coordinate


def input_blocks(board_size):
    blocks_count = int(input("Enter the number of blocks: "))
    blocks = []
    for block_id in range(blocks_count):
        block_coordinates = input_block_coordinates(block_id, board_size)
        blocks.append(block_coordinates)
    return blocks


def input_board_size():
    board_size = 0
    while board_size < 1:
        board_size = int(input("Enter board size: "))
        if board_size < 1:
            print("Invalid size")
    return board_size


def input_game_settings():
    board_size = input_board_size()
    blocks = input_blocks(board_size)
    return board_size, blocks
