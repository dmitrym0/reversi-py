#!/usr/bin/python
import numpy


BLACK = 2
WHITE = 1
EMPTY = 0


class ReversiBoard:
    def __init__(self):
        self.board = numpy.zeros((8, 8))

    def set_default_board(self):
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        return self

    def getboard(self):
        return self.board

    def islegal(self, tuple, color):
        if not self.isempty(tuple):
            return []
        return self._generateFlipsFor(tuple,color)


    def up(self, tuple):
        if tuple is None:
            return None
        return self.new_tuple_or_null((tuple[0], tuple[1] - 1))

    def down(self, tuple):
        if tuple is None:
            return None
        return self.new_tuple_or_null((tuple[0], tuple[1] + 1))

    def left(self, tuple):
        if tuple is None:
            return None
        return self.new_tuple_or_null((tuple[0]-1, tuple[1]))

    def right(self, tuple):
        if tuple is None:
            return None
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

    def isempty(self, tuple):
        return self.isposition(tuple, EMPTY)

    def isblack(self, tuple):
        return self.isposition(tuple, BLACK)

    def iswhite(self, tuple):
        return self.isposition(tuple, WHITE)

    def isposition(self, tuple, color):
        return self.board[tuple[0]][tuple[1]] == color

    def settupletocolor(self, tuple, color):
        self.board[tuple[0]][tuple[1]] = color

    def opposite_color(self, color):
        if color == WHITE:
            return BLACK
        return WHITE

    def flip(self, flips, color):
        for run in flips:
            for tuple in run:
                self.settupletocolor(tuple, color)


    def _generateFlipsFor(self, tuple, color):
        flipped_positions = []
        current_run = []
        opposite_color = self.opposite_color(color)
        directionals = [self.up, self.up_left, self.up_right, self.down, self.down_right, self.down_left, self.left, self.right]
        for direction in directionals:
            current_run = []
            new_position = direction(tuple)
            while (new_position is not None):
                # we got more than one flipped coordinate and now hit our color stone, so this is a valid run
                if (len(current_run) > 0 and self.isposition(new_position, color)):
                    current_run.append(new_position) # append the end of the run
                    current_run.append(tuple)        # append the start of the run
                    flipped_positions.append(current_run)
                    break
                elif (self.isposition(new_position, opposite_color)):
                    current_run.append(new_position)
                else:
                    break
                new_position  = direction(new_position)
        return flipped_positions

