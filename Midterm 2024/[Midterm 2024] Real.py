def read_segment():
    """Read segment values"""
    a = input().strip() == 'on'
    b = input().strip() == 'on'
    c = input().strip() == 'on'
    d = input().strip() == 'on'
    e = input().strip() == 'on'
    f = input().strip() == 'on'
    g = input().strip() == 'on'
    dp = input().strip() == 'on'
    return a, b, c, d, e, f, g, dp


def get_digit(a, b, c, d, e, f, g):
    """digit represented by the 7-segment display"""
    segments = (a, b, c, d, e, f, g)
    
    digit_patterns = {
        '8': (1, 1, 1, 1, 1, 1, 1),
        '0': (1, 1, 1, 1, 1, 1, 0),
        '3': (1, 1, 1, 1, 0, 0, 1),
        '9': (1, 1, 1, 1, 0, 1, 1),
        '7': (1, 1, 1, 0, 0, 0, 0),
        '2': (1, 1, 0, 1, 1, 0, 1),
        '5': (1, 0, 1, 1, 0, 1, 1),
        '6': (1, 0, 1, 1, 1, 1, 1),
        '1': (0, 1, 1, 0, 0, 0, 0),
        '4': (0, 1, 1, 0, 0, 1, 1),
    }

    for digit, pattern in digit_patterns.items():
        if segments == tuple(pattern):
            return digit

    return 'Error'


def format_result(digits, decimal_point_position):
    """specified decimal point position"""
    integer_part = digits[:decimal_point_position + 1] if decimal_point_position != -1 else digits
    fractional_part = digits[decimal_point_position + 1:] if decimal_point_position != -1 else ''

    result = integer_part + ('.' + fractional_part if fractional_part else '.00')

    # Ensure two decimal places
    if result.endswith('.'):
        result += '00'
    elif result.endswith('.0'):
        result += '0'

    return result


def main():
    """Main function"""
    digits = ''
    decimal_point_position = -1

    for i in range(3):
        a, b, c, d, e, f, g, dp = read_segment()
        digit = get_digit(a, b, c, d, e, f, g)
        
        if digit == 'Error':
            print('Error')
            return
            
        digits += digit
        
        if dp:
            decimal_point_position = i

    result = format_result(digits, decimal_point_position)
    print(result)

main()
