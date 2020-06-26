from score import Score
from human_player import HumanPlayer
from ai_player import AIPlayer
from game_manager import GameManager

if __name__ == '__main__':
    """
    You need to create 2 players, either Human or AI with different values
    For details see GameManager docs
    """
    score_keeper = Score()
    h1 = HumanPlayer(score_keeper, 'x', "Reuven")
    h2 = HumanPlayer(score_keeper, 'o', "Shimon")
    a1 = AIPlayer(score_keeper, 'x')
    a2 = AIPlayer(score_keeper, 'o', "Bot2")

    while True:
        # combine "x" and "o" accurately
        game_manager = GameManager(a1, a2)
        while not game_manager.game_over():
            game_manager.print_board()
            try:
                next_move = game_manager.next_move()
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

        print(game_manager.current_player().score.score)

        next_game = input("Want to play again? Y/N ?")
        if next_game == 'Y':
            continue
        else:
            print("Bye!")
            exit(0)
