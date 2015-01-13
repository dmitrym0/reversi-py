#!/usr/bin/python
import numpy


BLACK = 2
WHITE = 1
EMPTY = 0


class ReversiBoard:
    def __init__(self):
        self.board = numpy.zeros((8,8))

    def set_default_board(self):
        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 1
        return self

    def getboard(self):
        return self.board

    def islegal(self, tuple, color):
        return false

    def up(self, tuple):
        return self.new_tuple_or_null((tuple[0], tuple[1] - 1))

    def down(self, tuple):
        return self.new_tuple_or_null((tuple[0], tuple[1] + 1))

    def left(self, tuple):
        return self.new_tuple_or_null((tuple[0]-1, tuple[1]))

    def right(self, tuple):
        return self.new_tuple_or_null((tuple[0]+1, tuple[1]))

    def up_right(self, tuple):
        return self.up(self.right(tuple))

    def up_left(self, tuple):
        return self.up(self.left(tuple))

    def down_left(self, tuple):
            return self.down(self.left(tuple))

    def down_right(self, tuple):
        return self.down(self.right(tuple))

    def new_tuple_or_null(self, new_tuple):
        if self.inbound(new_tuple):
            return new_tuple
        return None 

    def inbound(self, tuple):
        return tuple[0] >= 0 and tuple[0] < 8 and tuple[1] >= 0 and tuple[1] < 8