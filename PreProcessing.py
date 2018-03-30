from skimage import data, io, filters
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import glob
import shutil
from PIL import Image

import threading, os, glob


#Create array of charaters in folder

def defineImages(charactersPath):
#Will need to crop here - (mnist supports 20*20
    directoryList = os.listdir(charactersPath)
    characterArray = []
    for file in directoryList:   #loop through folder destination
        if file.endswith(".jpeg") or file.endswith(".jpg"):
            img = Image.open(os.path.join(charactersPath, file))
            #numpyArray = np.array(img)
            characterArray.append(img)
    return characterArray


#def convertToArray:

#def thresholding(characterArray):
    #for image in characterArray:

    #return characterArray

#def noiseReduction(characterArray):
#    for image in characterArray:

#    return characterArray

#def shapness(characterArray):
    #for image in characterArray:

    #return characterArray


#def saveToFolder(characterArray, destination):
    #for file in characterArray:

    #return characterArray


if __name__ == "__main__":

    charactersPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/Implementation/inputImages"  #Destination of images to process
    destinationPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/Implementation/processed"   #Desitnation to save processed images

    arrayOfCharacters = defineImages(charactersPath)

    #for image in arrayOfCharacters:
        #Image.show(image)

    for file in arrayOfCharacters:
        file.show()

    #saveToFolder(arrayOfCharacters, destinationPath)

    #print arrayOfCharacters
