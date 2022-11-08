#맞았습니다!
import sys
n = int(sys.stdin.readline())
energy = list(map(int, sys.stdin.readline().split()))
total = max(energy)
energy.remove(total)
for i in range(n-1):
    total = total + energy[i]/2
print(total)