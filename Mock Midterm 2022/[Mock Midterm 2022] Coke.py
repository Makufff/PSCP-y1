"""[Mock Midterm 2022] Coke"""
def coke(a: int, b: int, c: int, d: int) -> int:
    """
    เดิมราคาขวดละ a บาท
    หากนำมาฝาขวดจำนวน b ฝา มาแลก จะซื้อขวดใหม่ได้ในราคา c บาท
    หากต้องการ Coke จำนวน d ขวด จะต้องจ่ายเงินน้อยที่สุดเท่าไร
    50 / (3 * 1) = 16 R 2
    """
    total = 0

    if not b and d:
        total += a * d
    elif b and c and d:
        if d % b:
            total += (a * (d - (d // b))) + (c * (d // b))
        else:
            total += (a * (d - ((d // b) - 1))) + (c * ((d // b) - 1))
    elif b and not c and d:
        if d % b:
            total += (a * (d - (d // b))) + (c * (d // b))
        else:
            total += (a * (d - ((d // b) - 1))) + (c * ((d // b) - 1))
    elif not d:
        total = 0

    return total

print(coke(int(input()), int(input()), int(input()), int(input())))
