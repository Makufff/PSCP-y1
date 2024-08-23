"""ทำไรผิด? [Mock Midterm 2022] Meteorite"""
def meteorite( a:float , b:int , c:float , cnt:int=1) -> None :
    if a / b >= c :
        for _ in range(a//b):
            cnt += 1
    return cnt
print(meteorite(float(input()) , int(input()) , float(input()) , 1))