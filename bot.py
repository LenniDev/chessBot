from copy import deepcopy as copy
import chess
from evaluations.simpleScore import simpleScore
from evaluations.material import materialEvaluation
from evaluations.quiescenceSearch import quiescenceSearch
from variation import VariationRoot

def getChildren(board:chess.Board,maximizing_player,sortMoves:bool,previousVariation):
    children = []
    if previousVariation is None:
        childVariations = []
    else:
        childVariations = previousVariation.getChildrenAsMoves()
    legalMoves = board.legal_moves
    def deleteMove(moveToCheck):
        for move in legalMoves:
            if move == moveToCheck:
                del move
                break

    for move, score, childVariation in childVariations:
            child = board.copy()
            child.push(move)
            children.append((child,move,score,childVariation))
            deleteMove(move)
    for move in legalMoves:
        child = board.copy()
        child.push(move)
        if sortMoves:
            score = simpleScore(board,child,move,maximizing_player)/100
        else:
            score = 0
        children.append((child,move,score,None))
        
    return sorted(children,key=lambda x:x[2],reverse=maximizing_player)


def minimax(
    board,
    depth,
    maximizing_player,
    alpha=-1000,beta=1000,
    options={
        'quiescenceSearch':True,
        'variation':{
            'save':True,'maxbranchSize':5
        }
    }
    ,currentVariation=None
    ,previousVariation=None):
    if board.is_game_over():
        if board.is_stalemate():
            return 0, None
        elif board.outcome().winner:
            return 100, None
        else:
            return -100, None
    if depth == 0:
        if options['quiescenceSearch']:
            return quiescenceSearch(
                board,
                maximizing_player,
                alpha, beta,
                options=options), None
        else:
            return materialEvaluation(board),None
    if options['variation']['save'] and currentVariation is None:
        currentVariation = VariationRoot()

    moves = getChildren(board, not maximizing_player, True,previousVariation)
    if maximizing_player:
        maximum = -1000
        maximumMove = None
        for child,move,_,previousVariationChild in moves:
            childVariation = currentVariation.appendChild()
            evaluation,_ = minimax(
                child,
                depth-1,
                not maximizing_player,
                alpha,beta,
                options,
                currentVariation=childVariation,
                previousVariation=previousVariationChild
            )
            childVariation.move=move
            childVariation.evaluation=evaluation
            if evaluation>maximum:
                maximum=evaluation
                maximumMove = move
            if evaluation >= beta:
                break
            alpha = max(alpha, evaluation)
        return maximum, maximumMove
    else:
        minimum = 1000
        minimumMove = None
        for child,move,_,previousVariationChild in moves:
            childVariation = currentVariation.appendChild()
            evaluation,_ = minimax(
                child,
                depth-1,
                not maximizing_player,
                alpha,beta,
                options,
                currentVariation=childVariation,
                previousVariation=previousVariationChild)
            childVariation.move=move
            childVariation.evaluation=evaluation
            if evaluation<minimum:
                minimum=evaluation
                minimumMove = move
            if evaluation <= alpha:
                break
            beta = min(beta, evaluation)
        return minimum, minimumMove