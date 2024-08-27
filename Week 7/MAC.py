"""MACDONAL Address"""
def valid1(txt):
    """Check if the MAC address follows the VALID 1 format"""
    alphacheck = "ABCDEFabcdef"
    num = 2
    checkvalid1 = True
    checkvalid2 = True
    if len(txt) == 17:
        for i, char in enumerate(txt):
            if i == num:
                checkvalid2 = txt[i] == "-"
                num += 3
            elif not char.isdigit() and char not in alphacheck:
                checkvalid1 = False
        if checkvalid1 and checkvalid2:
            return "VALID 1"
        return "ERROR"
    return "ERROR"

def valid2(txt):
    """Check if the MAC address follows the VALID 2 format"""
    alphacheck = "ABCDEFabcdef"
    num = 2
    checkvalid1 = True
    checkvalid2 = True
    if len(txt) == 17:
        for i, char in enumerate(txt):
            if i == num:
                checkvalid2 = txt[i] == ":"
                num += 3
            elif not char.isdigit() and char not in alphacheck:
                checkvalid1 = False
        if checkvalid1 and checkvalid2:
            return "VALID 2"
        return "ERROR"
    return "ERROR"

def valid3(txt):
    """Check if the MAC address follows the VALID 3 format"""
    alphacheck = "ABCDEFabcdef"
    num = 4
    checkvalid1 = True
    checkvalid2 = True
    if len(txt) == 14:
        for i, char in enumerate(txt):
            if i == num:
                checkvalid2 = txt[i] == "."
                num += 5
            elif not char.isdigit() and char not in alphacheck:
                checkvalid1 = False
        if checkvalid1 and checkvalid2:
            return "VALID 3"
        return "ERROR"
    return "ERROR"

def macdonald(txt):
    """MAC address validity based on the format"""
    if txt.count("-") == 5:
        print(valid1(txt))
    elif txt.count(":") == 5:
        print(valid2(txt))
    elif txt.count(".") == 2:
        print(valid3(txt))
    else:
        print("ERROR")

macdonald(input())
