"""Filter"""
import json

def filter_fn():
    """filter"""
    txt, score, check_nope = input(), float(input()), True
    get_dict = json.loads(txt)
    get_list = list(get_dict.items())
    get_list.sort(key=lambda x: int(x[0]))
    for i in get_list:
        if float(i[1]) >= score:
            check_nope = False
            print(f"{i[0]}\t{float(i[1]):.2f}")
    if check_nope:
        print("Nope")

filter_fn()
