"""Over Engineer"""
def main(max_height, stairs):
    """main"""
    dp = [2e9] * (len(stairs) + 1)
    dp[0] = 0
    for i in range(1, len(stairs) + 1):
        height = 0
        for j in range(i - 1, -1, -1):
            height += stairs[j]
            if height > max_height:
                break
            dp[i] = min(dp[i], dp[j] + 1)
    return dp[len(stairs)] if dp[len(stairs)] != 2e9 else "NO"
result = main(int(input()), [int(input()) for _ in range(int(input()))])
print(result)
