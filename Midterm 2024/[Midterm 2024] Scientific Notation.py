import re

def convert_to_scientific_notation(number):
    number = number.strip()
    
    # Check if the input is scientific notation
    sci_notation_match = re.match(r'^(-?\d*\.?\d+) x 10\^(-?\d+)$', number)
    
    if sci_notation_match:
        a, b = sci_notation_match.groups()
        a = float(a)
        b = int(b)
        # Convert to decimal format
        result = a * (10 ** b)
        # Format the result to preserve trailing zeros
        return "{:.6f}".format(result).rstrip('0').rstrip('.')
    
    else:
        # Split number into integer and decimal part
        if 'e' in number or 'E' in number:
            # Handle scientific notation with 'e'
            number = float(number)
        else:
            number = float(number)
        
        # Convert to scientific notation
        if number == 0:
            return "0"
        
        # Use Python's scientific notation formatting
        result = "{:.6e}".format(number)
        base, exponent = result.split('e')
        exponent = int(exponent)
        # Format the base to preserve trailing zeros
        base = "{:.6f}".format(float(base))
        return "{} x 10^{}".format(base.rstrip('0').rstrip('.'), exponent)

# Sample Test Cases
inputs = [
    "123000000",
    "1.23 x 10^8",
    "4590.000",
    "0.0000",
    "0.00135540",
    "9.011 x 10^-3"
]

for inp in inputs:
    print(f"Input: {inp} -> Output: {convert_to_scientific_notation(inp)}")
