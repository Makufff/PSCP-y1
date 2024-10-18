"""Classify"""
def classify():
    """classify"""
    lst1, lst2 = [], []
    while True:
        data = input()[0:4]
        if data == "END":
            break
        lst1.append(data)
    lst1.sort()
    for i in lst1:
        if (i[0:2]+" "+str(int(i[2:]))+" "+str(lst1.count(i))) not in lst2:
            lst2.append(i[0:2]+" "+str(int(i[2:]))+" "+str(lst1.count(i)))
    if len(lst2) > 1:
        for index, word in enumerate(lst2):
            if index > 0 and word[0:2] == lst2[index-1][0:2]:
                print("--" + word[2:])
            else:
                print(word)
    else:
        print(*lst2)

classify()
