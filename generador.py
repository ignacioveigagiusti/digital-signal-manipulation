#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:48:53 2020

@author: fabri
"""

import numpy as np
from scipy.signal import square, sawtooth

def generador(t, fs, amplitud, DC, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):

    """
    Descripción de la función:
    Parámetros de entrada
    amplitud:     Amplitud de la señal periódica
    frecuencia:   Frecuencia de Sinusoide, Cuadrada o Diente de Sierra
    fase:         Fase de la función sinusoidal
    duty:         Duty Cycle para la Señal Cuadrada en porcentaje
    width:        Fracción entre 0 y 1, es donde ocurre el máximo de
                    la Diente de Sierra
    primercorte:  Primer corte del Sinc
    ancho:        Para los pulsos rectangulares y triangulares
    DC:           Nivel DC para las señales periódicas
    tipo:         Señal a ser generada.
                  Si Tipo=1,2,3,4,5 o 6 se generará
                      Cos, Cuadrada, Diente (periódicas), Sinc, Pulso Rec o
                      Pulso Triang (No periódicas) respectivamente.
    Parámetro de salida:
    y:            señal generada
    """
    
    if tipo > 10 or tipo < 0:
        print('ERROR: el valor de Tipo debe estar entre 1 y 10')

    else:
        # Esto es un diccionario, se usa para crear una estructura equivalente 
        # al switch de matlab
        tipos_signal = {1 : coseno(t, frecuencia, fase, duty, width,
                                   primercorte, ancho, tipo),
                        2 : cuadrada(t, frecuencia, fase, duty, width,
                                     primercorte, ancho, tipo),
                        3 : dte_sierra(t, frecuencia, fase, duty, width,
                                       primercorte, ancho, tipo),
                        4 : funcion_sinc(t, frecuencia, fase, duty, width,
                                         primercorte, ancho, tipo),
                        5 : pulso_rec(t, frecuencia, fase, duty, width,
                                      primercorte, ancho, tipo),
                        6 : pulso_tri(t, frecuencia, fase, duty, width,
                                      primercorte, ancho, tipo),
                        7 : esc(t),
                        8 : sign(t),
                        9 : np.exp(-t),
                        10 : np.exp(-abs(t))          
                        }
        
        y = amplitud * tipos_signal[tipo] + DC
        
        return y
    
def coseno(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return np.cos(2 * np.pi * frecuencia * t + fase)

def cuadrada(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return square(2 * np.pi * frecuencia * t + fase)

def dte_sierra(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return sawtooth(2 * np.pi * frecuencia * t, width)

def funcion_sinc(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return np.sinc(t / primercorte)

def pulso_rec(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    # se genera manualmente
    y = np.zeros(t.size)
    inicio = int(0.5*t.size) - int((ancho/8)*t.size) 
    fin = int(0.5*t.size) + int((ancho/8)*t.size)
    y[inicio:fin] = 1
    return y
    
def pulso_tri(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    # el pulso triangular se genera convolucionando 2 rectangulares
    y = np.zeros(t.size//2 + 1)
    inicio = int(0.5*y.size) - int((ancho/8)*y.size) 
    fin = int(0.5*y.size) + int((ancho/8)*y.size)
    y[inicio:fin] = 1
    y = np.convolve(y,y)
    if y.size > t.size:
        y = y[:-1]  # quito una muestra para coincidir la longitud con t
    return y / np.max(y)

def esc(t):
    y = np.where(t < 0, 0, 1)
    return y

def sign(t):
    y = np.where(t < 0, -1, 1)
    return y