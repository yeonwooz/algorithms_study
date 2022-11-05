import sys
sys.setrecursionlimit(int(1e9))
readl = sys.stdin.readline
r, c = map(int, readl().split())
result = 0
mat = [[0] * 26 for _ in range(26)]
def nemonemo(count):
    global result, r, c
    if (count == r * c):
        result += 1
        return
    row = count // c + 1
    col = count % c + 1
    nemonemo(count + 1)
    if((mat[row][col - 1] == 0 or mat[row - 1][col] == 0 or mat[row-1][col - 1] == 0)):
        mat[row][col] = 1
        nemonemo(count + 1)
        mat[row][col] = 0
nemonemo(0)
print(result)
# 
# 2 ^ (row * col) - 4 칸짜리 배치하고