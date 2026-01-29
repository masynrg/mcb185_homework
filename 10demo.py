# 10demo.py by masyn

print('hello, again') #greeting

print(1.5e-2)
print(4*2)
print(15%6)

import math

print(math.log10(100))
print(math.sqrt(64))
print(math.pi)

#functions

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)   
print(pythagoras(3, 4))

def circle_area(r): return (math.pi * r**2)
def rectangle_area(w, h): return (w * h)

def f_to_c(f): return ((f - 32) * (5 / 9))
def mph_to_kph(m): return (m * 1.6)
def amean3(a, b, c): return ((a + b + c) / 3)
def gmean3(a, b, c): return (math.cbrt(a * b * c))
def hmean3(a, b, c): return (3 / ((1/a) + (1/b) + (1/c)))
def distance(a, b, x, y): return math.sqrt(((b-a)**2) + ((y-x)**2))