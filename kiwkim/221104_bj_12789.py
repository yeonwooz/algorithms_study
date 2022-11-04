#도키도키 간식드리미

import sys
from collections import deque
readl = sys.stdin.readline

N = int(readl())
line = deque(map(int, readl().split()))
tmp = []
bunho = 1
while (line):
    if bunho == line[0]:
        bunho += 1
        line.popleft()
    elif tmp and tmp[-1] == bunho:
        bunho += 1
        tmp.pop()
    else:
        tmp.append(line.popleft())
while tmp:
    if tmp.pop() == bunho:
        bunho += 1
    else:
        break
if N+1 == (bunho):
    print("Nice")
else:
    print("Sad")
