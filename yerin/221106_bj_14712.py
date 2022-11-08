# 14712 넴모넴모
# 계산복잡도 : (N*M)2^(N*M) ㅋㅋㅋㅋㅋㅋㅋㅋ -> 시간초과

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0

def nemo_nemo(mat, l):
    global cnt
    for i in range (0, N-1):
        for j in range (0, M-1):
            if mat[i*M+j] == mat[i*M+j+1] == mat[(i+1)*M+j] == mat[(i+1)*M+j+1] == '1':
                return
    
    cnt = cnt + 1

def binary_format(string, n):
    dif = n - len(string)
    if dif != 0:
        return '0'*dif + string
    else: return string

x = N*M
for i in range (1 << N*M):
    mat = binary_format(format(i, 'b'), N*M)
    nemo_nemo(mat, i)

print(cnt)



# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(a, b):
#     q = deque([(a,b,0)])
#     matrix[a][b] = 1

#     while q:
#         x, y, d = q.popleft()
#         for i in range (4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<M and matrix[nx][ny] != 1:
#                 q.append(nx,ny,d+1)
#                 matrix[nx][ny] = 1

