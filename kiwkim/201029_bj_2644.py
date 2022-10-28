# 백준 2644 촌수계산

import sys
readl = sys.stdin.readline
putnum = int(readl())
target1, target2 = map(int, readl().split())
mat = [[0] * (putnum + 1) for _ in range(putnum + 1)]
casenum = int(readl())
for _ in range(casenum):
    i, j = map(int, readl().split())
    mat[i][j] = 1
    mat[j][i] = 1
visit = [0] * (putnum + 1)
ret = 0
def dfs(frm, to, i):
    global ret
    visit[frm] = 1
    if frm == to:
        ret = i
    for next in range(1, putnum+1):
        if mat[frm][next] == 1 and visit[next] == 0:
            dfs(next, to, i + 1)
dfs(target1, target2, 0)
if ret == 0:
    ret = -1
print(ret)