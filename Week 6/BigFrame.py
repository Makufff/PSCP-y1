"""BigFrame"""
def main():
    """Main function"""
    txt1 = input().rstrip()
    txt2 = input().rstrip()
    txt3 = input().rstrip()
    txt4 = input().rstrip()
    txt5 = input().rstrip()
    line = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    print("**" + "*" * line + "**")
    print("* " + txt1 + " " * (line - len(txt1)) + " *")
    print("* " + txt2 + " " * (line - len(txt2)) + " *")
    print("* " + txt3 + " " * (line - len(txt3)) + " *")
    print("* " + txt4 + " " * (line - len(txt4)) + " *")
    print("* " + txt5 + " " * (line - len(txt5)) + " *")
    print("**" + "*" * line + "**")
main()
