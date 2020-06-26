class BoardUtils:
    def scan_board(self, board, code_to_run_for_each_item):
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                res = code_to_run_for_each_item(i, j, j == len(board.board[i]) - 1)
                if res is not None:
                    return res
