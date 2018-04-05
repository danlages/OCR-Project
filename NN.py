import tensorflow as tFlow

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)

nodesLayer1 = 500
nodesLayer2 = 500
nodesLayer3 = 500

numClasses = 10
sizeOfAnalysis = 100 #Determines the batch size of the dataset that will be analysed at a given time.

#Width and hieght of the network
y = tFlow.placeholder(tFlow.float32)
x = tFlow.placeholder(tFlow.float32 ,[None, 784]) #The data is reduced to a matrix of 28 by 28 to be processed (784)

def networkImplementation(data):
    layer1 = {'weights' : tFlow.Variable(tFlow.random_normal([784, nodesLayer1])), #Implement Weights
    'biases' : tFlow.Variable(tFlow.random_normal([nodesLayer1]))} #Implement Biases

    layer2 = {'weights' : tFlow.Variable(tFlow.random_normal([nodesLayer1, nodesLayer2])),
    'biases' :tFlow.Variable(tFlow.random_normal([nodesLayer2]))}

    layer3 = {'weights' : tFlow.Variable(tFlow.random_normal([nodesLayer2, nodesLayer3])),
    'biases' :tFlow.Variable(tFlow.random_normal([nodesLayer3]))}

    outputLayer = {'weights' : tFlow.Variable(tFlow.random_normal([nodesLayer3, numClasses])),
    'biases' :tFlow.Variable(tFlow.random_normal([numClasses]))}


    #(input * weights) + biases
    firstLayer = tFlow.add(tFlow.matmul(data, layer1['weights']), layer1['biases'])
    firstLayer = tFlow.nn.relu(firstLayer) #Rectified linear activation function

    secondLayer = tFlow.add(tFlow.matmul(firstLayer, layer2 ['weights']), layer2['biases'])   #Uses the outputs of the first layer in order perform cslculations on the data, taking into account the weights and biases of the
    secondLayer = tFlow.nn.relu(secondLayer)

    thirdLayer = tFlow.add(tFlow.matmul(secondLayer, layer3['weights']), layer3['biases'])
    thirdLayer = tFlow.nn.relu(thirdLayer)

    outputLayer = tFlow.matmul(thirdLayer, outputLayer['weights']) + outputLayer['biases']

    return outputLayer

def train(input):

    prediction = networkImplementation(x) #Runs neural network model
    costOfError = tFlow.reduce_mean(tFlow.nn.softmax_cross_entropy_with_logits(logits = prediction, labels = y)) #Cost function - difference between desired result and actual preditcion - the desired result is the lable associated with the dataset

    optimzeCost = tFlow.train.AdamOptimizer().minimize(costOfError) #Stohcasic Gradient Decent

    epochsToRun = 10

    tFlowSession = tFlow.InteractiveSession()
    tFlow.global_variables_initializer().run()
    saver = tFlow.train.Saver()

    iterate = 0
    while iterate < 10:
        epochUsed = 0         #trains the networks
        for i in range(int(mnist.train.num_examples/sizeOfAnalysis)):
            eX, eY = mnist.train.next_batch(sizeOfAnalysis)
            i, cost = tFlowSession.run([optimzeCost, costOfError], feed_dict = {x: eX, y: eY}) #Modifies the weights in order to optimise the network - minimizing error
            epochUsed += cost
        iterate = iterate + 1
        print('Epoch:', iterate, 'out of', epochsToRun, ' Margin of Error:', epochUsed)

    save_path = saver.save(tFlowSession, '/Users/daniellages/Documents/Computer Science/Year 3/OCR/OCR-Project/ocrModel.ckpt')
    print ("Save Location: ", save_path)
    correct = tFlow.equal(tFlow.argmax(prediction,1),tFlow.argmax(y, 1))
    accuracy = tFlow.reduce_mean(tFlow.cast(correct, 'float'))

    print ('Accuracy:',accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

train(x)
