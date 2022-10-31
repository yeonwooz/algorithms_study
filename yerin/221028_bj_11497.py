# 11497 통나무 건너뛰기
import sys
import heapq
input = sys.stdin.readline


T = int(input())

for i in range (T):
    N = int(input())
    woods = list(map(int, input().split()))
    heapq.heapify(woods)
    opt_list = [0] * N
    if N % 2 == 0: k = N//2
    else : k = N//2+1

    for j in range (k):
        opt_list[j] = heapq.heappop(woods)
        if j!=N-1-j: opt_list[N-1-j] = heapq.heappop(woods)
    
    d = 0
    for x in range (N):
        d = max(d, abs(opt_list[x-1]-opt_list[x]))

    print(d)


# 최적해 - 인덱스 2 차이나는 애들끼리 옆에 붙어있게 됨
# for i in range(T):
#     N = int(input())
#     woods = list(map(int, input().split()))
#     woods.sort()
    
#     d = 0
#     for j in range(N-2):
#         d = max(d, woods[j+2]-woods[j])
#     print(d)
