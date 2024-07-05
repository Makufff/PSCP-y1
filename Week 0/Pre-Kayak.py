"""Kayak eiei"""
n = int(input())
weight = sorted(map(int, input().split()))
remind, cnt = 0, 0
while cnt != n - 1:
    Calcu = [weight[i + 1] - weight[i] for i in range(len(weight) - 1)]
    min_idx = Calcu.index(min(Calcu))
    remind += weight[min_idx + 1] - weight[min_idx]
    weight.pop(min_idx + 1)
    weight.pop(min_idx)
    cnt += 1
print(remind)
