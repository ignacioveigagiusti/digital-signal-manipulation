# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:23:04 2020

@author: Ignacio
"""

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
N=48000          #Cantidad de puntos de la FFT

# importamos las señales Voz masculina y Voz femenina
samplerateVM, sigVMH = wav.read('Voz masculina.wav')
samplerateVF, sigVFH = wav.read('Voz femenina.wav')

sigVM=signal.decimate(sigVMH, 6, n=None, ftype='iir', axis=- 1, zero_phase=True)
sigVF=signal.decimate(sigVFH, 6, n=None, ftype='iir', axis=- 1, zero_phase=True)

samplerateVM=samplerate
samplerateVF=samplerate

duracionVM = np.size(sigVM) / samplerate  # operación para obtener la duración de la señal
timevecVM = np.linspace(0, duracionVM, np.size(sigVM))  # vector tiempo
duracionVF = np.size(sigVF) / samplerate  # operación para obtener la duración de la señal
timevecVF = np.linspace(0, duracionVF, np.size(sigVF))  # vector tiempo

#Creamos un chirp
flimchirp=1000
chirp = signal.chirp(t=timevec, f0=0, t1=1, f1=flimchirp, method='linear', phi=0, vertex_zero=True)

#Creamos la suma de senoidales
f1=samplerate/200

sin1=gen.generador(timevec, samplerate, 1, 0, f1, 0, 50, 0.5, 1, 0.5, 1)
sin2=gen.generador(timevec, samplerate, 1, 0, 2*f1, 0, 50, 0.5, 1, 0.5, 1)
sin3=gen.generador(timevec, samplerate, 1, 0, 3*f1, 0, 50, 0.5, 1, 0.5, 1)
sin4=gen.generador(timevec, samplerate, 1, 0, 4*f1, 0, 50, 0.5, 1, 0.5, 1)
sin5=gen.generador(timevec, samplerate, 1, 0, 5*f1, 0, 50, 0.5, 1, 0.5, 1)

sinsum=sin1+sin2+sin3+sin4+sin5

#creamos los filtros
fc = 250  # frecuencia de corte del filtro
wc = fc / (0.5*samplerate)  # frecuencia normalizada para el filtro digital
fp = [200,500]     # Banda para filtros Bandpass/Bandstop
arraysr=np.array(0.5*samplerate)
wp = fp / arraysr      # Banda normalizada para el filtro digital
rp=4     #Máximo ripple, en dB (chebyshev, ellip)
rs=40     #Mínima atenuación en banda rechazada, en dB (chebyshev, ellip)



# se obtienen los coeficientes de la función de transferencia del filtro
# Butterworth lowpass
b1, a1 = signal.butter(N=3, Wn=wc, btype='low')

# Chebyshev 1 Lowpass
b2, a2 = signal.cheby1(N=3, rp=rp, Wn=wc, btype='low')

# Chebyshev 2 Lowpass
b3, a3 = signal.cheby2(N=3, rs=rs, Wn=wc, btype='low')

# Elíptico Lowpass
b4, a4 = signal.ellip(N=3, rp=rp, rs=rs, Wn=wc, btype='low')

# Butterworth Highpass
b5, a5 = signal.butter(N=3, Wn=wc, btype='highpass')

# Chebyshev 1 Highpass
b6, a6 = signal.cheby1(N=3, rp=rp, Wn=wc, btype='highpass')

# Chebyshev 2 Highpass
b7, a7 = signal.cheby2(N=3, rs=rs, Wn=wc, btype='highpass')

# Elíptico Highpass
b8, a8 = signal.ellip(N=3, rp=rp, rs=rs, Wn=wc, btype='highpass')

# Butterworth Bandpass
b9, a9 = signal.butter(N=3, Wn=wp, btype='band')

# Chebyshev 1 Bandpass
b10, a10 = signal.cheby1(N=3, rp=rp, Wn=wp, btype='band')

# Chebyshev 2 Bandpass
b11, a11 = signal.cheby2(N=3, rs=rs, Wn=wp, btype='band')

# Elíptico Bandpass
b12, a12 = signal.ellip(N=3, rp=rp, rs=rs, Wn=wp, btype='band')

# Butterworth Bandstop
b13, a13 = signal.butter(N=3, Wn=wp, btype='bandstop')

# Chebyshev 1 Bandstop
b14, a14 = signal.cheby1(N=3, rp=rp, Wn=wp, btype='bandstop')

# Chebyshev 2 Bandstop
b15, a15 = signal.cheby2(N=3, rs=rs, Wn=wp, btype='bandstop')

# Elíptico Bandstop
b16, a16 = signal.ellip(N=3, rp=rp, rs=rs, Wn=wp, btype='bandstop')


w1, h1 = signal.freqz(b1,a1)
w2, h2 = signal.freqz(b2,a2)
w3, h3 = signal.freqz(b3,a3)
w4, h4 = signal.freqz(b4,a4)
w5, h5 = signal.freqz(b5,a5)
w6, h6 = signal.freqz(b6,a6)
w7, h7 = signal.freqz(b7,a7)
w8, h8 = signal.freqz(b8,a8)
w9, h9 = signal.freqz(b9,a9)
w10, h10 = signal.freqz(b10,a10)
w11, h11 = signal.freqz(b11,a11)
w12, h12 = signal.freqz(b12,a12)
w13, h13 = signal.freqz(b13,a13)
w14, h14 = signal.freqz(b14,a14)
w15, h15 = signal.freqz(b15,a15)
w16, h16 = signal.freqz(b16,a16)



#Módulo de filtraje:


b=0          #Señal a Filtrar

while b != 1 or b != 2 or b != 3 or b != 4 :
    b = input('''Seleccione la señal a filtrar ingresando un número:
    1 : Voz Masculina
    2 : Voz Femenina
    3 : Chirp
    4 : Suma de Senoidales    
    ''')
    b=int(b)
    if b == 1:
        origsig=sigVM
        break
    elif b == 2:
        origsig=sigVF
        break
    elif b == 3:
        origsig=chirp
        break
    elif b == 4:
        origsig=sinsum
        break
    else:
        break

a = 0
while a<1 or a>16:
    a = input('''Seleccione el filtro ingresando un número:
    1 : Butterworth lowpass
    2 : Chebyshev 1 Lowpass
    3 : Chebyshev 2 Lowpass
    4 : Elíptico Lowpass
    5 : Butterworth Highpass
    6 : Chebyshev 1 Highpass
    7 : Chebyshev 2 Highpass
    8 : Elíptico Highpass
    9 : Butterworth Bandpass
    10 : Chebyshev 1 Bandpass
    11 : Chebyshev 2 Bandpass
    12 : Elíptico Bandpass
    13 : Butterworth Bandstop
    14 : Chebyshev 1 Bandstop
    15 : Chebyshev 2 Bandstop
    16 : Elíptico Bandstop
    ''')
    a=int(a)
    if a == 1:
        bfn, afn = b1, a1 
    elif a == 2:
        bfn, afn = b2, a2
    elif a == 3:
        bfn, afn = b3, a3
    elif a == 4:
        bfn, afn = b4, a4
    elif a == 5:
        bfn, afn = b5, a5
    elif a == 6:
        bfn, afn = b6, a6
    elif a == 7:
        bfn, afn = b7, a7
    elif a == 8:
        bfn, afn = b8, a8
    elif a == 9:
        bfn, afn = b9, a9
    elif a == 10:
        bfn, afn = b10, a10
    elif a == 11:
        bfn, afn = b11, a11
    elif a == 12:
        bfn, afn = b12, a12
    elif a == 13:
        bfn, afn = b13, a13
    elif a == 14:
        bfn, afn = b14, a14
    elif a == 15:
        bfn, afn = b15, a15
    elif a == 16:
        bfn, afn = b16, a16
    else:
        bfn, afn = 0, 0
    
bfn, afn = bfn, afn      #Tipo de Filtro (índices an, bn)


sig_filt = signal.filtfilt(bfn, afn, origsig)
wfn, hfn = signal.freqz(bfn,afn)
labelfilt = 'butter lowpass'     #nombre del filtro

t,y=signal.impulse2((afn,bfn))
respuesta_fase = np.unwrap(np.angle(hfn))


Xo= fft(origsig,N)
X = fft(sig_filt,N)
lim = int(np.ceil((N+1)/2) - 1)
Xo = np.append(Xo[lim:1:-1], Xo[0:lim])
X = np.append(X[lim:1:-1], X[0:lim])
MXo = np.abs(Xo)
MXo = MXo / np.size(MXo)
MX = np.abs(X)
MX = MX / np.size(MX)
f =np.linspace((-N/2), (N/2), N-1) * samplerate/N



plt.figure(figsize=(25,15))
plt.rcParams.update({'font.size': 14})
plt.subplot (221)
plt.title('Señal original y filtrada en tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.plot(timevec,origsig, label = 'Original')
plt.plot(timevec,sig_filt, label = 'Filtrada')
plt.legend()
plt.grid()
plt.subplot (222)
plt.title('Señal original y filtrada en frecuencia')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.xlim(-4000,4000)
plt.plot(f,MXo, label = 'Original')
plt.plot(f,MX, label = 'Filtrada')
plt.legend()
plt.grid()
plt.subplot (234)
plt.title('Magnitud de H')
plt.xlabel('Frecuencia Normalizada')
plt.semilogx(wfn, 20 * np.log10(abs(hfn)), label=labelfilt)
plt.grid()
plt.subplot (235)
plt.title('Fase de H')
plt.xlabel('Frecuencia Normalizada')
plt.plot(wfn, respuesta_fase, label = labelfilt)
plt.grid()
plt.subplot (236)
plt.title('Respuesta al impulso h')
plt.xlabel('Tiempo')
plt.plot(t,y)
plt.grid()