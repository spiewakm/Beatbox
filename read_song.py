# -*- coding: utf-8 -*-
"""
modul: read_song:
odczyt definicji plików:
* defs.txt
* song.txt
"""

def readdefs(namesong):
    """
    opis: wczytanie konfiguracji piosenki
    
    dane wyjsciowe:
    bpm: beats per minute
    """
    namesong = namesong + '/' + 'defs.txt'
    with open(namesong, "r") as f:
        dicts = {}
        for line in f:
            values = line.split()
            if values[0] != '{' and values[0] != '}': 
                values[0] = values[0][1:-2]
                dicts[values[0]] = values[1]
    return dicts
    
    

def readsong(namesong):
    """
    opis: wczytywanie kolejnosci trakow w piosence "namesong"
    
    dane wejsciowe: 
    namesong: nazwa piosenki
    
    dane wyjsciowe:
    tracks: wektor z lista trackow, z ktorej sklada sie 
    piosenka "namesong"
    """
    namesong = namesong + '/' + 'song.txt'
    with open(namesong) as song:
        tracks = [line.split() for line in song]
    return tracks