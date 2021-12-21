import bot
import chess
import time

board = chess.Board()
pgn = ''
t1 = time.time()

while True:
    bot.i = 0
    _,move=bot.minimax(board,4,True)
    board.push(move)
    print(move,bot.i)
    pgn+=str(move) + ' '

    bot.i = 0
    _, move = bot.minimax(board, 4, False)
    board.push(move)
    print(move, bot.i)
    pgn += str(move) + ' '
    print(pgn)
