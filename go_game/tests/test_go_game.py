import unittest
from go_game.go_game import Board

class TestGoGame(unittest.TestCase):
    def test_capture_simple(self):
        b = Board(3)
        b.play_move(1, 1, 'white')
        b.play_move(0, 1, 'black')
        b.play_move(1, 0, 'black')
        b.play_move(1, 2, 'black')
        b.play_move(2, 1, 'black')
        self.assertEqual(b.board[1][1], '.')

    def test_suicide_not_allowed(self):
        b = Board(3)
        b.play_move(0, 1, 'black')
        b.play_move(1, 0, 'black')
        b.play_move(1, 2, 'black')
        b.play_move(2, 1, 'black')
        self.assertFalse(b.play_move(1, 1, 'white'))
        self.assertEqual(b.board[1][1], '.')

    def test_generate_random_move_full_board(self):
        b = Board(1)
        b.play_move(0, 0, 'black')
        self.assertIsNone(b.generate_random_move('white'))

if __name__ == '__main__':
    unittest.main()
