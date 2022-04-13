# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 08:07:39 2020

@author: Juan
"""

# -*- coding: utf-8 -*-
import numpy as np


def desplazagiro(x, t, fs, t0, Giro):
    N = len(t)
    d = t0*fs
    x1 = x
    x2 = np.zeros(N)
    if d > 0:
        for i in range(0,N-int(d)):
            x2[i+d]=x1[i]
    else:
        for i in range(0,N+int(d)):
            x2[i]=x1[i-d]
    if Giro == 1:
        x2 = np.flipud(x2)
    return x2