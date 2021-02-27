# Deep Learning

## Installation & hands-on

1. conda install tensorflow
2. Open an run the given python notebooks via anaconda-> Jupyter.

## Neural network

It’s a technique for building a computer program that learns from data. It is based very loosely on how we think the human brain works. First, a collection of software “neurons” are created and connected together, allowing them to send messages to each other. Next, the network is asked to solve a problem, which it attempts to do over and over, each time strengthening the connections that lead to success and diminishing those that lead to failure. 

Neurons work in a set of parallel pipes, and that's exactly how most of graphics cards work today.

**Q.** So when do you really use neural-networks/deep-learning?

**A.** When you have a very large data, and enough processing power for it, and when you want very accurate results. eg. self driving cars, cancer detection etc.

**LTU**: Linear Threshold Unit adds weights to output of 1 neuron going to the next set of neurons. Outputs by the next set of neurons are given by a step function that multiplies the weights and corresponding outputs, and sum them all, and outputs 1 if sum > 0. (See Image) 

**Perceptron**: A Layer of LTUs. A perceptron works by rewarding (increasing) weights that lead to correct behaviour during training.  

**MLP**: Deep Neural Network is basically Multi-layer perceptrons (MLP) with hidden layers. We reduce the no. of neurons as we move from initial layer to the next layers. 

Use the below url to play around newural networks.
```
http://playground.tensorflow.org/
```

## Important terms for deep learning

**Gradient-Descent** is a training algorithm for minimizing error over multiple steps. Basically we try different set of parameter values so that the error minimises before rising again. See Images folder for 'ball rolling down the hill' analogy. Beware of local minimas.

**Autodiff** is a calculus trick for optimally finding the gradients in gradient descent.

**Softmax** is a function used for classification using probability, for several given input values.

**Sigmoid**: While softmax is used for multi-class classification problems, sigmoid function is used for binay classification problems.

**Backpropogation**: algorithm used to traing MLP's weights.

**Activation Functions (aka rectifiers)**: Step functions don't work with gradient descent, as step functions don't have any gradient. Alternative approach is to use activation functions like **ReLU** (Rectified Liniar Unit).

**Optimization Functions**: Used to speed up gradient descent, by speeding up when on a slope, and slowing down when reaching a bottom. **Adam** is a popular choice of optimising function.

**Regularisation** = prevent overfitting. With thousands of weights to tune, overfitting is a problem. Dropout and early stopping are 2 common techniques for regularisation:

1. **Dropout** = Ignore x% of neurons at each stage.
2. **Early-Stopping** = Stop processing input data once performance starts dropping.

**Learning Rate and batch size**: As part of gradient descent, we start at a random point and sample different solutions (weights) to minimise some cost function. How far apart these samples are - is known as learning rate. Small learning rate may take too long to find the optimal solution, and a large learning rate can lead to overshooting the optimal solution.

Batch-size is how many training samples used within each epoch. Small batch-size can wiggle its way out of local minima, while large batch sizes can converge on a wrong solution at random. 

## TensorFlow
Library developed by Google used to construct artificial neural networks. Tensorflow can work on any platform, even on a mobile phone. And can also be used to distribute work across GPUs.

Tensorflow is basically used to construct graphs, and then execute those graphs. This feature makes this library useful for deep learning as well (DL was not the goal when the library was built initially).

A **tensor** is an array of values, used to configure the tensorflow execution. Getting these hyperparameters right is mostly what decides the success of DL model. Most of the times, trial and error help find the right solution.

Tensorflow provides matrix multiplication that can be used to mimic a Perceptron (see images).

Note that neural networks can work when the input data is normalized. scikit_learn's StandardScalar can do this for you. 

## Keras

Higher level API for deep learning on top of TensorFlow, available in Tensorflow 1.9+. It integrates well with scikit_learn as well. See the given examples in this project, for the same problem, the code when using Keras is way smaller than using TensorFlow directly.

## CNN - Convolutional Neural Networks

When you want to process data that doesn't neatly align into columns. Eg. Finding features within images (eg. stop sign on a road), sentiment analysis etc. CNNs work with overlapping layers of neurons that respond to a particular aspect of data, and feed the output to the next layer (convolution) which process increasingly complex aspect of the data. That's how the visual cortex of the brain works. For eg. an image of a road with stop sign, first set of neurons will process that it is an image, then the next layer will identify that there is a road, the next layer will identify that it has a sign, and then the last layer will process the design/color/shape/text of the sign to say that it is a 'STOP' sign. CNNs are very much resource intensive (CPU, RAM, GPU), but give very high accuracy. Hence used for areas like self driving cars where accuracy is of paramount importance. Getting training data, as well as saving it for CNN is also very hard (think of self driving cars sending real time data).

To do CNN with Keras, see the images folder, and the given python notebook.

## RNN - Recurrent Neural Networks

Used for time series data, ie when you want to predict future behavior based on past data. eg. Stock trades, self driving cars etc.

**Memory cell**: Output of one neuron is fed back to the same neuron as well. So over time, past behaviour of neuron influences present behaviour of the neuron.

This backpropagation can be truncated through time by limiting the number of steps going back in.

For RNN topologies, see the images folder.

**LSTM Cell**: Long-Short term memory cell => States from earlier time steps get diluted over time (eg. early words of a sentence can get diluted by the end of a sentence when learning a sentence structure). LSTM solves this problem by maintaining separate short-term and long-term states. 

**GRU cells** are an optimized version of LSTM cells.

Just like CNN, RNN are also resource heavy, and you need good machines to run them.

## Transfer Learning

Predefined models are available for general DL use cases. For eg., the given TransferLearning python notebook shows how using ResNet50 model, we can identify objects in a given image. Give any unseen image to the model (like fighterjet.jpg in the images folder) and see the model identify objects in the image.
