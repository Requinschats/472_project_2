from Game.Game import Game
import Game.outputs as o


def main():
    board_size, blocks = o.input_game_settings()
    game = Game(board_size=board_size, blocks=blocks, recommend=True)

    # g.play(algo=Game.ALPHABETA, player_x=Game.AI, player_o=Game.AI)
    # g.play(algo=Game.MINIMAX, player_x=Game.AI, player_o=Game.HUMAN)


if __name__ == "__main__":
    main()
