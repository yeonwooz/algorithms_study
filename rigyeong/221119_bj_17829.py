import sys
n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def rec(size, x, y):
    mid=size//2
    if size==2:
        answer=[matrix[x][y], matrix[x+1][y], matrix[x][y+1], matrix[x+1][y+1]]
        answer.sort()
        return answer[-2]
    lt=rec(mid, x, y)
    rt=rec(mid, x+mid, y)
    lb=rec(mid, x, y+mid)
    rb=rec(mid, x+mid, y+mid)
    answer=[lt, rt, lb, rb]
    answer.sort()
    return answer[-2]
print(rec(n, 0, 0))