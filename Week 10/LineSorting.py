"""LineSorting"""
def sort_lines_by_length():
    """Sort"""
    n = int(input())
    lines = []
    for _ in range(n):
        line = input()
        lines.append(line)
    sorted_lines = sorted(lines, key=len)
    for line in sorted_lines:
        print(line)
sort_lines_by_length()
