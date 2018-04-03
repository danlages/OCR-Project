from skimage import data, io, filters, exposure
from skimage.exposure import equalize_hist
from skimage.color import rgb2gray
from skimage.filters import threshold_mean, median, rank
from skimage.morphology import disk
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from scipy import misc, ndimage

import threading, os, glob

SIZE = 20, 20

#Create array of charaters in folder

def noiseReduction(image):
    image = filters.median(image, np.ones((3 , 3)))
    noise = np.random.random(image.shape)
    image[noise > 0.99] = 255
    image[noise < 0.01] = 0
    image = median(image, disk(1))
    return image

def thresholding(image):
    thresh = threshold_mean(image)
    image = image > thresh
    return image


def modify(path):
    #function for running functions
    characterArray = []
    directoryList = os.listdir(path)
    for file in directoryList:   #loop through folder destination
        if file.endswith(".jpeg") or file.endswith(".jpg"):
            img = os.path.join(charactersPath, file)
            image = io.imread(img)
            image = rgb2gray(image)
            image = noiseReduction(image)
            image = thresholding(image)
            characterArray.append(image) #can append to array to be used in other functions :D
            io.imshow(image)
            io.show()
    return characterArray


if __name__ == "__main__":

    charactersPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/OCR-Project/inputImages"  #Destination of images to process
    destinationPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/Implementation/processed"   #Desitnation to save processed images

    arrayOfCharacters = []
    arrayOfCharacters = modify(charactersPath)

"""    for image in arrayOfCharacters:
        io.imshow(image)
        io.show()
        io.imsave('fileTest.png', image)"""
