"""Bad Keyboard"""
def bad_keyword(txt):
    """ewewew"""
    new_txt = ""
    for i in txt:
        if i == "o":
            new_txt += "i"
        elif i == "i":
            new_txt += "o"
        elif i == "O":
            new_txt += "I"
        elif i == "I":
            new_txt += "O"
        else:
            new_txt += i
    print(new_txt)
bad_keyword(str(input()))
