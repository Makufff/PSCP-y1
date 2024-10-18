"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
import re
def find_vowel_words():
    """Find and sort words"""
    sentence = input().lower()
    words = re.findall(r'\b\w+\b', sentence)

    vowel_words = [word for word in words if len(re.findall(r'[aeiou]', word)) >= 2]

    if vowel_words:
        print('\n'.join(sorted(vowel_words)))
    else:
        print("Nope")

find_vowel_words()
