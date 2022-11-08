# 20115 에너지 드링크
import sys
input = sys.stdin.readline

N = int(input())

drinks = list(map(int, input().split()))
max_drink = max(drinks)
drinks.remove(max_drink)

for i in range (N-1):
    max_drink = max_drink + drinks[i]/2

print(max_drink)


# [개빠른 풀이]  
# n = int(sys.stdin.readline())
# energy = list(map(int, sys.stdin.readline().split()))
# print((sum(energy)+max(energy))/2)


# [나의 원래 풀이] - min heap 사용
# 결론: 힙을 쓸 필요가 없다
# N = int(input())

# drinks = list(map(float, input().split()))
# max_drink = max(drinks)
# drinks.remove(max_drink)
# heapq.heapify(drinks)

# for i in range (N-1):
#     s_drink = heapq.heappop(drinks)
#     max_drink = max_drink + s_drink/2

# print(max_drink)
    


