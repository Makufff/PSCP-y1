"""olm"""
def forkey(txt):
    """forkey"""
    return int(txt[1]), int(txt[2]), int(txt[3])\
        , ord(txt[0][0])*-1, ord(txt[0][1])*-1, ord(txt[0][2])*-1
def olm(country):
    """olm"""
    list1 = []
    for _ in range(country):
        word = input().split()
        list1.append(word)
    list1.sort(key=forkey, reverse=True)
    sum_medal = []
    sequence = []
    for i in list1:
        sum_medal.append(str(int(i[1])+int(i[2])+int(i[3])))
    for i in range(1, len(list1)+1):
        num_sequence = i
        if i != 1:
            if list1[i-1][1:] == list1[i-2][1:]:
                num_sequence = sequence[-1]
        sequence.append(str(num_sequence))
    for i, (seq, country_data, total) in enumerate(zip(sequence, list1, sum_medal)):
        print(seq, end=" ")
        print(*country_data, end=" ")
        print(total)
olm(int(input()))
