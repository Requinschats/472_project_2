from Game.Game import Game
import Game.outputs as o


def main():
    board_parameters = o.input_game_settings()
    game = Game(board_parameters=board_parameters, recommend=True)

    game.play(algo=Game.ALPHABETA, player_x=Game.AI, player_o=Game.AI,
              board_parameters=board_parameters)
    # g.play(algo=Game.MINIMAX, player_x=Game.AI, player_o=Game.HUMAN)


if __name__ == "__main__":
    main()
