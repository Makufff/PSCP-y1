"""BTSMRT"""
def is_free_entry(day, age, height):
    """Determine if entry is free based on day, age, and height."""
    if age < 14 and height < 90:
        return True

    if day == "Children Day" and age < 14 and height <= 140:
        return True

    if day == "Senior Day" and age >= 60:
        return True

    return False

def main():
    """Main function to process input and determine entry status."""
    day = input()
    age = float(input())
    height = float(input())

    if is_free_entry(day, age, height):
        print("FREE")
    else:
        print("PAY")

if __name__ == "__main__":
    main()
