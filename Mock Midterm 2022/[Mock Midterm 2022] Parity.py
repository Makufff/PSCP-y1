
"""incomplete s[Mock Midterm 2022] Parity"""
def add_even_odd_bit(bit : str , rule:str ) -> str :
    """Add last bit"""
    if rule == "Even":
        bit += "0" 
    else :
        bit += "1"
    return bit
print(add_even_odd_bit(input() , input()))
