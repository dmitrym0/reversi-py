#!/usr/bin/python
import unittest
import reversi


class ReversiTest(unittest.TestCase):

    def setUp(self):
        self.board = reversi.ReversiBoard().set_default_board()

    def tearDown(self):
        self.board = None

    def test_up(self):
        tuple = (4, 3)
        result = self.board.up(tuple)
        self.assertEqual(result, (4, 2))

    def test_up_right(self):
        self.assertEqual(self.board.up_right((2, 2)), (3, 1))

    def test_right(self):
        self.assertEqual(self.board.right((2, 2)), (3, 2))

    def test_out_of_bounds(self):
        self.assertIsNone(self.board.right((7, 0)))

    def test_initial_layout(self):
        self.assertTrue(self.board.iswhite((4,4)))
        self.assertTrue(self.board.isblack((4,3)))
        self.assertTrue(self.board.isempty((1,1)))

if __name__ == '__main__':
    unittest.main()
