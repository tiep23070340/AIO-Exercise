import numpy as np

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def approx_cos(x, n):
    cos_x = 0
    for i in range(n):
        cos_x += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return cos_x

def approx_sin(x, n):
    sin_x = 0
    for i in range(n):
        sin_x += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return sin_x

def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        cosh_x += (x ** (2 * i)) / factorial(2 * i)
    return cosh_x

def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n):
        sinh_x += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return sinh_x

x = 3.14
n = 10
print(approx_sin(x, n))
print(approx_cos(x, n))
print(approx_sinh(x, n))
print(approx_cosh(x, n))

assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))

assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))

assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))

assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))