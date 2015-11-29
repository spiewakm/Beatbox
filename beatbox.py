#!/opt/anaconda3/bin/python3

"""
modul glowny: beatbox

modul sluzy do tworzenia demo
"""

print('Zaczekaj chwile, tworze demo...')

import sys

name = sys.argv[1][:-1]
print(name)

import read_song as rs
import save_song as ss
import create_song as cs
import numpy as np
import zipfile
import os.path

# zakladam, ze jesli nie ma pliku .zip wowczas 
# istnieje rozpakowany katalog namesong
name_tmp = name + '.zip'
if os.path.isfile(name_tmp): 
    with zipfile.ZipFile(name_tmp, "r") as z:
        z.extractall('/tmp/')
        namesong = '/tmp/' + name
else: namesong = name

defs = rs.readdefs(namesong)
bpm = int(defs['bpm'])
attack = float(defs['attack'])
decay = float(defs['decay'])

tracks = rs.readsong(namesong)
y = cs.trackload(namesong, tracks, bpm, attack = attack, decay = decay)

fs_bpm = 44100*bpm
y[0:int(fs_bpm*attack)] *= np.linspace(0, 1, int(fs_bpm*attack))
if decay > 0: 
    y[-int(fs_bpm*decay):-1] *= np.linspace(1, 0, int(fs_bpm*decay) - 1)

ss.writesong(song = y, namesong = name, bpm = bpm)

print('Done!')
