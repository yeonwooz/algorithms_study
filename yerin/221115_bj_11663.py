# 11663 선분 위의 점
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

points = list(map(int, input().split()))
points.sort()

def bs_min(a):  
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if points[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end

def bs_max(b):   
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if b < points[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range (M):
    l1, l2 = map(int, input().split())
    
    print(bs_max(l2)-bs_min(l1))


