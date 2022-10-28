#2644 촌수계산
import sys

input = sys.stdin.readline

n = int(input())

p1, p2 = map(int, input().split())

m = int(input())
family = [ [] for _ in range (n+1) ]

for i in range (m):
    p, c = map(int, input().split())
    family[p].append(c)
    family[c].append(p)

visited = set()
cnt = 0

def dfs(u, d):
    global cnt 
    visited.add(u)

    if u == p2:
        cnt = d
        return 
    
    for i in range (len(family[u])):
        v = family[u][i]
        if v not in visited:
            dfs(v, d+1)

dfs(p1,0)
if cnt !=0: print(cnt)
else: print(-1)