from evaluations.material import materialEvaluation,materialCount
from evaluations.PieceSquareTables import tableEvaluation
from evaluations.simpleScore import simpleScore
import chess

def getChildren(board:chess.Board,maximizing_player): # needs maxamizing player to be reversed because it passes one layer down
    children = []
    for move in board.legal_moves:
        if board.is_capture(move):
            child = board.copy()
            child.push(move)
            score = simpleScore(board, child, move, maximizing_player)
            children.append((child, move, score))
    return sorted(children,key=lambda x:x[2],reverse=maximizing_player)
i = 0

def quiescenceSearch(board:chess.Board,maximizing_player, alpha, beta, options,evaluation = None):
    global i
    i += 1
    # if evaluation is None:
    #     standPatValue = materialEvaluation(board) + tableEvaluation(board) / 20
    # else:
    #     standPatValue = evaluation
    standPatValue = materialEvaluation(board) + tableEvaluation(board) / 20
    if maximizing_player:
        if standPatValue >= beta:
            return beta
        alpha = max(alpha,standPatValue)
    else:
        if standPatValue <= alpha:
            return alpha
        beta = min(standPatValue,beta)

    moves = getChildren(board, not maximizing_player)
    for child, move, _ in moves:
        # if board.is_en_passant(move):
        #     capture = 1
        # else:
        #     capture = materialCount[board.piece_type_at(move.to_square) - 1]
        if maximizing_player:
            evaluation = quiescenceSearch(child, not maximizing_player, alpha, beta, options)  # standPatValue + capture
        else:
            evaluation = quiescenceSearch(child, not maximizing_player, alpha, beta, options)  # standPatValue - capture
        if maximizing_player:
            if evaluation >= beta:
                return beta
            alpha = max(alpha,standPatValue)
        else:
            if evaluation <= alpha:
                return alpha
            beta = min(standPatValue,beta)
    if maximizing_player:
        return alpha
    else:
        return beta