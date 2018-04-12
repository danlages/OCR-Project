images = []
labels = []

datasetAPath = ""
datasetBPath = ""
def defineData(imageList, labelList):
    directoryAList = os.listdir(datasetAPath)
    directoryBList = os.listdir(datasetBPath)
    for file in directoryAList:
        if file.endswith('.png'):
            img = os.path.join(datasetAPath, file)
            image = io.imread(img)
            imageList.append(image)
            labelList.append(1)
    for file in directoryBList:
        if file.endswith('.png'):
            img = os.path.join(datasetBPath, file)
            image = io.imread(img)
            imageList.append(image)
            labelList.append(2)

    return imageList, labelList
