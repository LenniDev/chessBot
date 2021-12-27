import bot
import chess
import time

board = chess.Board()
puzzles = [
    ('5r2/1b3pbk/pp2N1pp/3qn3/8/PQPB3P/6P1/3R2K1 w - - 1 23','d3g6',4),
    ('5rk1/3n1pp1/2pr3p/8/3qPP2/P5P1/1PP1Q2P/R4R1K w - - 5 24','a1d1',4),
    ('2r3r1/2k5/2p1p3/4PpP1/1Q1N3P/3q4/P5P1/6K1 w - - 6 44','e4d6',4),
]

bot.i = 0
t1 = time.time()
for fen,bestMove,depth in puzzles:
    board.set_fen(fen)
    eval, move = bot.minimax(board, depth, True)
    t2 = time.time()
    print(move,bestMove,eval,t2 - t1)

print('Nodes=',bot.i)


