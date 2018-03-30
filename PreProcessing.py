from skimage import data, io, filters, threshold_otsu,
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import threading, os, glob


#Create array of charaters in folder

def defineImages(charactersPath):
#Will need to crop here - (mnist supports 20*20)
    for image in charactersPath:   #loop through folder destination

return characterArray

def thresholding(characterFile):

    for image in characterArray

return characterArray

def noiseReduction(characterArray):

    for image in characterArray

return characterArray

def shapness(characterArray):

    for image in characterArray

return characterArray


def saveToFolder(characterArray):

    for image in characterArray


if __name__ == "__main__":

charactersPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/Implementation/inputImages"

arrayOfCharacters = defineImages(charactersPath)
