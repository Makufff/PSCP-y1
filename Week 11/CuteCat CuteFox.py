"""CuteCat CuteFox"""
import json
def func_sort(txt):
    """func_sort"""
    return ord(txt[1][0]), int(txt[1][3:])
def count_catfox(group_list):
    """count_catfox"""
    cat = 0
    fox = 0
    for i in group_list:
        if i[1][0:3] == 'Cat':
            cat += 1
        elif i[1][0:3] == 'Fox':
            fox += 1
    return cat, fox
def cnf(num):
    """cnf"""
    group_dict = {}
    cat_chk, name_chk1 = False, False
    fox_chk, name_chk2 = False, False
    for i in range(num):
        txt = input().split(" : ")
        first = '{"'+txt[0][2:len(txt[0])-1]+'"'
        last = '"'+txt[1][1:len(txt[1])-2]+'"}'
        new_txt = first+" : "+last
        group_dict.update(json.loads(new_txt))
    group_list = list(group_dict.items())
    for i in group_list:
        if i[0] == 'Garfield':
            name_chk1 = True
        if i[0] == 'Fubuki':
            name_chk2 = True
    for i in group_list:
        if i[1] == 'Cat01':
            cat_chk = True
        if i[1] == 'Fox01':
            fox_chk = True
    if not cat_chk and not name_chk1:
        group_list.append(('Garfield', 'Cat01'))
    if not fox_chk and not name_chk2:
        group_list.append(('Fubuki', 'Fox01'))
    group_list.sort(key=func_sort)
    num_cat, num_fox = count_catfox(group_list)
    print(f"Cat : {num_cat}")
    print(f"Fox : {num_fox}")
    for i in group_list:
        print(i[0]+" : "+i[1])
cnf(int(input()))
