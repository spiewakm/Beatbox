"""
modul: save_song:
zapis piosenki do katalog /var/tmp
"""

import numpy as np
import scipy.io.wavfile
                      
def writesong(song, namesong, fs = 44100, bpm = 120):
    """
    opis: zapisuje stworzony wektor y
    do katalogu /var/tmp/
    """
    scipy.io.wavfile.write('/var/tmp/' + namesong + '.wav',
                       int(fs),
                       np.int16(song/max(np.abs(song))*32767))
                       