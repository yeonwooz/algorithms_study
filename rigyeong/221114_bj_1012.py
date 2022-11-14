import sys
from collections import deque
sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline())
for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    matrix = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    cnt = 0
    
    def dfs(x,y):
        delta = [[0,1], [1,0], [0,-1], [-1,0]]
        for d in delta:
            dx = x + d[0]
            dy = y + d[1]
            if (0 <= dx < m) and (0 <= dy < n):
                if matrix[dy][dx] == 1:
                    matrix[dy][dx] = -1
                    dfs(dx, dy)

    for i in range(m):
        for j in range(n):
            if matrix[j][i] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)