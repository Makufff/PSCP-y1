"""Vote"""
total_score = float(input())
max_score = float(input())
if max_score - max(0, total_score - 2 * max_score) > 2:
    print("Surprising")
else:
    print("Not surprising")
