import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    tree = list(map(int, sys.stdin.readline().split()))
    tree.sort()
    ans = 0
    for idx in range(2, N):
        ans = max(ans, abs(tree[idx] - tree[idx-2]))
    print(ans)