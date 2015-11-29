# -*- coding: utf-8 -*-
"""
modul: instruments
zawiera definicje instumentu, np. fala piłokształtna, kombinacja funkcji sinus
"""

import nutes as nut
import numpy as np

def gen_instrument(namesong, id_sample, nute, bpm = 60, fs = 44100, attack = 0, decay = 0):
    """
    funkcja generujaca nutki z wybranego 
    instrumentu
    
    dane wejsciowe:
    namesong: nazwa utworu
    
    id_sample: numer instrumentu
       
    fun: funkcja, ktora wyznaczy czestotliwosci dzwieku
    
    nute: ktora nutka ma byc zagrana z wybranego instrumentu
    
    bpm: beat per minute
    fs: samplig freq
    attack, decay
    
    dane wyjściowe:
    wektor y: nutka wygenerowana z instrumentu o id_sample
    """
    
    def readsample(namesong, id_sample):
        """
        funkcja pomocnicza
        opis: wczytanie konfiguracji instrumentu
        
        dane wyjsciowe:
        dicts: slownik, zawierajacy nastepujace informacje:
        id: nazwa instrumentu
        fun: funkcja do generacji nutki z wybranego instrumentu
        duration: dlugosc trwania nutki, tzn wielokrotnosc (60/bpm)
        vol: glosnosc dzwieku
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    