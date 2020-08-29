import math
import numpy as np

def nnese(inputData,fs,window=32,confidenceLevel=0.95,snr=4,alpha=0.35,beta=0.65):
	
	frameSize,h,kmin,dimension = calcAllConstants(confidenceLevel,window,fs)

	normalizedThreshold = calcNormalizedThreshold(dimension,snr)

	dataFrames = frame(inputData,frameSize)

	print(dataFrames.shape)

def calcAllConstants(confidenceLevel,window,fs):
	
	frameSize = math.floor(window*fs/1000)

	if frameSize%2 == 1:
		frameSize = frameSize + 1

	dimension = 1

	N = dimension/2

	h = 1/math.sqrt((1-confidenceLevel)*4*frameSize)

	kmin = math.floor((frameSize/2)-h*frameSize)


	return (frameSize,h,kmin,dimension)

def frame(samples,frameSize):
	
	numFrames = int(len(samples)/frameSize);
	
	frames = np.zeros((numFrames,frameSize))

	for i in range(0,numFrames):
		frames[i,:] = samples[i*frameSize:(i+1)*frameSize]

	return frames

def calcNormalizedThreshold(dimension, snr):
	if snr == 0:
	
		normalizedThreshold = math.sqrt(dimension)
	
	else:
	
		normalizedThreshold = (1/snr)*math.acosh(math.exp(math.pow(snr,2)/2))

	return normalizedThreshold




