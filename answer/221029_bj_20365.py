#블로그2 홍리경
#https://www.acmicpc.net/problem/20365

import sys
readl = sys.stdin.readline
putnum = int(readl())
putstr = readl().strip()
prev = putstr[0]
cnt= 1
for char in putstr:
    if prev != char:
        if char != putstr[0]:
            cnt += 1
            prev = char
        else:
            prev = char
print(cnt)