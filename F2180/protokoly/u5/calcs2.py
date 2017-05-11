#!/bin/python

from math import pow, sqrt

d = (2.02 + 2.02 + 2.02 + 1.98 * 5 + 1.96 + 1.96) / 10000
l = 0.522
m = 5.905
R = (9.952 + 9.962 + 9.948 + 9.962 + 9.952 + 9.954 + 9.942 + 9.952 + 9.958 + 9.944) / 1000 * 1/2
T = (19.68 + 19.81 + 19.84 + 19.72 + 19.78 + 19.72 + 19.75 + 19.78 + 19.94 + 19.84) / 100

ud = 0.00001
ul = 0.001
um = 0
uR = 0.00001
uT = 0.01

def G() :
    return 16 * 3.14 * pow(R, 2) * l / (5 * pow(d / 2, 4) * pow(T, 2))

def uG():
    return G() * sqrt(pow(2 * uR / R, 2) + pow(ul / l, 2) + pow(4 * ud / d, 2) + pow(2 * uT / T, 2))

print(G())
print(uG())
print(R)
print(d / 2)
print(T)
