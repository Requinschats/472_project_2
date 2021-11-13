import scoreboard.selectors as s
from Game.constants import X_TOKEN, EMPTY_TOKEN, O_TOKEN
from Game.selectors import select_list_average
from game_traces.outputs import output_game_parameters


def output_scoreboard(board_parameters, game_parameters, game_statistics, game_results):
    file = s.select_score_board_file(board_parameters)
    output_game_parameters(file, board_parameters, game_parameters)
    output_game_results(file, game_results)
    output_scoreboard_statistics(file, game_statistics)


def output_game_results(file, game_results):
    ties_count = 0
    player_x_win_count = 0
    player_o_win_count = 0
    for result in game_results:
        if result == X_TOKEN: player_x_win_count += 1
        if result == O_TOKEN: player_o_win_count += 1
        if result == EMPTY_TOKEN: ties_count += 1

    player_x_win_count_percentage = str((player_x_win_count / len(game_results)) * 100)
    player_o_win_count_percentage = str((player_o_win_count / len(game_results)) * 100)
    ties_count_percentage = str((ties_count / len(game_results)) * 100)

    file.write("\n\n" + str(len(game_results)) + " games")

    file.write(
        "\n\nTotal ties: " + str(ties_count) + " (" + ties_count_percentage + "%)")
    file.write(
        "\nTotal wins for heuristic e1: " + str(
            player_x_win_count) + " (" + player_x_win_count_percentage + "%)")
    file.write(
        "\nTotal wins for heuristic e2: " + str(
            player_o_win_count) + " (" + player_o_win_count_percentage + "%)")


def output_scoreboard_statistics(file, game_statistics):
    scoreboard_statistics = s.select_output_scoreboard_statistics(game_statistics)
    average_evaluation_time, evaluation_counts, average_evaluations_by_depths, average_evaluations_depths, average_move_per_game = scoreboard_statistics
    file.write("\n")
    file.write("\ni   Average evaluation time: " + str(average_evaluation_time) + "s")
    file.write("\nii  Total heuristic evaluations: " + str(evaluation_counts))
    file.write("\niii Evaluations by depth: " + str(average_evaluations_by_depths))
    file.write("\niv  Average evaluation depth: " + str(average_evaluations_depths))
    file.write("\nvi  Average moves per game: " + str(average_move_per_game))
