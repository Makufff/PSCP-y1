"""Niwarn World"""
from math import log2, sin, radians, sqrt

def find_x(n):
    """Find x value"""
    return 2 + (log2(n**2) / (2 * n * log2(n)))

def find_y(n, s):
    """Find y value"""
    return (sin(radians(30)) + sqrt(2 * s)) / (find_x(n) + 3)

def find_z(k):
    """Find z value"""
    return (find_y(k, k) ** 2) + (8456 * (find_x(k) ** 4) / (24 * k))

def sol(n, s, k):
    """Main function"""
    print(f"X: {find_x(n):.1f}, Y: {find_y(n, s):.1f}, Z: {find_z(k):.1f}")

if __name__ == "__main__":
    sol(float(input()), float(input()), float(input()))
