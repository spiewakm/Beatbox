# -*- coding: utf-8 -*-
"""
module: create_song

this module contains functions so that we can create a demo
"""

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import scipy.io.wavfile
import re
import nutes as nut
import instruments as inst

def trackload(namesong, tracks, bpm, fs = 44100, attack = 0, decay = 0):
    """
    scope: function to create a demo
    
    input:
    namesong: name of demo/song
    tracks: list of tracks that consists of a demo
    bpm: beats per minute
    fs: sampling frequency
    attack
    decay
    
    output:
    vector y: demo
    """
    y = np.array([]) # wyjsciowa piosenka
    counter = 0 # ktora sekunda dla kolejnej linii sampli
    sumn = 0 #
    fs_bpm = int(fs*(60/bpm)) 
    
    len_tracks = len(tracks)
    
    # wczytujemy po kolei kazdy track:
    for t in np.arange(len_tracks): # t linijka w song.txt
        track = namesong + '/track' + tracks[t][0] + '.txt'
        
    # wczytywanie kolejnosci sciezek:
        with open(track) as tr:
            samples = [line.split() for line in tr]
        
        len_samples = len(samples)
        # wczytywanie kazdej linijki danego tracku
        for s in np.arange(len_samples):
            new_line = samples[s]
            
            # kiedy wczytujemy kolejne 
            if counter > 0: sumn = np.sum([sumn, fs_bpm])
            counter += 1
                
            # dodawanie do wyjsciowego wektora y
            for i in range(len(new_line)):
                #print(new_line)
                if new_line[i] != '--':
                        # sprawdzamy, czy to nutka:
                    if bool(re.search("^[A-G]", new_line[i])):
                        #print((new_line[i], Nutes[new_line[i]]))
                        y_tmp = nut.gen_nute(new_line[i], nut.Nutes, bpm = bpm)
                        # sprawdzamy, czy instrument:
                    elif len(new_line[i]) == 6:
                        tmp = new_line[i]
                        id = tmp[0:2]
                        nute = tmp[-3:]
                        y_tmp = inst.gen_instrument(namesong, id, nute, bpm = bpm)
                        # jesli zadne z powyzszych, wczytujemy sample.wav lub
                    else:
                       fs_tmp, y_tmp = scipy.io.wavfile.read(namesong + '/sample' + new_line[i] + '.wav')
                       y_tmp = np.mean(y_tmp, axis = 1)
                       y_tmp /= 3276
                       y_tmp *= 0.5
                # pause
                else:
                    y_tmp = np.repeat(0, fs_bpm)
                            
                n = len(y_tmp)
                   
                if len(y) == 0: 
                    y = np.r_[y, y_tmp]
                else:
                    if sumn + n  > len(y)  : 
                        diff = len(y) - sumn
                        y[sumn:] += y_tmp[:diff]
                        y = np.r_[y, y_tmp[diff:]]

                    elif sumn + n  <= len(y) :
                        y[sumn:] += np.pad(y_tmp, (0, len(y) - sumn - n), mode = 'constant')
                    
    return y                 