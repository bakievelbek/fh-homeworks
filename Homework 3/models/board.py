from figure import Pawn, Rook, Knight, Bishop, Queen, King
from position import Position


class ChessBoard:
    figures = {
        'Pawn': Pawn,
        'Rook': Rook,
        'Knight': Knight,
        'Bishop': Bishop,
        'Queen': Queen,
        'King': King,
    }

    def __init__(self):
        self.board = self.initialize()

    def initialize(self):
        """Initialize the game board"""
        board = [["0" for i in range(8)] for j in range(8)]
        color = 'white'
        x_axis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        for i in range(8):
            board[1][i] = Pawn(Position(x_axis[i], '2'), "white")
            board[6][i] = Pawn(Position(x_axis[i], '7'), "black")

        for i in range(0, 8, 7):
            board[i][0] = Rook(Position(x_axis[0], f'{i + 1}'), color)
            board[i][1] = Knight(Position(x_axis[1], f'{i + 1}'), color)
            board[i][2] = Bishop(Position(x_axis[2], f'{i + 1}'), color)
            board[i][3] = Queen(Position(x_axis[3], f'{i + 1}'), color)
            board[i][4] = King(Position(x_axis[4], f'{i + 1}'), color)
            board[i][5] = Bishop(Position(x_axis[5], f'{i + 1}'), color)
            board[i][6] = Knight(Position(x_axis[6], f'{i + 1}'), color)
            board[i][7] = Rook(Position(x_axis[0], f'{i + 1}'), color)
            color = 'black'

        return board

    def print_board(self):
        numbers = '123456789'
        print("   A B C D E F G H")
        print(' ')
        for i in range(7, -1, -1):
            print(numbers[i], end="  ")
            for k in range(8):
                if type(self.board[i][k]) != str:
                    print(self.board[i][k].shape, end=" ")
                else:
                    print(self.board[i][k], end=" ")
            print()
        print(' ')
        print("   A B C D E F G H")
        return self.board

    def find_figure(self, position_from):
        x = int(position_from.x) - 1
        y = self.convert_letter_to_num(position_from.y)
        try:
            square = self.board[x][y]
            print(f'The figure you want to move is {square.title}')
            coordinates = input('Please enter the position where you want to move. E.g `A2`: ')
            position_to = Position(coordinates[0], coordinates[1])
            is_free, figure_to_move = self.check_position(position_to, position_from, square)
            if is_free == 'fight':
                print('Next turn')

            if is_free is True:
                print(f"Position is free.")
                print(f"Moving {square.title}")
                new_position = square.move(position_from, position_to)
                if new_position:
                    self.update_board(square, position_from, new_position)

            if not is_free:
                print(f"Position is not free. {figure_to_move.title} in on {figure_to_move.position.pos}")
        except IndexError as e:
            print(e)

    def check_position(self, position_to, position_from, figure):
        x = int(position_to.x) - 1
        y = self.convert_letter_to_num(position_to.y)

        try:
            square = self.board[x][y]
            if square == '0':
                return True, False
            elif figure.color != square.color:
                is_captured = figure.beat(figure, square, position_to, position_from)
                self.fight(is_captured, figure, position_to, position_from)
                return 'fight', False
            else:
                return False, square
        except IndexError as e:
            print(e)

    def fight(self, is_captured, figure, position_to, position_from):
        if is_captured:
            self.update_board(figure, position_from, position_to)
        else:
            print("Wrong move")

    def update_board(self, figure, old_position, new_position):
        x_old = int(old_position.x) - 1
        x_new = int(new_position.x) - 1
        y_old = self.convert_letter_to_num(old_position.y)
        y_new = self.convert_letter_to_num(new_position.y)
        self.board[x_old][y_old] = '0'
        self.board[x_new][y_new] = self.figures[figure.title](new_position, figure.color)
        print("Board updated")
        self.print_board()

    @staticmethod
    def convert_letter_to_num(letter):
        if letter.lower() == 'a':
            return 0
        if letter.lower() == 'b':
            return 1
        if letter.lower() == 'c':
            return 2
        if letter.lower() == 'd':
            return 3
        if letter.lower() == 'e':
            return 4
        if letter.lower() == 'f':
            return 5
        if letter.lower() == 'g':
            return 6
        if letter.lower() == 'h':
            return 7
