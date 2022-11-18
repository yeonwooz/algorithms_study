import sys
from collections import deque
readl = sys.stdin.readline

T = int(readl())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        prev_y, prev_x = q.popleft()
        for i in range(4):
            next_x = prev_x + dx[i]
            next_y = prev_y + dy[i]
            if 0 <= next_x < col and 0 <= next_y < row:
                if mat[next_y][next_x] == 1:
                    q.append((next_y, next_x))
                    mat[next_y][next_x] = 0
for t in range(T):
    cnt = 0
    col, row, K = map(int, readl().split())
    mat = [[0] * col for _ in range(row)]
    for k in range(K):
        x, y = map(int, readl().split())
        mat[y][x] = 1
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                cnt += 1
                mat[i][j] = 0
                bfs(i, j)

    print(cnt)


