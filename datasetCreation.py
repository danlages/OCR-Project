datasetPath = ""

images = []
labels = []


def defineData(images, labels):
    directoryList = os.listdir(datasetPath)
    for file in directoryList:
        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".JPG"):
            images.append(os.path.join(datasetPath, file))
            labels.append("a")
    return images, labels

def defineDataset(filename, label):
    imageAsString = tFlow.read_file(str(filename))
    imageData = tFlow.image.decode_png(imageAsString, channels = 1)
    image = tFlow.cast(imageData, tFlow.float32)
    return image, label

images, lables = defineData(images, labels)

dataset = tFlow.data.Dataset.from_tensor_slices((images, labels))
dataset = dataset.map(defineDataset)
