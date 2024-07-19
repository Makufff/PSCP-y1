"""I Love Drawing"""
n = int(input())
for i in range(1, 2*n):
    row = []
    for j in range(1, 2*n):
        value = min(i, j, 2*n-i, 2*n-j, n)
        row.append(f'{value:02d}')
    print(' '.join(row))
