"""Halloo"""
def Hallooo_word(word):
    """Haloon"""
    vowels = 'aeiou'
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in vowels:
            return word[:i + 1] + word[i] * 3 + word[i + 1:]
    return word
print(Hallooo_word(input()))
