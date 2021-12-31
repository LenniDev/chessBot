import bot
import chess
import time
import evaluations.quiescenceSearch as w
import evaluations.material as k

board = chess.Board()
pgns = []
white = 0
black = 0
for i in range(10000):
    pgn = ''
    #t1 = time.time()
    whiteTime = 0
    blackTime = 0
    while True:
        bot.i = 0
        t1 = time.time()
        _,move=bot.minimax(board,2,True)
        t2 = time.time()
        whiteTime += t2-t1
        board.push(move)
        print(move,bot.i,w.i,whiteTime)
        pgn+=str(move) + ' '

        black+=1
        bot.i = 0
        t1 = time.time()
        _, move = bot.minimax(board, 3, False)
        t2 = time.time()
        blackTime += t2-t1
        board.push(move)
        print(move, bot.i,w.i,blackTime)
        pgn += str(move) + ' '
        print(pgn)
