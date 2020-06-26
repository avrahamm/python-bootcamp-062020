class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [['.', '.', '.'] for row in range(board_size)]
        # self.board = [['x', '.', '.'], ['o', '.', '.'], ['.', '.', '.']]

    def is_valid(self, next_move):
        row, column = next_move
        try:
            return self.is_cell_empty(row, column)
        except IndexError:
            return False

    def is_cell_empty(self, i, j):
        return self.board[i][j] == '.'

    def empty_cell_exists(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.is_cell_empty(i, j):
                    return True
        return False

    def sign_move(self, next_move, value):
        row, column = next_move
        self.board[row][column] = value

    def is_all_the_same(self, i1, i2, i3, val):
        if (self.board[i1[0]][i1[1]] == self.board[i2[0]][i2[1]] and
                self.board[i1[0]][i1[1]] == self.board[i3[0]][i3[1]] and
                self.board[i1[0]][i1[1]] == val):
            return True
        else:
            return False
