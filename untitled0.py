# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:25:01 2020

@author: Ignacio
"""
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import scipy
import scipy.io.wavfile as wav
import fftplot as fftplt
from scipy.fftpack import fft, ifft
from matplotlib.pyplot import figure
import generador as gen
import IPython.display as ipd

samplerate = 8000  #Frecuencia de Muestreo
timestart=0       #Tiempo Inicial
timestop=1         #Tiempo Final
timestep=1/samplerate           
timevec = np.arange(timestart,timestop,timestep)   #Vector Temporal
N=1024          #Cantidad de puntos de la FFT

flimchirp=1000
chirp = signal.chirp(t=timevec, f0=0, t1=1, f1=flimchirp, method='linear', phi=0, vertex_zero=True)

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
plt.plot(timevec,chirp)
plt.title('Chirp')


X = fft(chirp,N)
lim = int(np.ceil((N+1)/2) - 1)
X = np.append(X[lim:1:-1], X[0:lim])  # Se corrige el espectro para ver 
                                                 # el nivel DC en el origen

MX = np.abs(X)  # Se busca el modulo de X

MX = MX / np.size(MX)  # Se escala para que la magnitud no sea funcion del tamano del vector x

f =np.linspace((-N/2), (N/2), N-1) * fs/N  # Se genera el eje de frecuencias

fig, ax1 = plt.subplots()  # Se grafica el modulo              
ax1.plot(f,MX)
ax1.set_xlabel('frecuencia [Hz]')
ax1.set_ylabel('amplitud')
ax1.set_title(title)