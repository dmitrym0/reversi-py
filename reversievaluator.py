import numpy
import reversi
import copy

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


class ReversiThinker:
    def __init__(self, evaluator, board, mycolor):
        self.evaluator = evaluator
        self.board = board
        self.mycolor = mycolor
        self.maxdepth = 3
        self._resetscore()

    def _resetscore(self):
        self.bestscore = -1000
        self.besttuple = (0,0)
        self.evals = 0

    def make_move(self):
        self._resetscore()
        moves = self.board.getlegalmovesforcolor(self.mycolor)
        for tuple in moves:
            result = self.walkthetree(tuple, copy.deepcopy(self.board), 0)
            if result is not None:
                return tuple

        print "Best score=", self.bestscore, " best move=", self.besttuple, " evals=", self.evals
        return self.besttuple

    def walkthetree(self, tuple, board, depth):
        print "Depth=", depth
        computer_flips = board.islegal(tuple, self.mycolor)
        board.flip(computer_flips, self.mycolor)
        moves = board.getlegalmovesforcolor(self.mycolor)
        self.evals += 1
        # print "Score=", score, " best=", self.bestscore, "tuple=", tuple

        if (depth >= self.maxdepth):
            score = self.evaluator.evaluate_board(board)[self.mycolor]
            if (score > self.bestscore):
                self.besttuple = tuple
                self.bestscore = score
            return score
        for tuple in moves:
            score = self.walkthetree(tuple, copy.deepcopy(board), depth + 1)
            if score is not None:
                return score
        return

