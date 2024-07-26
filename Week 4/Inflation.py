"""Delete Tammai"""
def main():
    """Delete Tammai Waku Waku"""
    cost = int(float(input()) * 100)
    years = int(input())
    percent = 381
    for _ in range(years):
        cost += (cost * percent) // 10000
    print(f"{cost // 100}.{cost % 100:02d}")
main()
