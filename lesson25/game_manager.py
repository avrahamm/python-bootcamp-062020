from board import Board
from board_utils import BoardUtils

"""
GameManager holds players, _current_player_index and board.
"""


class GameManager:
    def __init__(self, player0, player1, board_size=3):
        self._players = [player0, player1]
        self._current_player_index = 0
        self.board = Board(board_size)

    def current_player(self):
        return self._players[self._current_player_index]

    def is_valid_move(self, next_move):
        return self.board.is_valid(next_move)

    def next_move(self):
        current_player = self.current_player()
        # self.board is relevant for AIPlayer only.
        return current_player.next_move(self.board)

    def play(self, next_move):
        current_player_value = self.current_player().value
        self.board.sign_move(next_move, current_player_value)
        self._current_player_index = (self._current_player_index + 1) % 2

    def game_over(self):
        # return False
        if self.get_winner() is not None:
            return True

        return not self.board.empty_cell_exists()

    def get_winner(self):
        for player in self._players:
            # rows
            if self.board.is_all_the_same((0, 0), (0, 1), (0, 2), player.value):
                return player
            if self.board.is_all_the_same((1, 0), (1, 1), (1, 2), player.value):
                return player
            if self.board.is_all_the_same((2, 0), (2, 1), (2, 2), player.value):
                return player

            # columns
            if self.board.is_all_the_same((0, 0), (1, 0), (2, 0), player.value):
                return player
            if self.board.is_all_the_same((0, 1), (1, 1), (2, 1), player.value):
                return player
            if self.board.is_all_the_same((0, 2), (1, 2), (2, 2), player.value):
                return player

            # diagonals
            if self.board.is_all_the_same((0, 0), (1, 1), (2, 2), player.value):
                return player
            if self.board.is_all_the_same((0, 2), (1, 1), (2, 0), player.value):
                return player

    def print(self):
        self.print_board()

    def print_board(self):
        bu = BoardUtils()
        bu.scan_board(
            self.board.board,
            lambda i, j, is_last: print(
                f"{self.board.board[i][j]:3}", end="\n" if is_last else ""
            )
        )
