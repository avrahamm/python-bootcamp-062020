import unittest
from unittest.mock import MagicMock, patch
from main import main
from io import StringIO


class TestMain(unittest.TestCase):
    def setUp(self):
        self.fake_input = MagicMock()
        self.fake_output = StringIO()

    def tearDown(self):
        self.fake_input = None
        self.fake_output = None

    def test_main_2(self):
        board_size = '2'
        self.fake_input.side_effect = ['A', 'Bb', board_size, '1,1', '1,0', 'N']

        with patch('builtins.input', self.fake_input), patch('sys.stdout', self.fake_output):
            main()
            print(self.fake_output)
            self.assertTrue('x! Reuven won\n' in self.fake_output.getvalue())

    def test_main_3(self):
        board_size = '3'
        self.fake_input.side_effect = ['A', 'Bb', board_size, '1,0', '1,1', '1,2', 'N']

        with patch('builtins.input', self.fake_input), patch('sys.stdout', self.fake_output):
            main()
            print(self.fake_output)
            self.assertTrue('x! Reuven won\n' in self.fake_output.getvalue())


if __name__ == '__main__':
    unittest.main()
