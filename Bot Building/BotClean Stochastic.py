# https://www.hackerrank.com/challenges/botcleanr/problem

def nextMove(posr, posc, board):
    d_x, d_y = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                d_x, d_y = j, i
    next_move = ''
    if posc < d_x:
        next_move = 'RIGHT'
    elif posc > d_x:
        next_move = 'LEFT'
    else:
        if posr > d_y:
            next_move = 'UP'
        elif posr < d_y:
            next_move = 'DOWN'
        else:
            next_move = 'CLEAN'
    print(next_move)
    

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)