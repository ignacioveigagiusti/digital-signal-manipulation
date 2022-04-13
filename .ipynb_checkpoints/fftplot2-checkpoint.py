#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NOTA: en Python, a diferencia de matlab, uno no necesita crear un archivo 
aparte para construir una función. No obstante, en este caso lo hacemos así,
para facilitar su reutilización.

La estructura de las funciones es del tipo:
    
def mi_funcion(param1, param2, param3):
    .
    .
    (código que va a ejecutar la función)
    .
    .
    return resul1, resul2
    
mi_funcion es una funcion que recibe tres parámetros y devuelve dos valores
    
Luego hago un llamado a esa función para ejecutarla:

r1, r2 = mi_funcion(param1 = a, param2 = b, param3 = c)

A continuación creamos una función que grafica una fft a partir de una señal x

"""

import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

def graficar_fft(x, fs, objeto_ax, N='default', title=''):
    
    """
    Funcion que calcula la transformada de Fourier de x
    y grafica su modulo y fase (el eje x muestra los valores de frecuencia)
    
    Parámetros:
            
            x: es la señal a la que se le desea hallar la fft
            
            fs: es la frecuencia de muestreo de la senal original
            
            N: es el numero de puntos de la fft, debe ser una potencia de 2,
                de no ser asi, el algoritmo corrige tal que N es la proxima 
                potencia de 2 mas cercana al N proporcionado por el usuario
                
            objeto_ax: objeto axes sobre el cual graficar
            
    Retorna:
        
            X: contiene la Transformada de Fourier

    """

    # Coloca los valores por default para N
    if N == 'default':
        N = 2**(proxima_potencia_de_2(np.size(x)))
        
    # Calcula la fft, haciendo zero padding
    X = fft(x,N)
    lim = int(np.ceil((N+1)/2) - 1)
    X = np.append(X[lim:1:-1], X[0:lim])  # Se corrige el espectro para ver 
                                                 # el nivel DC en el origen

    MX = np.abs(X)  # Se busca el modulo de X

    MX = MX / np.size(MX)  # Se escala para que la magnitud no sea funcion del tamano del vector x

    #MX = MX / N

    f = f=np.linspace((-N/2), (N/2), N-1) * fs/N  # Se genera el eje de frecuencias

    print(np.sum(MX))
    # fig, ax1 = plt.subplots()  # Se grafica el modulo              
    objeto_ax.plot(f,MX)
    objeto_ax.set_xlabel('frecuencia [Hz]')
    objeto_ax.set_ylabel('amplitud')
    objeto_ax.set_title(title)

# funcion accesoria para calcular la potencia de 2 mas cercana a un numero
def proxima_potencia_de_2(numero):
    if numero > 1:
        for i in range(1, int(numero)):
            if (2 ** i >= numero):
                return 2 ** i
    else:
        print('Ingrese un número mayor o igual a 2')