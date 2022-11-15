import sys
n, m = map(int, sys.stdin.readline().split())
dots = list(map(int, sys.stdin.readline().split()))
dots.sort()

def dot_min(a): # 선분 중 가장 작은 점의 index 구하기
    start = 0
    end = n- 1 
    while start <= end:
        mid = (start + end) // 2  
        if dots[mid] < a:  
            start = mid + 1 
        else:
            end = mid -1  
    return end + 1  

def dot_max(b): # 선분 중 가장 큰 점의 index 구하기
    start = 0
    end = n- 1 
    while start <= end: 
        mid = (start + end) // 2
        if dots[mid] > b:
            end = mid - 1 
        else:
            start = mid + 1 
    return end      
    
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dot_max(e) - dot_min(s) + 1)