"""PhoneNumber"""
def format_phone_number(phone_number, nation):
    """
    Format the phone number based on its length and nation type.

    Args:
        phone_number (str)
        nation (str)

    Returns:
        str
    """
    if len(phone_number) == 9:
        if nation == "Domestic":
            return f"{phone_number[0]} {phone_number[1:5]} {phone_number[5:]}"
        return f"+66 {phone_number[1:5]} {phone_number[5:]}"

    if nation == "Domestic":
        return f"{phone_number[:2]} {phone_number[2:6]} {phone_number[6:]}"
    return f"+66{phone_number[1]} {phone_number[2:6]} {phone_number[6:]}"

def main():
    """Main function to process input and format phone number."""
    phone_number = input()
    nation = input()
    formatted_number = format_phone_number(phone_number, nation)
    print(formatted_number)

if __name__ == "__main__":
    main()
