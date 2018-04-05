from PIL import Image
from scipy import misc, ndimage
from skimage import data, io, filters, exposure, img_as_uint
from skimage.exposure import equalize_hist
from skimage.color import rgb2gray
from skimage.filters import threshold_mean, median, rank
from skimage.morphology import disk
import matplotlib.pyplot as plt
import numpy as np

import threading, os, glob

SIZE = 28
#Create array of charaters in folder

destinationPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/OCR-Project/processed/"

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
    i = 0
    for file in directoryList:   #loop through folder destination
        if file.endswith(".jpeg") or file.endswith(".jpg"):
            img = os.path.join(charactersPath, file)
            i = i + 1
            image = io.imread(img)
            image = rgb2gray(image)
            image = noiseReduction(image)
            image = thresholding(image)
            characterArray.append(image) #can append to array to be used in other functions :D
            io.imshow(image)
            io.show()
    return characterArray

def saveImage(characterArray, path):
    for i, image in enumerate(characterArray):
        io.imsave(path + "file" + str(i) + ".png", img_as_uint(image))

def prepareForMNIST():
    arrayOfOutputs = []
    directoryList = os.listdir(destinationPath)
    for file in directoryList:
        if file.endswith(".png"):
            img = os.path.join(destinationPath, file)
            data = Image.open(img).convert('L')
            width = float(data.size[0])
            height = float(data.size[1])

            newMnistInput = Image.new('L', (SIZE, SIZE), 255)

            if height > width:
                imageWidth = int(round((20.0/height*width),0))
                mnistImage = data.resize((imageWidth,20), Image.LANCZOS)
                positionV = int(round(((SIZE - imageWidth)/2),0))
                newMnistInput.paste(mnistImage, (positionV, 4))

            elif width > height:
                imageHeight = int(round((20.0/width*height),0))
                mnistImage = data.resize((imageHeight,20), Image.LANCZOS)
                positionH = int(round(((SIZE - imageHeight)/2),0))
                newMnistInput.paste(mnistImage, (positionH, 4))
            arrayOfOutputs.append(newMnistInput)

    return arrayOfOutputs


if __name__ == "__main__":

    charactersPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/OCR-Project/inputImages/"  #Destination of images to process
    finalPath = "/Users/daniellages/Documents/Computer Science/Year 3/OCR/OCR-Project/imagesForOCR/"
    arrayOfCharacters = []
    arrayOfMNIST = []
    arrayOfCharacters = modify(charactersPath)
    saveImage(arrayOfCharacters, destinationPath) #Save Image for preperation
    arrayOfMNIST = prepareForMNIST()
    saveImage(arrayOfMNIST, finalPath)
