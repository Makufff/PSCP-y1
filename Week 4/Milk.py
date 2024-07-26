"""I don't Have Knowledge"""
def main(a, b, c, d):
    """Main function"""
    milk = cap = d // a
    if b:
        while cap >= b:
            new_milk = (cap // b) * c
            milk += new_milk
            cap = cap % b + new_milk
    print(milk)
main(*(int(input()) for _ in range(4)))
