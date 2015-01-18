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

    def test_left(self):
        self.assertEqual(self.board.left((2, 2)), (1, 2))

    def test_up_left(self):
        self.assertEqual(self.board.up_left((2, 2)), (1, 1))

    def test_right(self):
        self.assertEqual(self.board.right((2, 2)), (3, 2))

    def test_down(self):
        self.assertEqual(self.board.down((2,2)), (2,3))

    def test_down_right(self):
        self.assertEqual(self.board.down_right((2, 2)), (3, 3))

    def test_out_of_bounds(self):
        self.assertIsNone(self.board.right((7, 0)))

    def test_initial_layout(self):
        self.assertTrue(self.board.iswhite((4,4)))
        self.assertTrue(self.board.isblack((4,3)))
        self.assertTrue(self.board.isempty((1,1)))

    def test_is_legal_for_a_spot_already_taken(self):
        self.assertFalse(self.board.islegal((4,4,), reversi.WHITE))

    def test_is_legal_for_random_empty_spot_thats_not_legal(self):
        self.assertFalse(self.board.islegal((0,0), reversi.WHITE))

    def test_is_legal_for_the_initial_position_that_should_be_legal(self):
        result = self.board.islegal((3,2), reversi.BLACK)
        self.assertEqual(result, [[(3, 3), (3, 4), (3, 2)]])

    def test_an_illegal_move_for_whites_initially(self):
        result = self.board.islegal((2,3), reversi.WHITE)
        self.assertEqual(result, [])


    def test_the_number_of_available_legal_moves(self):
        black_available_moves = self.board.getlegalmovesforcolor(reversi.BLACK)
        white_available_moves = self.board.getlegalmovesforcolor(reversi.WHITE)
        self.assertEqual(len(black_available_moves), 4)
        self.assertEqual(len(white_available_moves), 4)



if __name__ == '__main__':
    unittest.main()
