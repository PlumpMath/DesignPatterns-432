import io
import itertools
import os
import sys
import tempfile
import unicodedata

def main():
    checkers = CheckersBoard()
    print(checkers)

    chess = ChessBoard()
    print(chess)

    if sys.platform.startswith("win"):
        filename = os.path.join(tempfile.gettempdir(), "gameboard.txt")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sys.stdout.getvalue())
        print("wrote '{}'".format(filename), file=sys.__stdout__)

if sys.platform.startswith("win"):
    def console(char, background):
        return char or " "
    sys.stdout = io.StringIO()
else:
    def console(char, background):
        return "\x1B[{}m{}\x1B[0m".format(
                43 if background == BLACK else 47, char or " ")

class AbstractBoard:

    def __init__(self, rows, columns):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()


    def populate_board(self):
        raise NotImplementedError()


    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            squares.append("\n")
        return "".join(squares)

class CheckersBoard(AbstractBoard):

    def __init__(self):
        self.populate_board()


    def populate_board(self): # Thanks to Doug Hellmann for the idea!
        def black():
            return create_piece(DRAUGHT, BLACK)
        def white():
            return create_piece(DRAUGHT, WHITE)
        rows = ((None, black()), (black(), None), (None, black()),
                (black(), None),            # 4 black rows
                (None, None), (None, None), # 2 blank rows
                (None, white()), (white(), None), (None, white()),
                (white(), None))            # 4 white rows
        self.board = [list(itertools.islice(
            itertools.cycle(squares), 0, len(rows))) for squares in rows]