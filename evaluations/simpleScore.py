import chess
from evaluations.material import materialCount

def simpleScore(board,child,move,maximizing_player): # needs maxamizing player to be reversed because it passes one layer down
    if maximizing_player:
        color = chess.WHITE
    else:
        color = chess.BLACK
    score = 0
    if board.is_en_passant(move):
        score += 3
    elif board.is_capture(move):
        score += 8 * (
                (
                        1 + materialCount[board.piece_type_at(move.to_square) - 1]
                ) / (
                        1 + materialCount[board.piece_type_at(move.from_square) - 1]
                )
        )
    if move.promotion is not None:
        score += 40
    if child.is_check():
        if maximizing_player:
            score += 10
        else:
            score -= 10
    for attack in child.attacks(move.to_square):
        piece = child.piece_type_at(attack)
        if piece is not None:
            score += materialCount[piece - 1]
    for attack in child.attackers(color, move.to_square):
        piece = child.piece_type_at(attack)
        if piece is not None:
            score -= materialCount[piece - 1]
    return score