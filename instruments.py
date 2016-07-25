# -*- coding: utf-8 -*-
"""
module: instruments

this modeule contains definition of a instrument,
for example: combination of sine waves or sawtooth waves
"""

import nutes as nut
import numpy as np

def gen_instrument(namesong, id_sample, nute, bpm = 60, fs = 44100, attack = 0, decay = 0):
    """
    function generates notes from selected instrument
    
    input:
    namesong: name of demo/song
    
    id_sample: number of instrument
       
    fun: function that determines frequency of sound
    
    note: which notes should be played from a selected instrument
    
    bpm: beat per minute
    fs: samplig freq
    attack, decay
  
    output:
    vector y: generated note from an id_sample instrument
    """
    
    def readsample(namesong, id_sample):
        """
        scope: load a configuration of instrument
        
        output:
        dicts: dictionary contains following info:
        id: name of instrument
        fun: function to generate note from selected instrument 
        duration: duration of notes (60/bpm)
        vol: volume of sound
        attack, decay
        """
        namesong = namesong + '/sample' + id_sample +  '.txt'
        with open(namesong, "r") as f:
            dicts = {}
            for line in f:
                values = line.split()
                if values[0] != '{' and values[0] != '}': 
                    values[0] = values[0][1:-2]
                    dicts[values[0]] = values[1]
        return dicts
    
    sample_new = readsample(namesong, id_sample)
    d = float(sample_new['duration']) # duration, ile razy dluzej trwa sample

    f = nut.Nutes[nute]
    T = d*(60/bpm)
    #fs = int(fs*(60/bpm))
    t = np.linspace(0, T, fs*T)
    
    #id = sample_new['id']
    fun = sample_new['fun']
    y = eval(fun)
    y *= float(sample_new['vol'])
    
    attack = float(sample_new['attack'])
    decay = float(sample_new['decay'])
    if attack > 0: y[0:int(T*fs*attack)] *= np.linspace(0,1,int(T*fs*attack))
    if decay > 0:
        y[-int(T*fs*decay):-1] *= np.linspace(1,0,int(T*fs*decay) - 1)
    return y
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    