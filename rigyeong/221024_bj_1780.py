import sys
n = int(sys.stdin.readline())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

minus, zero, one = 0, 0, 0
def divide(x,y,n):
    global minus, zero, one
    color = paper[x][y]
    if n == 1:
        if color == -1:
            minus += 1
        elif color == 0:
            zero += 1
        else:
            one += 1
        return 
    else:
        cnt = 0
        for i in range(x,x+n):
            for j in range(y,y+n):
                if color == paper[i][j]:
                    cnt += 1
                else:
                    break

        if cnt != n**2:    #균일하지 않을 때
            divide(x, y, n//3) 
            divide(x, y+(n//3), n//3)
            divide(x, y+(2*n//3), n//3)
            divide(x+(n//3), y, n//3)
            divide(x+(n//3), y+n//3, n//3)
            divide(x+(n//3), y+(2*n//3), n//3)
            divide(x+(2*n//3), y, n//3)
            divide(x+(2*n//3), y+(n//3), n//3)
            divide(x+(2*n//3), y+(2*n//3), n//3)
                        
        else:
            if color == -1:
                minus += 1
            elif color == 0:
                zero += 1
            else:
                one += 1
divide(0,0,n)
print(minus)
print(zero)
print(one)