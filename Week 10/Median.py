"""Median"""
def median():
    """Calu"""
    n = int(input())
    data = []
    for _ in range(n):
        number = float(input())
        data.append(number)
    data.sort()
    if n % 2 == 1:
        median_value = data[n // 2]
    else:
        median_value = (data[n // 2 - 1] + data[n // 2]) / 2
    print(f"{median_value:.3f}")
median()
