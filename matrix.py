#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

mat = np.zeros((9,9))
for i in range(0,9):
    for j in range(0,3):
	mat[i][j] = 1
    mat[8][i] = 1
mat[(4,7,1),(5,7,8)] = 1
print(mat)

plt.spy(mat)
plt.show()
