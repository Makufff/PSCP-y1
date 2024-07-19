"""I Love Drawing"""
def main():
    """Main"""
    number = int(input())
    for i in range(-number + 1, number):
        for j in range(-number + 1, number):
            print(f"{number - abs(abs(i) - abs(j)):02d}", end=" ")
        print()
main()
