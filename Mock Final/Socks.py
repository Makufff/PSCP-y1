"""Socks"""
from collections import Counter

def find_pair_socks(socks):
    """find Pair Socks"""
    sock_count = Counter(socks)
    paired_socks = []
    for sock, count in sorted(sock_count.items()):
        pairs = count // 2
        if pairs > 0:
            paired_socks.extend([sock + sock] * pairs)
    result = " ".join(paired_socks) if paired_socks else "None"
    total_pairs = len(paired_socks)
    return result, total_pairs
input_socks = input().strip()
sorted_socks, pair_count = find_pair_socks(input_socks)
print(sorted_socks)
print(pair_count)
