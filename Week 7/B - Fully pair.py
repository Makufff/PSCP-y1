"""Pairing"""
def pair(txt):
    """Check if all characters"""
    checked_chars = ""
    ans = ""
    for i in txt:
        if i in checked_chars:
            continue
        num = txt.count(i)
        if not num % 2:
            checked_chars += i
        else:
            ans += i
            checked_chars += i
    if not ans:
        print("fully paired")
    else:
        print(ans)

if __name__ == "__main__":
    pair(input())
