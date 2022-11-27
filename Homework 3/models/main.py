from figure import ChessFigure
from board import ChessBoard
from position import Position


class Chess:
    chess_figure = ChessFigure
    board = ChessBoard()

    def start(self):
        self.board.print_board()
        while True:
            coordinates = input("This is your board. "
                                "Make a move by entering the position of figure that you want to move. E.g `A2`: ")
            position = Position(coordinates[0], coordinates[1])

            self.board.find_figure(position)

    def __init__(self):
        self.start()


chess = Chess()
