# https://www.hackerrank.com/challenges/saveprincess2/problem

def nextMove(n,r,c,grid):
    p_x, p_y = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p_x, p_y = j, i
    next_move = ''
    if c < p_x:
        next_move = 'RIGHT'
    elif c > p_x:
        next_move = 'LEFT'
    else:
        if r > p_y:
            next_move = 'UP'
        else:
            next_move = 'DOWN'
    return next_move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))