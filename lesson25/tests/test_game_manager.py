import unittest
from score import Score
from board import Board
from human_player import HumanPlayer
from ai_player import AIPlayer
from game_manager import GameManager


class GameManagerTest(unittest.TestCase):
    def setUp(self):
        self.score_keeper = Score()
        self.h1 = HumanPlayer(self.score_keeper, 'x', "Reuven")
        self.h2 = HumanPlayer(self.score_keeper, 'o', "Shimon")
        self.a1 = AIPlayer(self.score_keeper, 'x', "Bot1")
        self.a2 = AIPlayer(self.score_keeper, 'o', "Bot2")

    def tearDown(self):
        self.fake_input = None
        self.fake_output = None

    def test_game_over_winner(self):
        board_size = 3
        game_manager = GameManager(self.a1, self.a2, board_size)
        board = Board(board_size)
        board.board = [
            ['o', '.', '.'],
            ['x', 'x', 'x'],
            ['o', '.', '.']
        ]
        game_manager.board = board
        self.assertTrue(game_manager.game_over())

    def test_game_over_full(self):
        board_size = 3
        game_manager = GameManager(self.a1, self.a2, board_size)
        board = Board(board_size)
        board.board = [
            ['o', 'o', 'x'],
            ['x', 'x', 'o'],
            ['o', 'x', 'o']
        ]
        game_manager.board = board
        self.assertTrue(game_manager.game_over())

    def test_game_not_over(self):
        board_size = 3
        game_manager = GameManager(self.a1, self.a2, board_size)
        board = Board(board_size)
        board.board = [
            ['o', '.', '.'],
            ['x', 'x', '.'],
            ['o', '.', '.']
        ]
        game_manager.board = board
        self.assertFalse(game_manager.game_over())


if __name__ == '__main__':
    unittest.main()
