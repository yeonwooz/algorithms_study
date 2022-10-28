import sys
input = sys.stdin.readline


t = int(input())
for i in range(t):
    n = int(input())
    height = list(map(int, input().split()))
    height.sort()
    temp = [0]*(n+1)
    
    temp[0] = height[0]
    
    i = 0
    while height:
        if i%2 == 0:
            temp[n-i//2] = height[0]
            del height[0]
        else:
            temp[i//2+1] = height[0]
            del height[0]
        i = i+1
    
    diff = []
    for j in range(len(temp)-1):
        diff.append(abs(temp[j+1]-temp[j]))
    print(max(diff))
#################################################
#################################################
# import sys
# input = sys.stdin.readline

# t = int(input())
# for i in range(t):
#     n = int(input())
#     height = list(map(int, input().split()))
#     height.sort()
#     height.append(height[0])
#     diff = []
#     i=0
#     while i < len(height)-1:
#         diff.append(height[i])
#         i=i+2
    
        
    
    
    
    
    
    
