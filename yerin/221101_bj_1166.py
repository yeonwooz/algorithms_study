# 1166 선물
# 오후 11시 26분
N, L, W, H = map(int, input().split())
start, end = 0, int((L * W * H) ** (1/3)) + 1  # 세제곱근 + 1까지

for _ in range(10000): # 1 ≤ L, W, H ≤ 1,000,000,000
    mid = (start + end) / 2
    cnt = (L // mid) * (W // mid) * (H // mid)
    if cnt >= N:
        start = mid
    else:
        end = mid

print("%.10f" %(end))
