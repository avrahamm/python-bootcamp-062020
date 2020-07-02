import unittest

from score import Score
from ai_player import AIPlayer
from human_player import HumanPlayer
from game_manager import GameManager
from board import Board


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.score_keeper = Score()
        self.h1 = HumanPlayer(self.score_keeper, 'x', "Reuven")
        self.h2 = HumanPlayer(self.score_keeper, 'o', "Shimon")
        self.a1 = AIPlayer(self.score_keeper, 'x')
        self.a2 = AIPlayer(self.score_keeper, 'o', "Bot2")
        # self.board_size = 3

    def test_board_eq_init_3(self):
        board_size = 3
        board_3 = Board(board_size)
        board_3.board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        board = Board(board_size)
        self.assertEqual(board_3, board)

    def test_board_eq_init_4(self):
        board_size = 4
        board_4 = Board(board_size)
        board_4.board = [
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]
        board = Board(board_size)
        self.assertEqual(board_4, board)

    def test_board_eq_3(self):
        board_size = 4
        board_4 = Board(board_size)
        board_4.board = [
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

        board = Board(board_size)
        board.board = [
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]
        self.assertEqual(board_4, board)

    def test_board_eq_4(self):
        board_size = 3
        board_3 = Board(board_size)
        board_3.board = [
            ['x', 'o', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        board = Board(board_size)
        board.board = [
            ['x', 'o', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        self.assertEqual(board_3, board)

    def test_is_valid_move(self):
        board_size = 3
        valid_move = [0, 0]
        occupied = [0, 1]
        out_of_board = [0, board_size +2]

        board = Board(board_size)
        board.board = [
            ['.', 'o', 'x'],
            ['.', 'x', '.'],
            ['x', '.', 'o']
        ]

        self.assertTrue(board.is_valid_move(valid_move))
        self.assertFalse(board.is_valid_move(occupied))
        self.assertFalse(board.is_valid_move(out_of_board))

    def test_empty_cell_exists(self):
        board_size = 3
        valid_move = [0, 0]
        occupied = [0, 1]
        out_of_board = [0, board_size +2]

        board_available = Board(board_size)
        board_available.board = [
            ['.', 'o', 'x'],
            ['.', 'x', '.'],
            ['x', '.', 'o']
        ]

        board_full = Board(board_size)
        board_full.board = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['x', 'x', 'o']
        ]

        self.assertTrue(board_available.empty_cell_exists())
        self.assertFalse(board_full.empty_cell_exists())

    def test_is_winning_row_3(self):
        board_size = 3
        board_3 = Board(board_size)
        board_3.board = [
            ['x', 'x', 'x'],
            ['o', '.', '.'],
            ['.', 'o', '.']
        ]

        self.assertTrue(board_3.is_winning_row('x'))
        self.assertFalse(board_3.is_winning_row('o'))

    def test_is_winning_col_4(self):
        board_size = 4
        board_4 = Board(board_size)
        board_4.board = [
            ['o', '.', 'o', 'x'],
            ['.', 'o', '.', 'x'],
            ['.', '.', '.', 'x'],
            ['.', '.', '.', 'x'],
        ]

        self.assertTrue(board_4.is_winning_col('x'))
        self.assertFalse(board_4.is_winning_col('o'))

    def test_is_winning_first_diagonal(self):
        board_size = 3
        board_3 = Board(board_size)
        board_3.board = [
            ['x', 'o', 'o'],
            ['.', 'x', '.'],
            ['.', '.', 'x']
        ]

        self.assertTrue(board_3.is_winning_first_diagonal('x'))
        self.assertFalse(board_3.is_winning_first_diagonal('o'))

    def test_is_winning_second_diagonal(self):
        board_size = 3
        board_3 = Board(board_size)
        board_3.board = [
            ['.', 'o', 'x'],
            ['.', 'x', '.'],
            ['x', '.', 'o']
        ]

        self.assertTrue(board_3.is_winning_second_diagonal('x'))
        self.assertFalse(board_3.is_winning_second_diagonal('o'))

if __name__ == '__main__':
    unittest.main()
