# importing libraries
import numpy as np
import scipy
import essentia
import librosa
import librosa.display
import matplotlib.pyplot as pyplot


## load .wav file
path = ""

## audio loader
loader = essentia.standard.MonoLoader(filename=path)

audio = loader()

## Tonic Indian Art Music

tonic = essentia.standard.TonicIndianArtMusic()(audio)

print(tonic)
