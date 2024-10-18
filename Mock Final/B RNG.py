import json
def find_max_sum(lst, n, s):
    if n >= len(lst):
        return sum(lst) * (n // len(lst)) + sum(lst[:n % len(lst)])
    total = sum(lst[:n])
    max_sum = total
    for i in range(len(lst)):
        total = total - lst[i] + lst[(i + n) % len(lst)]
        if i % s == 0:
            max_sum = max(max_sum, total)
    return max_sum
lst = json.loads(input())
n, s = int(input()) , int(input())
result = find_max_sum(lst, n, s)
print(result)