from Game.Game import Game
import Game.mocks as m
import game_traces.selectors as gs


def main():
    # Real run:
    # board_parameters = o.input_game_settings()

    # Dev run:
    board_parameters = m.input_mock_game_settings()

    Game(board_parameters=board_parameters, recommend=True) \
        .play(algo=Game.ALPHABETA, player_x=Game.AI, player_o=Game.AI,
              board_parameters=board_parameters, file=gs.select_game_traces_file(board_parameters))


if __name__ == "__main__":
    main()
