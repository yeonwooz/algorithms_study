import sys
from collections import deque
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
family = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    family[child].append(parent)
    family[parent].append(child)

dp = [0] * (n+1)
visited = []
def bfs():
    global a, b, visited, family
    cnt =0
    q = deque()
    q.append(a)
    visited.append(a)
    while q:
        p = q.popleft()
        for parent in family[p]:
            if parent not in visited:
                visited.append(parent)
                dp[parent] = dp[p] + 1
                if b != parent:
                    q.append(parent)
                else: break
    return
bfs()
if dp[b] == 0:
    print(-1)
else:
    print(dp[b])