import unittest
from game_manager import GameManager


class GameTest(unittest.TestCase):
    def test_init_board(self):
        game = GameManager(3)
        board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        self.assertEqual(board, game.board)


if __name__ == '__main__':
    unittest.main()
