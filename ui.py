import bot
import chess
import chess.svg
import time

board = chess.Board()
def show():
    with open('gameState.svg', mode='w') as gameState:
        gameState.write(chess.svg.board(board, size=600, lastmove=move, orientation=chess.BLACK))
        gameState.close()

pgns = []
pgn = ''

whiteTime = 0
blackTime = 0

while True:
    bot.i = 0
    t1 = time.time()
    _,move=bot.minimax(board,2,True)
    t2 = time.time()
    whiteTime += t2-t1
    board.push(move)
    print(move,whiteTime)
    pgn+=str(move) + ' '
    show()
    bot.i = 0
    t1 = time.time()
    print('your turn')
    while True:
        move = input("your move is:")
        print(move)
        try:
            move = chess.Move.from_uci(move)
            board.push(move)
            break
        except Exception:
            print("invalid try again")

    t2 = time.time()
    blackTime += t2-t1
    print(move,blackTime)
    pgn += str(move) + ' '
    print(pgn)
    show()
