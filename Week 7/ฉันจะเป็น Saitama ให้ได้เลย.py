"""ฉันจะเป็น Saitama ให้ได้เลย"""
from math import ceil
def main(v,s,l,r) :
    """One Punch"""
    cv = int(input())
    cs = int(input())
    cr = int(input())
    cl = int(input())

    v_cv = ceil(v / cv)
    s_cs = ceil(s / cs)
    l_cl = ceil(l / cl)
    r_cr = ceil(r / cr)

    if v_cv < s_cs :
        v_cv,s_cs = s_cs,v_cv
    if v_cv < l_cl :
        v_cv,l_cl = l_cl,v_cv
    if v_cv < r_cr :
        v_cv,r_cr = r_cr,v_cv

    return v_cv

print(main(int(input()),int(input()),int(input()),int(input())))
