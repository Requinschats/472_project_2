import os

from Game.selectors import select_list_average


def select_score_board_file(board_parameters):
    board_size, blocks, winning_line_size, maximum_depths, maximum_computing_time = board_parameters
    file_name = "scoreboard" + str(board_size) + str(len(blocks)) + str(winning_line_size) + str(
        maximum_computing_time) + ".text"
    file_path = "scoreboard/scoreboard/" + file_name

    if os.path.isfile(file_path):
        os.remove(file_path)

    return open(file_path, 'a+')


def select_average_evaluations_by_depth(evaluations_by_depths_list):
    evaluations_by_depths = {}
    for evaluations_by_depth in evaluations_by_depths_list:
        for depth, evaluation_count in evaluations_by_depth.items():
            if depth in evaluations_by_depths:
                evaluations_by_depths[depth].append(evaluation_count)
            else:
                evaluations_by_depths[depth] = [evaluation_count]
    return select_average_evaluations_by_depth_from_evaluations_by_depths(evaluations_by_depths)


def select_average_evaluations_by_depth_from_evaluations_by_depths(evaluations_by_depths):
    average_evaluations_by_depths = {}
    for depth, evaluations_count in evaluations_by_depths.items():
        average_evaluations_by_depths[depth] = select_list_average(evaluations_count)
    return average_evaluations_by_depths


def select_output_scoreboard_statistics(game_statistics):
    evaluation_times = []
    heuristic_evaluation_counts = []
    evaluations_by_depth = []
    evaluation_depths = []
    move_per_games = []
    for game_stat in game_statistics:
        evaluation_times.append(select_list_average(game_stat["evaluation_times"]))
        heuristic_evaluation_counts.append(sum(game_stat["states_evaluated"].values()))
        evaluations_by_depth.append(game_stat["state_count_per_depth"])
        evaluation_depths.append(game_stat["average_move_depths"])
        move_per_games.append(game_stat["move_count"])

    average_evaluation_time = select_list_average(evaluation_times)
    evaluation_counts = sum(heuristic_evaluation_counts)
    average_evaluations_by_depths = select_average_evaluations_by_depth(evaluations_by_depth)
    average_evaluations_depths = select_list_average(evaluation_depths)
    average_move_per_game = select_list_average(move_per_games)
    return average_evaluation_time, evaluation_counts, average_evaluations_by_depths, average_evaluations_depths, average_move_per_game
