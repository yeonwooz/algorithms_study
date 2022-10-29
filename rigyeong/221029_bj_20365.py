import sys
n = int(sys.stdin.readline())
problems = sys.stdin.readline().strip()

colors = {'B':0, 'R':0}
colors[problems[0]] += 1 #처음 색 칠하기
for i in range(1, n):
    if problems[i] != problems[i-1]:
        colors[problems[i]] += 1
min_cnt = min(colors['B'], colors['R']) +1
print(min_cnt)