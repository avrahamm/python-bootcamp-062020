import time

from src.base_player import BasePlayer
from src.board_utils import BoardUtils


class AIPlayer(BasePlayer):
    def __init__(self, score_keeper, value, name="Bot"):
        super().__init__(score_keeper, value, name)

    def next_move(self, board):
        print(f"{self.name} turn, value {self.value}")
        time.sleep(2.4)

        def foreach_cell(i, j, is_last):
            if board.board[i][j] == '.':
                return [i, j]

        utils = BoardUtils()
        return utils.scan_board(
            board.board,
            foreach_cell,
        )
