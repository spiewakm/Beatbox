# -*- coding: utf-8 -*-
"""
module: read_song:
load definitions of files:
* defs.txt
* song.txt
"""

def readdefs(namesong):
    """
    scope: load a configuration of demo 
    
    output:
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
    scope: load order of tracks in a demo
    
    input: 
    namesong: name of demo
    
    output:
    tracks: vector of list of tracks that contains of a demo 
    """
    namesong = namesong + '/' + 'song.txt'
    with open(namesong) as song:
        tracks = [line.split() for line in song]
    return tracks