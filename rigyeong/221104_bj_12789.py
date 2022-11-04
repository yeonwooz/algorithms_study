import sys
from collections import deque
n = int(sys.stdin.readline())
seq = deque(map(int, sys.stdin.readline().split()))
q = deque()
cnt = 1

while seq:
    if seq[0] != cnt:
        s = seq.popleft()
        q.append(s)
    else:
        cnt += 1
        seq.popleft()
    while q:
        if q and q[-1] == cnt:
            q.pop()
            cnt += 1
        else: break
        
if len(q) == 0: print("Nice")

while q:
    if q[-1] != cnt:
        print("Sad")
        break
    else:
        cnt += 1
        q.pop()