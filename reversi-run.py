#!/usr/bin/python

import reversi
import pprint


pp = pprint.PrettyPrinter(indent=4)
b = reversi.ReversiBoard().set_default_board()
pp.pprint(b.getboard())

flips = b.islegal((2,3), reversi.WHITE)
# flips = b.islegal((3, 2), reversi.BLACK)
b.flip(flips, reversi.WHITE)
pp.pprint(b.getboard())
pp.pprint(flips)

#white_available_moves = b.getlegalmovesforcolor(reversi.WHITE)
#pp.pprint(white_available_moves)