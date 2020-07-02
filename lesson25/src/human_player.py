from src.base_player import BasePlayer
import src.exceptions as exceptions


class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper, value, name="Joe"):
        super().__init__(score_keeper, value, name)
        # print(self.score)

    def next_move(self, board):
        next_move = input(f"{self.name} turn, value {self.value}. Type the square position as (row, column)")
        try:
            coordinates = [int(coordinate.strip()) for coordinate in next_move.split(',')]
            return coordinates
        except Exception:
            raise exceptions.ParseMoveError("Illegal input for next move")

