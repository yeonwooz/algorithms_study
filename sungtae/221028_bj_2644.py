import sys
input = sys.stdin.readline

n = int(input()) # n: 전체 사람의 수
p1, p2 = map(int, input().split()) # 촌수를 계산하는 사람
m = int(input()) # 부모 자식들 간의 관계의 개수
parent_relation = [[] for _ in range(n+1)] # 그래프

for i in range(m):
    x, y = map(int, input().split())
    parent_relation[x].append(y) # x->부모 y->자식
    parent_relation[y].append(x)

visited = set()
cnt = 0

def dfs(p, distance): # dfs
    global cnt
    visited.add(p)
    if p == p2:
        cnt = distance
        return
    
    for i in range(len(parent_relation[p])):
        v = parent_relation[p][i]
        if v not in visited:
            dfs(v, distance+1)

dfs(p1, 0)
if cnt:
    print(cnt)
else:
    print(-1)
        
    
    
