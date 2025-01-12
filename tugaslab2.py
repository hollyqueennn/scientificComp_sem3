# -*- coding: utf-8 -*-
"""tugaslab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13D5_IZ7iKBnSqEwwdNn4hMHDTzbMmgoG
"""

def my_bisection(f, a, b, tol):
    r = [(a+b)/2]
    e = [abs(f(r[0]))]
    i = 0
    if f(a)*f(b) > 0:
        return "Cannot compute the root"
    while e[i] > tol:
        n = (a + b) / 2
        if f(a) * f(n) < 0:
            b = n
        elif f(n) * f(b) < 0:
            a = n
        r.append((a + b) / 2)
        e.append(abs(f(r[i + 1])))
        i += 1
    return r, e

import numpy as np
import math

f = lambda x: x ** 2 - 2

a = 0
b = 2
tol = 1e-1

r, e = my_bisection(f, a, b, tol)

print('Case 1')
print('R =', r)
print('E =', e)

f2 = lambda x: np.sin(x) - np.cos(x)

a = 0
b = 2
tol = 1e-2

r, e = my_bisection(f2, a, b, tol)

print('Case 2')
print('R =', r)
print('E =', e)