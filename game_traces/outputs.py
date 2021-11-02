import game_traces.selectors as s
import Game.selectors as gs


def output_game_trace_initial_values(file, board_parameters, game_parameters, game):
    if not file:
        return

    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    player_x, player_o, algo = game_parameters
    file.write("Board size: " + str(board_size))
    file.write("\nBlocks: " + str(blocks))
    file.write("\nWinning line size: " + str(winning_line_size))
    file.write("\nMaximum depths: " + str(maximum_depths))
    file.write("\nMaximum computing time: " + str(maximum_computing_time))
    file.write("\nPlayer x: " + str(s.select_player_text_from_token(player_x)))
    file.write("\nPlayer 0: " + str(s.select_player_text_from_token(player_o)))
    file.write("\nAlgorithm: " + str(s.select_algo_name_from_token(algo)))

    file.write("\n\nInitial board configuration \n")
    output_game_trace_board(file, game, board_parameters)


def output_game_trace_board(file, game, board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    for y in range(board_size):
        for x in range(board_size):
            file.write(game.current_state[x][y])
        file.write("\n")
    file.write("\n")


def output_move_to_game_trace(file, move_coordinates, evaluation_time, game, board_parameters):
    if not file:
        return

    file.write("\nMove coordinates: " + str(move_coordinates))
    file.write("\nEvaluation_time: " + str(evaluation_time) + "\n")
    output_game_trace_board(file, game, board_parameters)


def output_state_count_per_depth(file, state_count_per_depth):
    file.write("\nStates evaluated for each depth: ")
    for depth, state_count in sorted(state_count_per_depth.items()):
        file.write("Depth: " + str(depth) + ", state count: " + str(state_count) + " ")


def output_game_trace_statistics(file, statistics):
    average_evaluation_time = gs.select_list_average(statistics["evaluation_times"])
    file.write("\nAverage evaluation time: " + str(average_evaluation_time))

    file.write("\nNumber of states evaluated: " + str(statistics["states_evaluated"]))

    average_per_move_average_depth = gs.select_list_average(statistics["average_move_depths"])
    file.write("\nAverage of per-move average depth: " + str(average_per_move_average_depth))

    output_state_count_per_depth(file, statistics["state_count_per_depth"])

    file.write("\nTotal number of moves: " + str(statistics["move_count"]))


def output_game_trace_end(file, winner, end_game_statistics):
    if not file:
        return

    file.write("\nWinner: " + str(s.select_player_from_token(winner)))
    output_game_trace_statistics(file, end_game_statistics)
