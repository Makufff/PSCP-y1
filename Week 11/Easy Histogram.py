"""Easy Histogram"""
def histogram(s: str):
    """Easy Histogram"""
    nubz = {chr(i): 0 for i in range(65, 91)}
    nubz.update({chr(i): 0 for i in range(97, 123)})
    for char in s:
        if char in nubz:
            nubz[char] += 1
    for char in range(97, 123):
        char_lower = chr(char)
        char_upper = chr(char - 32)
        if nubz[char_lower] > 0:
            print(f"{char_lower} = {nubz[char_lower]}")
        if nubz[char_upper] > 0:
            print(f"{char_upper} = {nubz[char_upper]}")
histogram(input().strip())
