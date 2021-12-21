import chess
import random

materialCount = [1,2.8,3.2,5,9,0]  # king only worth 0 because cant be caputered
def materialEvaluation(board:chess.Board):
    if board.is_repetition(3):
        return 0
    material = 0
    for piece in chess.PIECE_TYPES:
        for _ in board.pieces(piece, chess.WHITE):
            material += materialCount[piece - 1]
        for _ in board.pieces(piece, chess.BLACK):
            material -= materialCount[piece - 1]
    return material +random.random()*0.1
