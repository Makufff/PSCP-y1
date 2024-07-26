"HAHAHA"
def main(food_drink_cost):
    "HOKHOK"
    service_charge = food_drink_cost * 0.10
    service_charge = max(50, min(service_charge, 1000))
    subtotal = food_drink_cost + service_charge
    vat = subtotal * 0.07
    total = subtotal + vat
    return round(total, 2)
print(f"{main(int(input())):.2f}")
