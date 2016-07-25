#!/usr/bin/python

"""
main module: beatbox

this module creates demo of a selected song
from following list of songs:
- harry potter
- winter is coming
- szla dzieweczka
- mam chusteczke

"""
import read_song as rs
import save_song as ss
import create_song as cs
import numpy as np
import zipfile
import os.path
import sys

name = sys.argv[1]

if name not in ('harry_potter', 'mam_chusteczke', 'szla_dzieweczka', 'winter_is_coming'):
    print('Ups... Invalid name of demo! Try again!')
    print('You can choose following names of demo: \n harry_potter \n mam_chusteczke \n szla_dzieweczka \n winter_is_coming')
    sys.exit()
    
print('Wait a minute I am creating demo...')
print("Demo's name: " + name)
print('...')


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

print('Done!\n')
print('You can use following command to play a created demo:')
print('mplayer ' + name + '.wav\n')
print('Have fun!')