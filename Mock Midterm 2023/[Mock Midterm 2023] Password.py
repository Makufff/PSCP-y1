"""[Mock Midterm 2023] Password"""
from math import log2

def check_punctuation(txt, r_value):
    """Check for punctuation in the text and adjust the value."""
    punctuation_chars = '''~`!@#$%&^*()-_+={ }[\\]|/:;'"<>,.?'''
    if any(char in punctuation_chars for char in txt):
        r_value += 32
    return r_value

def password_strength():
    """Evaluate the strength of a given password."""
    txt = input().strip()
    r_value = 0

    if any(char.islower() for char in txt):
        r_value += 26
    if any(char.isupper() for char in txt):
        r_value += 26
    if any(char.isdigit() for char in txt):
        r_value += 10

    r_value = check_punctuation(txt, r_value)
    strength_score = int(log2(r_value ** len(txt)))

    if strength_score < 28:
        print(strength_score, "Very Weak", sep="\n")
    elif 28 <= strength_score <= 35:
        print(strength_score, "Weak", sep="\n")
    elif 36 <= strength_score <= 59:
        print(strength_score, "Reasonable", sep="\n")
    elif 60 <= strength_score <= 127:
        print(strength_score, "Strong", sep="\n")
    else:
        print(strength_score, "Very Strong", sep="\n")

if __name__ == "__main__":
    password_strength()
