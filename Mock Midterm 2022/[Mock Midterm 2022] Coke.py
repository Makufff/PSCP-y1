"""[Mock Midterm 2022] Coke"""
def coke( a:int , b:int , c:int ,d:int) -> int :
    """
    เดิมราคาขวดละ a บาท
    หากนำมาฝาขวดจำนวน b ฝา มาแลก จะซื้อขวดใหม่ได้ในราคา c บาท
    หากต้องการ Coke จำนวน d ขวด จะต้องจ่ายเงินน้อยที่สุดเท่าไร
    50 / (3 * 1) = 16 R 2
    """
    total = 0
    cnt_free = 1
    while d != 0 :
        d -= 1
        if not cnt_free % b :
            total += c
        else :
            total += a
        cnt_free += 1
    return total
print(coke(int(input()) , int(input()) , int(input()) , int(input())))        
