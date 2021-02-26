# https://www.hackerrank.com/challenges/saveprincess/problem

def displayPathtoPrincess(n,grid):
    m_x, m_y = 0, 0
    p_x, p_y = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p_x, p_y = j, i
            if grid[i][j] == 'm':
                m_x, m_y = j, i
                
    for _ in range(min(m_x, p_x), max(m_x, p_x)):
        print('RIGHT' if m_x < p_x else 'LEFT')
    for _ in range(min(m_y, p_y), max(m_y, p_y)):
        print('DOWN' if m_y < p_y else 'UP')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)