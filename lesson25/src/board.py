from src.board_utils import BoardUtils
import src.exceptions as exceptions


class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        # self.board = [['.', '.', '.'] for row in range(board_size)]
        self.board = [['.' for x in range(self.board_size)] for y in range(self.board_size)]
        # self.board = [['x', '.', '.'], ['o', '.', '.'], ['.', '.', '.']]

    def __eq__(self, other):
        if self.board_size != other.board_size:
            return False

        def foreach_cell(i, j, is_last):
            if self.board[i][j] != other.board[i][j]:
                return False

        utils = BoardUtils()
        if utils.scan_board(self.board, foreach_cell) is False:
            return False
        return True

    def is_valid_move(self, next_move):
        row, column = next_move
        try:
            return self.is_cell_empty(row, column)
        except IndexError:
            raise exceptions.OutOfBoardError(row, column)

    def is_cell_empty(self, i, j):
        return self.board[i][j] == '.'

    def empty_cell_exists(self):
        def foreach_cell(i, j, is_last):
            if self.is_cell_empty(i, j):
                return True

        utils = BoardUtils()
        if utils.scan_board(self.board, foreach_cell):
            return True
        return False

    def sign_move(self, next_move, value):
        row, column = next_move
        self.board[row][column] = value

    def is_winning_row(self, value):
        for row in range(self.board_size):
            answer = True
            for col in range(self.board_size):
                if self.board[row][col] != value:
                    answer = False
                    break
            if answer:
                return True

        return False

    def is_winning_col(self, value):
        for col in range(self.board_size):
            answer = True
            for row in range(self.board_size):
                if self.board[row][col] != value:
                    answer = False
                    break
            if answer:
                return True

        return False

    def is_winning_first_diagonal(self, value):
        answer = True
        for i in range(self.board_size):
            if self.board[i][i] != value:
                answer = False
                break

        return answer

    def is_winning_second_diagonal(self, value):
        answer = True
        for i, j in zip(range(self.board_size), range(self.board_size - 1, -1, -1)):
            if self.board[i][j] != value:
                answer = False
                break

        return answer
