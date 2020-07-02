from score import Score
from human_player import HumanPlayer
from ai_player import AIPlayer
from game_manager import GameManager


def main():
    # 1st human player is created.
    score_keeper = Score()
    h1 = HumanPlayer(score_keeper, 'x', "Reuven")
    # h2 = HumanPlayer(score_keeper, 'o', "Shimon")
    # a1 = AIPlayer(score_keeper, 'x')
    # a2 = AIPlayer(score_keeper, 'o', "Bot2")

    while True:
        """
        You need to create 2nd 'o' player, either Human or AI, and select its name.
        For details see GameManager docs
        """
        opponent = GameManager.get_opponent_player(score_keeper)
        board_size = GameManager.input_board_size()

        game_manager = GameManager(h1, opponent, board_size)
        board = game_manager.board
        while not game_manager.game_over():
            game_manager.print_board()
            try:
                current_player = game_manager.current_player()
                next_move = current_player.next_move(board)
                print(next_move)
                if game_manager.is_valid_move(next_move):
                    game_manager.play(next_move)
                else:
                    print("Illegal move, either the cell is not empty or indexes are out of board!")
            except Exception:
                print('Illegal format move!')
                continue

        game_manager.print_board()
        winner = game_manager.get_winner()
        if winner is not None:
            print(f"{winner.value}! {winner.name} won")
            winner.sign_victory()
        else:
            print("No winner, game over...")

        score_keeper.print()

        next_game = input("Want to play again? Y/N ?")
        if next_game == 'Y':
            continue
        else:
            print("Bye!")
            break


if __name__ == '__main__':
    main()
