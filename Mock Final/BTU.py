"""BTU"""
def get_btu_condition(area):
    """function btu condition"""
    ans = 0
    if area <= 150: ans = 5000
    elif area <= 250: ans = 6000
    elif area <= 300: ans = 7000
    elif area <= 350: ans = 8000
    elif area <= 400: ans = 9000
    elif area <= 450: ans = 10000
    elif area <= 550: ans = 12000
    elif area <= 700: ans = 14000
    elif area <= 1000: ans = 18000
    elif area <= 1200: ans = 21000
    elif area <= 1400: ans = 23000
    elif area <= 1500: ans = 24000
    elif area <= 2000: ans = 30000
    else: ans = 34000
    return ans
def main(area:int,height:int,people:int,room_type:str,sun_exposure:str):
    """main function"""
    btu = get_btu_condition(area)
    btu += max(0, height - 8) * 1000
    btu += max(0, people - 2) * 600
    btu += 4000 if room_type.lower() == "kitchen" else 0
    if sun_exposure.lower() == "facing the sun":
        btu = int(btu * 1.1)
    elif sun_exposure.lower() == "shaded":
        btu = int(btu * 0.9)
    return btu
print(main(int(input()),int(input()),int(input()),input(),input()))
