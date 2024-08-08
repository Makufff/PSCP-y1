"""Easy"""
def main(num):
    """Easy"""
    group = []
    for i in str(num):
        group.append(int(i))
    calc1 = sum(group)
    calc2 = int(str(group[-3])+str(group[-2])+str(group[-1])) *10
    calc3 = calc1 + calc2
    if len(str(calc3)) > 4:
        calc3 = str(calc3)
        print(calc3[-4]+calc3[-3]+calc3[-2]+calc3[-1])
    elif calc3 < 1000:
        print(calc3+1000)
    else:
        print(calc3)
main(str(input()))
