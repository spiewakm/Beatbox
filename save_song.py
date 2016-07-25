"""
module: save_song:

this module saves a demo to a locale folder
"""

import numpy as np
import scipy.io.wavfile
                      
def writesong(song, namesong, fs = 44100, bpm = 120):
    """
    scope: save created a vector y to a locale folder
    """
    scipy.io.wavfile.write(namesong + '.wav',
                       int(fs),
                       np.int16(song/max(np.abs(song))*32767))
                       