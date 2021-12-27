from copy import deepcopy as copy
import chess
import random
from evaluations.simpleScore import simpleScore
from evaluations.material import materialEvaluation
from evaluations.quiescenceSearch import quiescenceSearch

def getChildren(board:chess.Board,maximizing_player,sortMoves:bool):
    children = []
    for move in board.legal_moves:
        child = board.copy()
        child.push(move)
        if sortMoves:
            score = simpleScore(board,child,move,maximizing_player)
        else:
            score = 0
        children.append((child,move,score))
    return sorted(children,key=lambda x:x[2],reverse=maximizing_player)
i = 0

def minimax(board,depth,maximizing_player,alpha=-1000,beta=1000,options={'quiescenceSearch':True}):
    global i
    i+=1
    if board.is_game_over():
        if board.is_stalemate():
            return 0, None
        elif board.outcome().winner:
            return 100, None
        else:
            return -100, None
    if depth == 0:
        if options['quiescenceSearch']:
            return quiescenceSearch(board, maximizing_player, alpha, beta, options=options), None
        else:
            return materialEvaluation(board),None

    moves = getChildren(board, not maximizing_player, True)
    if maximizing_player:
        maximum = -1000
        maximumMove = None
        for child,move,_ in moves:
            evaluation,_ = minimax(child,depth-1,not maximizing_player,alpha,beta,options)
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
        for child,move,_ in moves:
            evaluation,_ = minimax(child,depth-1,not maximizing_player,alpha,beta)
            if evaluation<minimum:
                minimum=evaluation
                minimumMove = move
            if evaluation <= alpha:
                break
            beta = min(beta, evaluation)
        return minimum, minimumMove