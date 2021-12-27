import numpy as np
import chess

table = [
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1.5, 3.5, 5, 5, 5, 1.5, 1.5, 1.5],
            [1, 1, 3, 4.5, 4.5, 1, 1, 1],
            [0, 0, 2.5, 4.5, 4.5, 0, 0, 0],
            [-1, -1, 2, 4, 4, 0, -1, 0],
            [1, -1, 1, 0, 0, -1, -1, 1],
            [1, 1, 1, -4, -4, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
         ],
        [
            [1, 2, 2, 3, 3, 2, 2, 1],
            [1, 2, 3, 4, 4, 3, 2, 1],
            [1, 2, 3, 4, 4, 3, 2, 1],
            [0, 1, 2, 3, 3, 2, 1, 0],
            [0, 0, 1, 2, 2, 1, 0, 0],
            [-2, -1, 0, 1, 1, 0, -1, -2],
            [-3, -3, -2, -1, -1, -2, -3, -3],
            [-4, -3, -2, -2, -2, -2, -3, -4],
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 1, 1, 2, 2, 2],
            [-1, 2, 0, 0, 0, 0, 2, 0],
            [1.5, 1, -2, -2, -2, -2, 1, 1.5],
        ],
        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 0, -1],
            [-1, 0, 0, 1, 1, 0, 0, -1],
            [-1, 0, 1, 2, 2, 1, 0, -1],
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        [
            [-3, -3, -3, -3, -3, -3, -3, -3],
            [-3, -3, -3, -3, -3, -3, -3, -3],
            [-3, -3, -3, -3, -3, -3, -3, -3],
            [-3, -3, -3, -3, -3, -3, -3, -3],
            [-3, -3, -3, -3, -3, -3, -3, -3],
            [-1, -1, -1, -2.5, -2.5, -1, -1, -1],
            [2, -1, -1, -2.5, -2.5, -1, 0, 2],
            [3, 3, 0, -1, -1, 0, 3, 3]
        ]
]
def pieceSquareTable(piece, square):
    x, y = square
    return table[piece][7-y][x]


def square_to_index(square, turn: bool):
    if turn:
        return square % 8, 7 - square // 8
    else:
        return square % 8, square // 8

def evaluatePieceScope(board,piece,square):
    if piece == chess.BISHOP:
        return len(board.attacks(square)) / 8
    if piece == chess.ROOK:
        return len(board.attacks(square)) / 4
    if piece == chess.QUEEN:
        return len(board.attacks(square)) / 12
    return 0


def tableEvaluation(board: chess.Board):
    position = 0
    for piece in chess.PIECE_TYPES:
        for square in board.pieces(piece, chess.WHITE):
            position += pieceSquareTable(piece-1,square_to_index(square,False))
            position += evaluatePieceScope(board,piece,square)
        for square in board.pieces(piece, chess.BLACK):
            position -= pieceSquareTable(piece-1,square_to_index(square,True))
            position -= evaluatePieceScope(board,piece,square)
    return position

if __name__ == '__main__':
    board = chess.Board()
    import time
    t1 = time.time()
    for i in range(100000):
        tableEvaluation(board)
    t2 = time.time()
    print(t2-t1)
