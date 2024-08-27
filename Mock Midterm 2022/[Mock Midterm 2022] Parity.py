
"""incomplete s[Mock Midterm 2022] Parity"""
def main(binary:str , even_or_odd:str):
    """Main function"""
    string_builder = ""
    point_increment = 0

    for text in binary:
        if text == "1":
            point_increment += 1
        string_builder += text

    if even_or_odd == "even":
        string_builder += "0" if not point_increment % 2 else "1"
    elif even_or_odd == "odd":
        string_builder += "1" if not point_increment % 2 else "0"

    print(string_builder)

if __name__ == "__main__":
    main(input() , input().lower())
