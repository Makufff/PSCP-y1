"""Horizontal Histogram"""
def horizontal():
    """horizontal"""
    txt = input()
    freq = {char: txt.count(char) for char in set(txt)}
    sorted_chars = sorted(freq, key=lambda x: ord(x) - 66 if x.islower() else ord(x))

    for char in sorted_chars:
        count = freq[char]
        num_set = count // 5 - (not count % 5)
        remain = count - num_set * 5
        print(f"{char} : {'-----|' * num_set + '-' * remain}")

horizontal()
