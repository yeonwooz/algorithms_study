import sys
readl = sys.stdin.readline

size = int(readl().strip())

mat = []
for _ in range(size):
    mat.append(list(map(int, readl().split())))
ret = [0] * 3
def cut(mat, r, c, size):
    plag = mat[r][c]
    plag2 = 1
    row = 0
    col = 0
    for i in range(r, r + size//3):
        for j in range(c, c + size//3):
            if mat[i][j] != plag:
                plag2 = 0
                break
        else: continue
        break
    if plag2 == 1:
        ret[plag+1] += 1
    else:
        size = size // 3
        if size > 0:
            for y in range(3):
                for x in range(3):
                    cut(mat, r + y*size//3, c + x*size//3, size)
for k in range(3):
    for t in range(3):
        cut(mat, k*size//3, t*size//3, size)
print(*ret,sep="\n")