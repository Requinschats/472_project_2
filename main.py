from Game.Game import Game
import Game.outputs as o
import Game.mocks as m
import Game.selectors as s
import game_traces.selectors as gs


def main():
    # Real run:
    # board_parameters = o.input_game_settings()

    # Dev run:
    board_parameters = m.input_mock_fast_game_settings()

    game = Game(board_parameters=board_parameters, recommend=True)

    game.play(algo=Game.MINIMAX, player_x=Game.AI, player_o=Game.AI,
              board_parameters=board_parameters, file=gs.select_game_traces_file(board_parameters))


if __name__ == "__main__":
    main()
