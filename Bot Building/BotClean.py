# https://www.hackerrank.com/challenges/botclean/problem

import math

def find_closest(bot, dirts):
    if len(dirts) > 0:
        closest = (10,10)
        distance = 10
        for dirt in dirts:
            d = math.sqrt((dirt[0] - bot[0]) ** 2 + (dirt[1] - bot[1]) ** 2)
            if d <= distance:
                closest = dirt
                distance = d
        return closest

def next_move(posr, posc, board):
    dirts = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd': 
                dirts.append((j, i))

    d_x, d_y = find_closest((posc, posr), dirts)

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
    next_move(pos[0], pos[1], board)