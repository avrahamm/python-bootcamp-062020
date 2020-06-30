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

    def test_board_eq_init(self):
        board_size = 3
        board_3 = Board(board_size)
        board_3.board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        board = Board(board_size)
        self.assertEqual(board_3, board)

    def test_board_eq(self):
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
        valid_move = [0, 1]
        invalid_move = [0, 4]
        board_size = 3
        board_3 = Board(board_size)
        board_3.board = [
            ['x', 'o', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]

        self.assertEqual(board_3, board)


if __name__ == '__main__':
    unittest.main()
