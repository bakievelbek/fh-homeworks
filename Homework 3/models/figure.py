from position import Position


class ChessFigure:
    """ChessFigure Superclass. All ChessFigure objects inherit the ChessFigure class"""
    shape = str
    position = Position

    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, position_from, position_to):
        pass

    def beat(self, beats, beaten, position_to, position_from):
        can_beat = self.move(position_to, position_from)
        if can_beat:
            print(f"{beats.color} {beats.title} beats {beaten.color} {beaten.title}")
            return can_beat
        return False

    @staticmethod
    def convert_letter_to_num(letter):
        if letter.lower() == 'a':
            return 1
        if letter.lower() == 'b':
            return 2
        if letter.lower() == 'c':
            return 3
        if letter.lower() == 'd':
            return 4
        if letter.lower() == 'e':
            return 5
        if letter.lower() == 'f':
            return 6
        if letter.lower() == 'g':
            return 7
        if letter.lower() == 'h':
            return 8


class Pawn(ChessFigure):
    shape = "P"
    title = "Pawn"
    value = "2"
    first_move = True

    def move(self, position_from, position_to):
        print("Pawn is moving")
        if self.first_move:
            if self.convert_letter_to_num(position_to.y) == self.convert_letter_to_num(
                    position_from.y) and int(position_to.x) - int(position_from.x) <= 2:
                self.first_move = False
                return position_to

            else:
                print(f"Pawn cannot move to {position_to}")
        else:
            if self.convert_letter_to_num(position_to.y) == self.convert_letter_to_num(
                    position_from.y) and int(position_from.x) - int(position_to.x) == 1:
                self.first_move = False
                return position_to
            else:
                print("Pawn cannot move through 2 or more squares 2 and more times")
        return False

    def beat(self, beats, beaten, position_to, position_from):
        if beaten.title == "King":
            print("Pawn cannot beat a King")
            return False
        if position_to.y != position_from.y and abs(
                int(position_from.x) - int(position_to.x)) == 1 and beaten.title != "King":
            print(f"{beats.color} Pawn beats {beaten.color} {beaten.title}")
            return True
        return False


class Knight(ChessFigure):
    shape = "G"
    title = "Knight"
    value = "3"

    def move(self, position_from, position_to):
        if abs(int(position_from.x) - int(position_to.x)) == 2 and abs(
                self.convert_letter_to_num(position_from.y) - self.convert_letter_to_num(position_to.y)) == 1 \
                or abs(int(position_from.x) - int(position_to.x)) == 1 and \
                abs(self.convert_letter_to_num(position_from.y) - self.convert_letter_to_num(position_to.y)) == 2:
            return position_to
        else:
            print(f"Knight cannot move to {position_to}")
        return False


class Rook(ChessFigure):
    shape = "R"
    title = "Rook"
    value = "7"

    def move(self, position_from, position_to):
        if position_from.x == position_to.x or position_from.y == position_to.y:
            return position_to
        else:
            print(f"Rook cannot move to {position_to}")
        return False


class Bishop(ChessFigure):
    shape = "B"
    title = "Bishop"
    value = "7"

    def move(self, position_from, position_to):
        if abs(int(position_from.x) - int(position_to.x)) == abs(
                self.convert_letter_to_num(position_from.y) - self.convert_letter_to_num(position_to.y)):
            return position_to
        else:
            print(f"Bishop cannot move to {position_to}")
        return False


class Queen(ChessFigure):
    shape = "Q"
    title = "Queen"
    value = "7"

    def move(self, position_from, position_to):
        if position_from.x == position_to.x or position_from.y == position_to.y:
            return position_to
        if abs(int(position_from.x) - int(position_to.x)) == abs(
                self.convert_letter_to_num(position_from.y) - self.convert_letter_to_num(position_to.y)):
            return position_to
        else:
            print(f"Queen cannot move to {position_to}")
        return False


class King(ChessFigure):
    shape = "K"
    title = "King"
    value = "1"
    first_move = True

    def move(self, position_from, position_to):
        if abs(int(position_from.x) - int(position_to.x)) <= 1 and abs(
                self.convert_letter_to_num(position_from.y) - self.convert_letter_to_num(position_to.y)) <= 1:
            return position_to
        else:
            print(f"King cannot move to {position_to}")
        return False

    def castling(self, position_from, position_to, position_of_rook):
        if not self.first_move:
            if abs(int(position_from.x) - int(position_to.x)) <= 1 and abs(
                    self.convert_letter_to_num(position_from.y) - self.convert_letter_to_num(position_to.y)) <= 1:
                if self.convert_letter_to_num(position_from.y) - self.convert_letter_to_num(position_to.y) > 0:
                    position_of_rook = Position(self.convert_letter_to_num(position_to.y) - 1, int(position_of_rook.x))
                else:
                    position_of_rook = Position(self.convert_letter_to_num(position_to.y) + 1, int(position_of_rook.x))
                return position_to, position_of_rook
