import sys
readl = sys.stdin.readline
casenum = int(readl())

for i in range(casenum):
    namu = int(readl())
    trees = list(map(int, readl().split()))
    trees.sort()
    maxchai = 0
    for i in range(namu - 2):
        cha = trees[i+2] - trees[i]
        if cha > maxchai:
            maxchai = cha
    print(maxchai)