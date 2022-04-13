# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 08:36:38 2020

@author: Juan
"""


import numpy as np


def desplaza(x, t, fs, t0):
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
    return x2

#function [salidaManipulada]= desplazamiento(x,fs,t,t0)     
#N=length(t);  % se determina el número de muestras total
#d=t0*fs;      % se calcula el desplazamiento en muestras   
#x1=x;          % se usa una variable auxiliar
#x2=zeros(1,N); % se inicializa el vector aux. con ceros
#if d>0         % se verifica si se quiere desplazar a la izquierda
#               %para tratarlos de manera diferente
#for i=1:N-d;
#    x2(i+d)=x1(i);  % movimiento a la derecha
#end
#else
#    for i=1:N+d
#        x2(i)=x1(i-d); % movimiento a la izquierda
#    end
#end
#salidaManipulada=x2;
