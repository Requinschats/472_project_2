from Game.Game import Game
import Game.mocks as m
import game_traces.selectors as gs
from Heuristic.heuristic import Heuristic
from scoreboard.outputs import output_scoreboard


def main():
    # Real run:
    # board_parameters = o.input_game_settings()
    # Dev run:
    board_parameters = m.input_mock_game_settings()

    round_count = 1
    game_statistics = []
    game_results = []
    game_parameters = player_x, player_o, algo = Game.AI, Game.AI, Game.MINIMAX
    heuristics = Heuristic.HEURISTIC_1_ID, Heuristic.HEURISTIC_ID_RANDOM

    for game_index in range(2 * round_count):
        statistics, game_result = Game(board_parameters=board_parameters,
                                       recommend=True, heuristics=heuristics) \
            .play(algo=algo, player_x=player_x, player_o=player_o,
                  board_parameters=board_parameters,
                  file=gs.select_game_traces_file(board_parameters))
        game_statistics.append(statistics)
        game_results.append(game_result)

    output_scoreboard(board_parameters, game_parameters, game_statistics, game_results)


if __name__ == "__main__":
    main()
