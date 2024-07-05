n = int(input())
weights = list(map(int, input().split()))
weights.sort()

def calculate_sum_diff(weights):
    return sum(weights[k+1] - weights[k] for k in range(0, len(weights)-1, 2))

min_diff = float('inf')

for i in range(2*n):
    for j in range(i+1, 2*n):
        if j > i + 1:  # Ensure j is after i+1 to maintain the sequence
            new_weights = weights[:i] + weights[i+1:j] + weights[j+1:]
            diff = calculate_sum_diff(new_weights)
            min_diff = min(min_diff, diff)

print(min_diff)
