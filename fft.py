# -*- coding: utf-8 -*-

from numpy import linspace, mean
from scipy.fftpack import fft, fftfreq
from scipy.io.wavfile import read
from sys import platform
if platform == 'darwin':
    import matplotlib as plt
    plt.use("TkAgg")
    from matplotlib import pyplot


def plot(choix, plotNumb):
    audiopath = "music/" + choix + ".wav"

    # lecture du fichier son mono
    rate,signal = read(audiopath)

    # definition du vecteur temps
    dt = 1./rate
    FFT_size = 2**18
    NbEch = signal.shape[0]

    t = linspace(0,(NbEch-1)*dt,NbEch)
    t = t[0:FFT_size]

    # calcul de la TFD par l'algo de FFT
    signal = signal[0:FFT_size]
    signal = signal - mean(signal)  # soustraction de la valeur moyenne du signal
                                    # la frequence nulle ne nous interesse pas
    signal_FFT = abs(fft(signal))   # on ne recupere que les composantes reelles


    # recuperation du domaine frequentiel
    signal_freq = fftfreq(signal.size)

    # extraction des valeurs reelles de la FFT et du domaine frequentiel
    signal_FFT = signal_FFT[0:len(signal_FFT)//2]
    signal_freq = signal_freq[0:len(signal_freq)//2]

    y = [2 for i in range(signal_freq.size)]
    for i in range(signal_freq.size // 1):

        if signal_FFT[i] > 1000000:
            y[i] = 1
            #print(signal_FFT[i])
            #print(signal_freq[i])
            #print(y[i])
        else:
            y[i] = 0
            #print(signal_FFT[i])
            #print(signal_freq[i])
            #print(y[i])

    print("taille du tableau bool du seuil")
    print(len(y))

    #affichage du spectre du signal
    pyplot.figure(figsize=(5, 2))
    pyplot.title(choix)
    pyplot.plot(signal_freq,signal_FFT)
    #pyplot.plot(t,signal)
    #pyplot.xlabel('Temps (s)')
    pyplot.xlabel('Frequence (Hz)')
    pyplot.ylabel('Amplitude')
    #pyplot.grid()

    if (plotNumb == 1):
        pyplot.savefig('myplot1.jpg')
    else:
        pyplot.savefig('myplot2.jpg')
    pyplot.clf()
    pyplot.cla()

    return y