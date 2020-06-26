from score import Score
from human_player import HumanPlayer
from ai_player import AIPlayer
from game_manager import GameManager

if __name__ == '__main__':
    score_keeper = Score()
    h1 = HumanPlayer(score_keeper, 'x', "Shimon")
    h2 = HumanPlayer(score_keeper, 'x', "Reuven")
    # a = AIPlayer(score_keeper, 'o')

    while True:
        game_manager = GameManager(h1, a)
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

        if winner.value == h.value:  # "x":
            print(f"{h.value}! {h.name} won")
        elif winner.value == a.value:  # "o":
            print(f"{a.value}! {a.name} won")
        else:
            print("game over...")

        winner.sign_victory()
        print(h.score.score)

        next_game = input("Want to play again? Y/N ?")
        if next_game == 'Y':
            continue
        else:
            print("Bye!")
            exit(0)
