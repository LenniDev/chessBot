import bot
import chess
import time

board = chess.Board()
fens = [
    '3r1rk1/1bq2ppp/p2p2n1/1p2n3/1Pp1P3/P1N2N2/2QRBPPP/3R2K1 w - - 8 19',
    '8/8/N2kp2Q/1p2b3/3n4/r7/3K4/8 w - - 0 47',
    '1q3rk1/p2R1ppp/1p2r3/1Q6/2P1R2P/P4P2/5P2/7K w - - 3 27',
    '5rk1/5pp1/3r3p/1pp1p3/3qP3/1P1P2RP/2PQ2P1/3R3K w - - 2 34',
    '2rq1rk1/pppbnppp/4pn2/3p2B1/2PP4/P1PBPN2/2Q2PPP/R4RK1 w Q - 5 9'
]

bot.i = 0
t1 = time.time()
for fen in fens:
    board.set_fen(fen)
    _, move = bot.minimax(board, 3, True)
    print(move, bot.i)
    t2 = time.time()
    print(t2 - t1)
print('Nodes=',bot.i)


