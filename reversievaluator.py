import numpy
import reversi
import copy


SCORE = "score"
MOVE = "move"

class ReversiEvaluator:
    def __init__(self):
        self.scores =      ([[ 100.,  -20.,  020.,  010.,  010.,  020.,  -20.,  100.],
                             [ -20.,  -20.,  050.,  050.,  050.,  010.,  -20.,  -20.],
                             [ 020.,  010.,  010.,  000.,  010.,  010.,  010.,  020.],
                             [ 010.,  050.,  020.,  000.,  010.,  010.,  050.,  010.],
                             [ 010.,  010.,  030.,  000.,  010.,  010.,  050.,  010.],
                             [ 020.,  050.,  040.,  000.,  010.,  010.,  010.,  020.],
                             [ -20.,  -20.,  050.,  050.,  050.,  050.,  -20.,  -20.],
                             [ 100.,  -20.,  020.,  010.,  010.,  020.,  -20.,  100.]])

    def best(self, board, player, opponent):
        self.original = player
        result = self.minimax(board,2, player, opponent)
        return result

    def minimax(self, board, ply, player, opponent):
        best = {MOVE: (), SCORE: -100000}
        moves = board.getlegalmovesforcolor(player)

        if ply == 0 or len(moves) == 0:
            score =  self.evaluate_board(board)
            return {MOVE: (), SCORE: score[player]}

        for move in moves:
            new_board = copy.deepcopy(board)
            computer_flips = new_board.islegal(move, player)
            new_board.flip(computer_flips, player)
            result = self.minimax(new_board, ply-1, opponent, player)
            if player == self.original:
                if result[SCORE] >= best[SCORE]:
                    best = {MOVE: move, SCORE:result[SCORE]}
            else:
                if result[SCORE] <= best[SCORE]:
                    best = {MOVE: move, SCORE:result[SCORE]}
        return best

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
