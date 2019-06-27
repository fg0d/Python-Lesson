#!/usr/bin/env python3 
#Python3 дээр бичигдсэн гэдгийг илэрхийлж байна.
# -*- coding: utf-8 -*-
"""
0. install numpy ( sudo apt install python-numpy OR sudo pip install numpy)
1. install matplotlib (sudo apt install python-matplotlib OR sudo pip install matplotlib)
"""
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()
