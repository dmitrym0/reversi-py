import numpy
import reversi

class ReversiEvaluator:
    def __init__(self):
        self.scores =      ([[ 100.,  -20.,  020.,  010.,  010.,  020.,  -20.,  100.],
                             [ -20.,  -20.,  000.,  000.,  000.,  000.,  -20.,  -20.],
                             [ 020.,  000.,  000.,  000.,  000.,  000.,  000.,  020.],
                             [ 010.,  000.,  000.,  000.,  000.,  000.,  000.,  000.],
                             [ 010.,  000.,  000.,  000.,  000.,  000.,  000.,  000.],
                             [ 020.,  000.,  000.,  000.,  000.,  000.,  000.,  020.],
                             [ -20.,  -20.,  000.,  000.,  000.,  000.,  -20.,  -20.],
                             [ 100.,  -20.,  020.,  010.,  010.,  020.,  -20.,  100.]])

    def evaluate_board(self, board):
        whitescore = 0
        blackscore = 0
        for x in range(8):
            for y in range(8):
                tuple = (x,y)
                if board.iswhite(tuple):
                    whitescore += self.scores[x][y]
                if board.isblack(tuple):
                    blackscore += self.scores[x][y]
        return {reversi.WHITE: whitescore, reversi.BLACK: blackscore}

