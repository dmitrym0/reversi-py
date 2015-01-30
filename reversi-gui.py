#!/usr/bin/python
from Tkinter import *
import numpy
import reversi


class App:
    def __init__(self, master):
        self.board = numpy.zeros((8, 8), dtype=object)
        self.master = master
        self.reversi_board = reversi.ReversiBoard().set_default_board()
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


    def _replace_button_image_with_image(self, tuple, image):
        button = self.board[tuple[0]][tuple[1]]
        button.configure(image=image,command=lambda: self.handle_click(tuple[0],tuple[1]))
        button.image = image

        button.pack(side=LEFT)


    def handle_click(self, x,y):
        if (x,y) in self.current_legal_moves:
            self.update_board_with_move((x,y))
        else:
            print "not ok"

    def update_board_with_move(self, tuple):
        flips = self.reversi_board.islegal(tuple, self.current_move)
        self.reversi_board.flip(flips, self.current_move)
        self.current_move = self.reversi_board.opposite_color(self.current_move)
        self.current_legal_moves = self.reversi_board.getlegalmovesforcolor(self.current_move)
        self.redraw(self.reversi_board)
        self.higlight_legal_moves(self.current_legal_moves)


root = Tk()

app = App(root)
root.mainloop()
root.destroy() # optional; see description below
