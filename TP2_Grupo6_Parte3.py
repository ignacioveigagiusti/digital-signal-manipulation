# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:58:46 2020

@author: Ignacio
"""

import numpy as np
import matplotlib.pyplot as plt
import generador as gen
from scipy.fftpack import fft
from desplazagiro import desplazagiro
from girodesplaza import girodesplaza

samplerate = 1000
timestart=-2
timestop=2
timestep=1/samplerate
timevec = np.arange(timestart,timestop,timestep)
N=48000          #Cantidad de puntos de la FFT


#PARÁMETROS PRIMERA SEÑAL:

amplitud=1         #Amplitud
DC=0               #DC (Para periódicas)
frecuencia=5       #Frecuencia (para periódicas)
fase=0             #Fase
duty=50            #Duty (Para Tren de Pulsos)
width=0.5          #Entre 0 y 1, Posición del Pico (Para Señal Triangular)
primercorte=1      #Primer Corte (Para Sinc)
ancho=1            #Ancho para los pulsos rectangulares y triangulares
t0=1               #Desplazamiento en segundos
giro=1             #Giro (0 ó 1)

#PARÁMETROS SEGUNDA SEÑAL:

amplitud2=1         #Amplitud
DC2=0               #DC
frecuencia2=5       #Frecuencia
fase2=0             #Fase
duty2=50            #Duty (Para Tren de Pulsos)
width2=0.5          #Entre 0 y 1, Posición del Pico (Para Señal Triangular)
primercorte2=1      #Primer Corte (Para Sinc)
ancho2=1            #Ancho para los pulsos rectangulares y triangulares
t02=1               #Desplazamiento en segundos
giro2=1             #Giro (0 ó 1)



sigtype1=0
while 1 > sigtype1 or sigtype1 > 10 :
    sigtype1 = input('''Seleccione un tipo de señal ingresando el número correspondiente para la
                primera señal a convolucionar:
                1 : Coseno
                2 : Cuadrada (Tren de pulsos)
                3 : diente de sierra
                4 : Sinc
                5 : Pulso Rectangular
                6 : Pulso Triangular
                7 : Escalón
                8 : Signo
                9 : Exponencial Unilateral
                10 : Exponencial Bilateral
                ''')
    sigtype1=int(sigtype1)
    if sigtype1 == 1 or sigtype1 == 2:
        break

sig1= gen.generador(timevec, samplerate, amplitud, DC, frecuencia, fase, duty, width, primercorte, ancho, int(sigtype1))

sigmanip1=0
while sigmanip1 != 1 or sigmanip1 != 2 :
    sigmanip1 = input('''Seleccione la manipulación a aplicar a la primer señal:
    1 : Desplazamiento-Giro
    2 : Giro-Desplazamiento
    ''')
    sigmanip1=int(sigmanip1)
    if sigmanip1 == 1 or sigmanip1 == 2:
        sigmanip1=int(sigmanip1)
        break

if sigmanip1 == 1:
    sig1=desplazagiro(sig1, timevec, samplerate, t0, giro)
else:
    sig1=girodesplaza(sig1, timevec, samplerate, t0, giro)


sigtype2=0
while 1 > sigtype2 or sigtype2 > 10 :
    sigtype2 = input('''Seleccione un tipo de señal ingresando el número correspondiente para la
                segunda señal a convolucionar:
                1 : Coseno
                2 : Cuadrada (Tren de pulsos)
                3 : diente de sierra
                4 : Sinc
                5 : Pulso Rectangular
                6 : Pulso Triangular
                7 : Escalón
                8 : Signo
                9 : Exponencial Unilateral
                10 : Exponencial Bilateral
                ''')
    sigtype2=int(sigtype2)
    if sigtype2 == 1 or sigtype2 == 2:
        break

sig2= gen.generador(timevec, samplerate, amplitud2, DC2, frecuencia2, fase2, duty2, width2, primercorte2, ancho2, int(sigtype2))

sigmanip2=0
while sigmanip2 != 1 or sigmanip2 != 2 :
    sigmanip2 = input('''Seleccione la manipulación a aplicar a la primer señal:
    1 : Desplazamiento-Giro
    2 : Giro-Desplazamiento
    ''')
    sigmanip2=int(sigmanip2)
    if sigmanip2 == 1 or sigmanip2 == 2:
        sigmanip2=int(sigmanip2)
        break

if sigmanip2 == 1:
    sig2=desplazagiro(sig2, timevec, samplerate, t02, giro2)
else:
    sig2=girodesplaza(sig2, timevec, samplerate, t02, giro2)


sigconvo= np.convolve(sig1,sig2)

timevecconvo=np.arange(2*timestart,(2*timestop)-(timestep),timestep)


X = fft(sigconvo,N)
lim = int(np.ceil((N+1)/2) - 1)
X = np.append(X[lim:1:-1], X[0:lim])
MX = np.abs(X)
MX = MX / np.size(MX)
f =np.linspace((-N/2), (N/2), N-1) * samplerate/N

max=np.argmax(MX)
print(max)

LIM = -(1.5*(np.abs(np.argmax(MX))))
print(LIM)

LIM2 = (1.5*(np.abs(np.argmax(MX))))
print(LIM2)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2,figsize=(10,10))
plt.setp(ax1, xlabel='Tiempo')
plt.setp(ax2, xlabel='Tiempo')
plt.setp(ax3, xlabel='Tiempo')
plt.setp(ax4, xlabel='Frecuencia')
plt.setp(ax1, ylabel='Amplitud')
plt.setp(ax3, ylabel='Amplitud')
ax1.set_title('Señal 1')
ax2.set_title('Señal 2')
ax3.set_title('Convolución')
ax4.set_title('Convolución en Frecuencia')
ax1.plot(timevec,sig1)
ax2.plot(timevec,sig2)
ax3.plot(timevecconvo,sigconvo)
ax4.plot(f,MX)
ax4.set_xlim( (-2) * np.maximum(frecuencia,frecuencia2) , 2 * np.maximum(frecuencia,frecuencia2))