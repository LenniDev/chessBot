from evaluations.material import material
from evaluations.PieceSquareTables import tableEvaluation
from evaluations.kingSafety import kingSafety

def positionalEvaluation(board):
    if board.is_repetition(3):
        return 0
    materialBalance = material(board)
    #kingSafetyFactor = kingSafety(board)
    pieceActivity = tableEvaluation(board)
    return materialBalance*10 + pieceActivity# + kingSafe