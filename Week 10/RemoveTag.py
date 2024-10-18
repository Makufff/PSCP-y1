"""RemoveTag"""
def removetag():
    """RemoveTag"""
    txt = input()
    new_txt = ""
    skip = False
    for i, char in enumerate(txt):
        if char == "<":
            skip = True
        elif char == ">":
            skip = False
        elif not skip:
            if char != " ":
                new_txt += char
                if i < len(txt) - 1 and txt[i + 1] == "<":
                    new_txt += " "
            elif new_txt and new_txt[-1] != " ":
                new_txt += " "
    print(new_txt.split())
removetag()
