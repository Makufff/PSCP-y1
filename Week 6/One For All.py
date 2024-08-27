"""One For All"""
def main():
    """Main function"""
    cnt = int(input())
    exp = 0
    value = ""
    for _ in range(cnt):
        txt = input()
        exp += 1
        if exp == cnt:
            value += (txt + f"_{cnt}")
        elif not exp % 2:
            value += (txt + "-" * exp)
        else:
            value += (txt + "*" * exp)
    print(value)
main()
