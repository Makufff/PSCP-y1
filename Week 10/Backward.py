"""Backward"""
def reverse_input():
    """Collect input until NULL"""
    data = []
    while True:
        line = input()
        if line == "NULL":
            break
        data.append(line)
    print('\n'.join(reversed(data)))

reverse_input()
