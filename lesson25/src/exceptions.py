class ParseMoveError(Exception):
    def __init__(self, message):
        super().__init__(message)


class OutOfBoardError(Exception):
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col
