"""Solar Beam"""
def find_hot(left, right):
    """Find the 'hot'"""
    hot = ""
    left, right = str(left), str(right)
    loop = -len(left)
    if loop == -2:
        loop = -3
    for i in range(-2, loop, -1):
        if left[i] == " ":
            break
        hot += left[i]
    hot = hot[::-1]
    if right.count(" ") == 1:
        hot += " " + right[1:]
    else:
        hot += " " + right[1:right.find(" ", 1)]
    return hot


def find_cool(left, right):
    """Find the 'cool'"""
    left, right = str(left), str(right)
    cool = ""
    cool2 = ""
    if left.count(" ") < right.count(" "):
        for i in range(-2, -len(right), -1):
            if right[i] == " ":
                break
            cool += right[i]
        cool = cool[::-1]
    elif left.count(" ") > right.count(" "):
        cool += left[1:left.find(" ", 1)]
    else:
        cool += left[1:left.find(" ", 1)] + " "
        for i in range(-2, -len(right), -1):
            if right[i] == " ":
                break
            cool2 += right[i]
        cool2 = cool2[::-1]
        cool += cool2
    return cool


def main_find_hot_and_cool():
    """Determine the 'hot' and 'cool'"""
    txt = input()
    hot = ""
    cool = ""
    num_spaces = txt.count(" ")
    txt = " " + txt + " "
    left = txt[:txt.find(" Sun ") + 1]
    right = txt[txt.find(" Sun ") + 4:]
    if num_spaces == 1:
        hot += txt.replace("Sun", "").replace(" ", "")
        cool += txt.replace("Sun", "").replace(" ", "")
    elif txt.startswith(" Sun "):
        hot += txt[5:txt.find(" ", 5)]
        for i in range(-2, -len(txt), -1):
            if txt[i] == " ":
                break
            cool += txt[i]
        cool = cool[::-1]
    elif txt.endswith(" nuS "):
        for i in range(-6, -len(txt), -1):
            if txt[i] == " ":
                break
            hot += txt[i]
        hot = hot[::-1]
        cool += txt[1:txt.find(" ", 1)]
    else:
        hot += find_hot(left, right)
        cool += find_cool(left, right)
    print(f"Hot: {hot}")
    print(f"Cool: {cool}")

if __name__ == "__main__":
    main_find_hot_and_cool()
