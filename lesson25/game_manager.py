from board import Board
from board_utils import BoardUtils
from human_player import HumanPlayer
from ai_player import AIPlayer

"""
GameManager holds players, _current_player_index and board.
"""


class GameManager:
    def __init__(self, player0, player1, board_size=3):
        self._players = [player0, player1]
        self._current_player_index = 0
        self.board = Board(board_size)

    @staticmethod
    def get_opponent_player(score_keeper):
        dispatcher = {
            'H': HumanPlayer,
            'A': AIPlayer
        }
        while True:
            opponent_type = input(f"Select Human or AI, H/A respectively: ")
            opponent_name = input(f"Select opponent name: ")
            try:
                opponent = dispatcher[opponent_type](score_keeper, 'o', opponent_name)
                return opponent
            except Exception:
                print('Illegal format, try again: ')

    def current_player(self):
        return self._players[self._current_player_index]

    def is_valid_move(self, next_move):
        return self.board.is_valid_move(next_move)

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
            if self.board.is_winning_row(player.value):
                return player

            # columns
            if self.board.is_winning_col(player.value):
                return player

            # first diagonal
            if self.board.is_winning_first_diagonal(player.value):
                return player

            # second diagonal
            if self.board.is_winning_second_diagonal(player.value):
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
