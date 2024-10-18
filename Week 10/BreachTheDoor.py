"""Regx is all u need"""
import re
def filter_long_words():
    """Extract words longer than 6 characters from a given sentence."""
    sentence = input()
    words = re.findall(r'\b[a-zA-Z]{7,}\b', sentence)
    print(' '.join(words))
filter_long_words()
