"""longer"""
from math import pi

def compare_perimeters(radius: float, length1: float, length2: float) -> None:
    """
    Compare the perimeter of a circle with a rectangle and print the result.
    """
    circle_perimeter = 2 * pi * radius
    rectangle_perimeter = 2 * (length1 + length2)
    if circle_perimeter > rectangle_perimeter:
        comparison_result = "Circle is longer"
    elif circle_perimeter < rectangle_perimeter:
        comparison_result = "Rectangle is longer"
    else:
        comparison_result = "Equal"
    difference = abs(circle_perimeter - rectangle_perimeter)
    print(comparison_result)
    print(f"{difference:.5f}")
compare_perimeters(float(input()), float(input()), float(input()))
