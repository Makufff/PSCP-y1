"""[Mock Midterm 2022] Heron of Alexandria"""
def cal_heron(a:float , b:float , c:float) -> float :
    """Cal Heron function"""
    return (((a+b+c)/2)*((((a+b+c)/2))-a)*((((a+b+c)/2))-b)*((((a+b+c)/2))-c))**0.5
print(f"{cal_heron(float(input()) , float(input()) , float(input())):.3f}")
