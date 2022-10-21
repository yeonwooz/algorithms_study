# took 15 min
import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # k: 영식 랜선 개수, n: 필요한 랜선 개수 , k<=n
lan_list = [int(input()) for _ in range(k)] # lan_list: 가지고 있는 각 랜선의 길이

start = 1 # 1이상으로 잘라야 함
end = max(lan_list) # 가장 큰 값

# 이분탐색 시작
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0 # 만들 수 있는 랜선의 개수 
    for i in range(len(lan_list)):
        cnt += lan_list[i]//mid # mid로 잘라가면서 개수 세주기
    
    if cnt < n: 
        end = mid -1
    else:
        start = mid + 1
        result = mid

print(result)
