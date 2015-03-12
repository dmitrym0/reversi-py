#!/usr/bin/python
from Tkinter import *
import numpy
import reversi
import reversievaluator


class App:
    def __init__(self, master):
        self.board = numpy.zeros((8, 8), dtype=object)
        self.master = master
        self.reversi_board = reversi.ReversiBoard().set_default_board()
        self.evaluator = reversievaluator.ReversiEvaluator()
        self._init_board()
        self.current_move = reversi.WHITE
        self.current_legal_moves = self.reversi_board.getlegalmovesforcolor(self.current_move)
        self.redraw(self.reversi_board)
        self.higlight_legal_moves(self.current_legal_moves)

    def _init_board(self):
        for y in range(8):
            frame = Frame(self.master)
            frame.pack()
            for x in range(8):
                image = PhotoImage(file="empty.gif")
                button = Button(frame, image=image, command=lambda: self.handle_click(x,y))
                button.image = image
                button.pack(side=LEFT)
                button.x = x
                button.y = y
                self.board[x][y] = button


    def redraw(self, board):
        for y in range(8):
            for x in range(8):
                image = None
                if board.iswhite((x,y)):
                    image = PhotoImage(file="white.gif")
                elif board.isblack((x,y)):
                    image = PhotoImage(file="black.gif")
                else:
                    image = PhotoImage(file="empty.gif")

                self._replace_button_image_with_image((x,y), image)

    def higlight_legal_moves(self, legalmoves):
        for legalmove in legalmoves:
            print "Highlighting ", legalmove
            image = PhotoImage(file="circle.gif")
            self._replace_button_image_with_image(legalmove, image)

    def higlight_white_moves(self, runs):
        for run in runs:
            for move in run:
                print "highlight white ", move
                image = PhotoImage(file="white-flipped.gif")
                self._replace_button_image_with_image(move, image)

    def higlight_black_moves(self, runs):
        for run in runs:
            for move in run:
                print "highlight black ", move
                image = PhotoImage(file="black-flipped.gif")
                self._replace_button_image_with_image(move, image)

    def _replace_button_image_with_image(self, tuple, image):
        button = self.board[tuple[0]][tuple[1]]
        button.configure(image=image,command=lambda: self.handle_click(tuple[0],tuple[1]))
        button.image = image
        button.pack(side=LEFT)


    def handle_click(self, x,y):
        if (x,y) in self.current_legal_moves:
            self.update_board_with_move((x,y))
        else:
            print "this move is not legal"

    def update_board_with_move(self, tuple):
        flips = self.reversi_board.islegal(tuple, self.current_move)
        self.reversi_board.flip(flips, self.current_move)
        computer_color = self.reversi_board.opposite_color(self.current_move)
        computer_move = self.evaluator.best(self.reversi_board,computer_color, self.current_move)
        print "Computer move=", computer_move
        computer_flips = self.reversi_board.islegal(computer_move[reversievaluator.MOVE], computer_color)
        self.reversi_board.flip(computer_flips, computer_color)
        self.current_legal_moves = self.reversi_board.getlegalmovesforcolor(self.current_move)
        self.redraw(self.reversi_board)
        self.higlight_legal_moves(self.current_legal_moves)
        self.higlight_white_moves(flips)
        self.higlight_black_moves(computer_flips)
        stats = self.reversi_board.boardstats()
        print "Pieces= White: ", stats[reversi.WHITE], " black: ", stats[reversi.BLACK]
        score = self.evaluator.evaluate_board(self.reversi_board)
        print "Score = White: ", score[reversi.WHITE], " black: ", score[reversi.BLACK]


root = Tk()

app = App(root)
root.mainloop()
root.destroy() # optional; see description below
