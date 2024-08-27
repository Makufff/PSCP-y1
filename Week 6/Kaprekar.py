"""5555555เลิกเป็นผู้ดี"""
def sor_t(num1, num2, num3, num4):
    """sor_t number from highest to lowest"""
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num1 < num4:
        num1, num4 = num4, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num2 < num4:
        num2, num4 = num4, num2
    if num3 < num4:
        num3, num4 = num4, num3
    return (str(num1)+str(num2)+str(num3)+str(num4), str(num4)+str(num3)+str(num2)+str(num1))
def kaprekars(text):
    """find gow many time thats 4 number turn into 6174"""
    count = 0
    while text != "6174":
        num1 = int(text)//1000
        num2 = (int(text)%1000)//100
        num3 = ((int(text)%1000)%100)//10
        num4 = ((int(text)%1000)%100)%10
        high, low = sor_t(num1, num2, num3, num4)
        text = int(high)-int(low)
        text = str(text)
        count += 1
    print(count)
kaprekars(input())
