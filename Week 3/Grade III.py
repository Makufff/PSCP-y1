"""Hello"""
def cal_grade(score):
    """Calculate"""
    value = 0.0
    if 95 <= score <= 100:
        value = 4.0
    elif 90 <= score < 95:
        value = 3.5
    elif 85 <= score < 90:
        value = 3.0
    elif 80 <= score < 85:
        value = 2.5
    elif 75 <= score < 80:
        value = 2.0
    elif 70 <= score < 75:
        value = 1.5
    elif 65 <= score < 70:
        value = 1.0
    elif 60 <= score < 65:
        value = 0.5
    elif 0 < score < 60:
        value = 0.0
    return value
def main(): 
    """Main"""
    count = int(input())
    overall = 0
    for _ in range(count):
        overall += cal_grade(float(input()))
    print(f"{((int((overall/count)*100))/100):.2f}")
main()
