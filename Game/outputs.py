def draw_game_board(game):
    print()
    for y in range(0, 3):
        for x in range(0, 3):
            print(F'{game.current_state[x][y]}', end="")
        print()
    print()
