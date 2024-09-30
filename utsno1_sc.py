# -*- coding: utf-8 -*-
"""UTSNO1_SC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UsSTbSFkEhtPvZ7OQ7oOb5FyTEt2MfBn
"""

import numpy as np
import sys

def input_dialog():
    m = int(input("Masukkan jumlah variabel: "))
    a = [[0.0] * (m+1) for i in range(m)]
    for i in range(m):
        print("Masukkan koefisien dan hasil persamaan ke %d"%(i+1))
        for j in range(m+1):
            if j == m:
                b = input("Hasil persamaan: ")
                a[i][j] = b
            else:
                b = input("Koefisien ke-%d: "%(j+1))
                a[i][j] = b
    a = np.array(a, dtype=float)
    return (a, m)

def forward_elimination(b, n):
    for i in range(n-1):
        if b[i][i] == 0:
            sys.exit()
        for j in range(i+1, n):
            ratio = b[j][i] / b[i][i]
            for k in range(n+1):
                b[j][k] = b[j][k] - ratio * b[i][k]
    return b

def back_substitution(c, n):
    y = np.zeros(n)
    y[n-1] = c[n-1][n] / c[n-1][n-1]
    for i in range(n-2,-1,-1):
        y[i] = c[i][n]
        for j in range(i+1,n):
            y[i] = y[i] - c[i][j] * y[j]
        y[i] = y[i]/c[i][i]
    return y

matrix, m = input_dialog()
matrix = forward_elimination(matrix, m)
result = back_substitution(matrix, m)

def format_titik(value):
    formatted = format(int(value), ',')
    return formatted.replace(',', '.')

print(f"Batu bata: Rp {format_titik(result[0])} /kg")
print(f"Semen: Rp {format_titik(result[1])} /kg")
print(f"Besi: Rp {format_titik(result[2])} /kg")