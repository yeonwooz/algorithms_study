import sys
input = sys.stdin.readline 

n = int(input()) # 에너지 드링크의 수
a = list(map(int, input().split())) # 에너지드링크
print((sum(a)+max(a))/2)

# a.remove(sum) # 

# for i in range(n-1):
#     sum += a[i]/2
#     # if a[i] % 2 == 0:
#     #     sum += a[i]//2
#     # else:
#     #     sum += a[i]//2 + 0.5

# print(sum)

# if sum % 2 == 0:
#     print(int(sum))
# else:
#     print(sum)