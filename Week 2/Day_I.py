"""Day"""
year = int(input())
if not year % 4:
    if not year % 100:
        if not year % 400:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")
