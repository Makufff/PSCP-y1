"""
[Not recommended] Diamond II
"""
def find_max_diamond_value(m:int, n:int, diamond_values:list) -> int:
    """
    How to solution :
    1. create 3d of list use to memo
    2. Init first row
    3. Subsequent row
    4. Calu maximum value considering
    5. Update the current cell
    6. Swap row
    Return the maximum value
    """
    prev_row = [0] * n
    curr_row = [0] * n

    for j in range(n):
        prev_row[j] = diamond_values[0][j]

    for i in range(1, m):
        for j in range(n):
            max_prev = prev_row[j]
            if j > 0:
                max_prev = max(max_prev, prev_row[j - 1])
            if j < n - 1:
                max_prev = max(max_prev, prev_row[j + 1])

            curr_row[j] = max_prev + diamond_values[i][j]

        prev_row, curr_row = curr_row, prev_row

    return max(prev_row)

def main(m:int , n:int) -> int:
    """Main Function"""
    diamond_values = [list(map(int, input().split())) for _ in range(m)]
    result = find_max_diamond_value(m, n, diamond_values)
    print(result)

main(int(input()),int(input()))
