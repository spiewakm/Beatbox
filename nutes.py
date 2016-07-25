# -*- coding: utf-8 -*-
"""
module: nutes

this module contains the definition of notes, the definition of a dictionary
and the definition of a function that generates notes

additionally, we assumed that 'basic' notes come from the sine wave
"""

import numpy as np

nute = ['C-0', 'C#0', 'D-0', 'D#0', 'E-0', 'F-0', 'F#0', 'G-0', 'G#0', 'A-0', 'A#0', 'B-0', 
        'C-1', 'C#1', 'D-1', 'D#1', 'E-1', 'F-1', 'F#1', 'G-1', 'G#1', 'A-1', 'A#1', 'B-1', 
        'C-2', 'C#2', 'D-2', 'D#2', 'E-2', 'F-2', 'F#2', 'G-2', 'G#2', 'A-2', 'A#2', 'B-2', 
        'C-3', 'C#3', 'D-3', 'D#3', 'E-3', 'F-3', 'F#3', 'G-3', 'G#3', 'A-3', 'A#3', 'B-3', 
        'C-4', 'C#4', 'D-4', 'D#4', 'E-4', 'F-4', 'F#4', 'G-4', 'G#4', 'A-4', 'A#4', 'B-4', 
        'C-5', 'C#5', 'D-5', 'D#5', 'E-5', 'F-5', 'F#5', 'G-5', 'G#5', 'A-5', 'A#5', 'B-5', 
        'C-6', 'C#6', 'D-6', 'D#6', 'E-6', 'F-6', 'F#6', 'G-6', 'G#6', 'A-6', 'A#6', 'B-6', 
        'C-7', 'C#7', 'D-7', 'D#7', 'E-7', 'F-7', 'F#7', 'G-7', 'G#7', 'A-7', 'A#7', 'B-7', 
        'C-8', 'C#8', 'D-8', 'D#8', 'E-8', 'F-8', 'F#8', 'G-8', 'G#8', 'A-8', 'A#8', 'B-8']

freq = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87, 
        32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74, 
        65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.83, 110.00, 116.54, 123.47, 
        130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 
        246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 
        466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61, 
        880.00, 932.33, 987.77, 1046.50, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 
        1661.22, 1760.00, 1864.66, 1975.53, 2093.00, 2217.46, 2349.32, 2489.02, 2637.02, 2793.83, 2959.96, 
        3135.96, 3322.44, 3520.00, 3729.31, 3951.07, 4186.01, 4434.92, 4698.63, 4978.03, 5274.04, 5587.65, 
        5919.91, 6271.93, 6644.88, 7040.00, 7458.62, 7902.13]

# definition of dictionary
Nutes = {}
for i in range(len(nute)):
    Nutes[nute[i]] = freq[i]
    
def gen_nute(nute, Nutes, bpm, fs = 44100):
    """
    scope: function that generated nutes
    
    input: 
    nute: definition of nute, eg. A-4
    Nutes: dictionary contains frequency corresponding to notes 
    
    output:
    vector y: generated note from the sine waves
    """
    f = Nutes[str(nute)] # czestotliwosc odpowiadajaca danej nutce
    T = 1.5*(60/bpm) # zakladam, ze nutka trwa 1.5 
    #fs = int(fs*(60/bpm)) # Hz, sampling frequency
    
    t = np.linspace(0, T, int(fs*T))
    y = np.sin(2*np.pi*f*t)

    attack = 0.01
    decay = 0.05
    if attack > 0: y[0:int(T*fs*attack)] *= np.linspace(0, 1 ,int(T*fs*attack))
    if decay > 0: 
        y[-int(T*fs*decay):-1] *= np.linspace(1,0,int(T*fs*decay) - 1)
    return y