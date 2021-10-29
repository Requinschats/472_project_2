from Game.Game import Game
import Game.outputs as o
import Game.mocks as m


def main():
    # board_parameters = o.input_game_settings()
    board_parameters = m.input_mock_fast_game_settings()

    game = Game(board_parameters=board_parameters, recommend=True)

    game.play(algo=Game.MINIMAX, player_x=Game.HUMAN, player_o=Game.AI,
              board_parameters=board_parameters)
    # game.play(algo=Game.MINIMAX, player_x=Game.AI, player_o=Game.AI,
    #           board_parameters=board_parameters)


if __name__ == "__main__":
    main()
