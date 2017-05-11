#!/bin/python

from math import pow, sqrt

g = 9.81
y = 0.00273151
a = 0.00490
b = 0.02840
l = 0.0901

### odchylky

ul = 0.0001
ua = 0.00005
ub = ua
uy = 2.145 * pow(10, -6)

def E():
    return g * pow(l, 3) / (4 * pow(a, 3) * b * y)

def uE():
    return E() * sqrt(pow(3 * ul / l, 2) + pow(3 * ua / a, 2) + pow(ub / b, 2) + pow(uy / y, 2))

print(uE())
print(E())
