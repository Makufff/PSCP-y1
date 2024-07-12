"""Burhhh"""
x_me = float(input())
y_me = float(input())
radius = float(input())
x_mosquito = float(input())
y_mosquito = float(input())
if ((x_me - x_mosquito)**2 + (y_me - y_mosquito)**2)**0.5 <= radius:
    print("Yes")
else:
    print("No")
