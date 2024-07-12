"""WeightStation"""
ave_w = float(input())
weight1 = float(input())
weight2 = float(input())
weight3 = float(input())
total_weight = ave_w * 4
weight4 = total_weight - (weight1 + weight2 + weight3)
if total_weight > 15000:
    print("Overweight")
else:
    half_average = ave_w / 2
    if (abs(weight1 - ave_w) > half_average or
        abs(weight2 - ave_w) > half_average or
        abs(weight3 - ave_w) > half_average or
        abs(weight4 - ave_w) > half_average):
        print("Unbalance")
    else:
        print(f"Pass {weight4:.2f}")
