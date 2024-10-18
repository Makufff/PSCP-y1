"""factor"""
def find_factors(n, divisor=2, factors=None):
    """Resursion find factors"""
    if factors is None:
        factors = {}
    if n == 1:
        return factors  
    if n % divisor == 0:
        factors[divisor] = factors.get(divisor, 0) + 1
        return find_factors(n // divisor, divisor, factors)
    return find_factors(n, divisor + 1, factors)
def format_output(factors):
    """format ouput string"""
    return " x ".join([f"{p}" if c == 1 else f"{p}**{c}" for p, c in sorted(factors.items())])
def main(n):
    """main function"""
    for _ in range(n):
        number = int(input())
        print(format_output(find_factors(number)))
main(int(input()))
