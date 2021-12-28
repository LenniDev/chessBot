import chess
import random

materialCount = [1,2.8,3.2,5,9,0]  # king only worth 0 because cant be caputered

def whiteMaterial(board):
    material = 0
    for piece in chess.PIECE_TYPES:
        for _ in board.pieces(piece, chess.WHITE):
            material += materialCount[piece - 1]
    return material

def blackMaterial(board):
    material = 0
    for piece in chess.PIECE_TYPES:
        for _ in board.pieces(piece, chess.BLACK):
            material += materialCount[piece - 1]
    return material

def material(board):
    return whiteMaterial(board) - blackMaterial(board)


def materialEvaluation(board:chess.Board):
    if board.is_repetition(3):
        return 0
    return material(board)  # + random.random()*0.1
