"""ติด TimeOut"""
n = int(input())
weights = list(map(int, input().split()))
weights.sort()
min_diff = float('inf')
for i in range(2*n):
    for j in range(i+1, 2*n):
        new_weights = weights[:i] + weights[i+1:j] + weights[j+1:]
        diff = sum(new_weights[k+1] - new_weights[k] for k in range(0, 2*n-2, 2))
        min_diff = min(min_diff, diff)
print(min_diff)
