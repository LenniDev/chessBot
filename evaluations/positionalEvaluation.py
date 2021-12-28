from evaluations.material import whiteMaterial, blackMaterial
from evaluations.PieceSquareTables import tableEvaluation
from evaluations.kingSafety import kingSafety

def positionalEvaluation(board):
    if board.is_repetition(3):
        return 0
    whiteMaterialBalance = whiteMaterial(board)
    blackMaterialBalance = blackMaterial(board)
    #kingSafetyFactor = kingSafety(board)
    if blackMaterialBalance<14:
        whiteGamePhase = 1
    else:
        whiteGamePhase = 0
    if whiteMaterialBalance<14:
        blackGamePhase = 1
    else:
        blackGamePhase = 0
    materialBalance = whiteMaterialBalance - blackMaterialBalance
    pieceActivity = tableEvaluation(board,whiteGamePhase,blackGamePhase)
    return materialBalance*10 + pieceActivity# + kingSafe