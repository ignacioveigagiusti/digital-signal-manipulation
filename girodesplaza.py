# -*- coding: utf-8 -*-
import numpy as np

def girodesplaza(x, t, fs, t0, Giro):
    N = len(t)
    d = t0*fs
    x1 = x
    if Giro == 1:
        x1 = np.flipud(x1)
    x2 = np.zeros(N)
    if d > 0:
        for i in range(0,N-int(d)):
            x2[i+d]=x1[i]
    else:
        for i in range(0,N+int(d)):
            x2[i]=x1[i-d]
    return x2