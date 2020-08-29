from scipy.io import wavfile
import numpy as np
import nnese
from sys import exit

fs, data = wavfile.read('voz.wav')

output = nnese.nnese(data,fs)