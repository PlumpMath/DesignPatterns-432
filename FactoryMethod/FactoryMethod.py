import io

BLACK, WHITE = ("BLACK", "WHITE")

def main():
    checkers = CheckersBoard()
    print(checkers)

    chess = ChessBoard()
    print(chess) # 打印的时候会调用AbstractBoard的__str__方法

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