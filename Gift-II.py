"""Gift-II"""
weights = [int(input()) for _ in range(8)]
for weight in weights:
    if not weight % 2:
        print(weight)
        break
