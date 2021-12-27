import chess

king = chess.KING

def virtualMobility(board):
    board = board.copy()
    queen = chess.QUEEN
    whiteKing = list(board.pieces(king, chess.WHITE))[0]
    board.set_piece_at(
        whiteKing,
        chess.Piece(queen,chess.WHITE)
    )
    whiteMobility = len(board.attacks(whiteKing))

    blackKing = list(board.pieces(king, chess.BLACK))[0]
    board.set_piece_at(
        blackKing,
        chess.Piece(queen,chess.BLACK)
    )
    blackMobility = len(board.attacks(blackKing))
    return blackMobility - whiteMobility  # mobility is bad

shieldValue = [1,2.2,2,2,3,0]
attackValue = [1,3,3,4,7,1]
def kingShield(board:chess.Board):
    shieldMaterial = 0
    whiteKing = list(board.pieces(king, chess.WHITE))[0]

    possibleShield = [whiteKing + 8, whiteKing + 9, whiteKing + 7, whiteKing + 16, whiteKing + 17, whiteKing + 15]
    for possibleShieldMaterial in possibleShield:
        try:
            if board.color_at(possibleShieldMaterial) is chess.WHITE:
                shieldMaterial += shieldValue[board.piece_type_at(possibleShieldMaterial) - 1]
            elif board.color_at(possibleShieldMaterial) is chess.BLACK:
                shieldMaterial -= attackValue[board.piece_type_at(possibleShieldMaterial) - 1]
        except IndexError:
            pass
    blackKing = list(board.pieces(king, chess.BLACK))[0]
    possibleShield = [blackKing - 8, blackKing - 9, blackKing - 7, blackKing - 16, blackKing - 17, blackKing - 15]
    for possibleShieldMaterial in possibleShield:
        try:
            if board.color_at(possibleShieldMaterial) is chess.BLACK:
                shieldMaterial -= shieldValue[board.piece_type_at(possibleShieldMaterial) - 1]
            elif board.color_at(possibleShieldMaterial) is chess.WHITE:
                shieldMaterial += attackValue[board.piece_type_at(possibleShieldMaterial) - 1]
        except IndexError:
            pass
    return shieldMaterial + 2 * virtualMobility(board)

def kingSafety(board):
    return 0.1*kingShield(board) + virtualMobility(board)

if __name__ == '__main__':
    b = chess.Board()
    b.set_fen('r2qkbnr/ppp1pppp/2npb3/8/8/8/PPPP1PPP/RNBQKBNR w KQkq - 0 4')
    print(virtualMobility(b))