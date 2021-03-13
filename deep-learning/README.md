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

**Perceptron**: A Layer of LTUs. A perceptron works by rewarding (increasing) weights that lead to correct behaviour during training. A preceptron is equal to applying activation function on (bias + sum of dot products for weights and Xi). 

**MLP**: Deep Neural Network is basically Multi-layer perceptrons (MLP) with hidden layers. We reduce the no. of neurons as we move from initial layer to the next layers. 

**Transfer Learning**: Predefined models are available for general DL use cases. For eg., the given TransferLearning python notebook shows how using ResNet50 model, we can identify objects in a given image. Give any unseen image to the model (like fighterjet.jpg in the images folder) and see the model identify objects in the image.

## Tuning DL Algortihms

**Gradient-Descent** is a training algorithm for minimizing error over multiple steps. Basically we try different set of parameter values so that the error minimises before rising again. See Images folder for 'ball rolling down the hill' analogy. Beware of local minimas.

**Autodiff** is a calculus trick used internally by most of DL algorithms for optimally finding the gradients in gradient descent.

**Backpropogation**: algorithm used to train MLP's weights by back propagating errors to previous layers. Previous layers will then tweak the weights to reduce the error.

**Activation Functions (aka rectifiers)**: Takes inputs from all neurons from a layer, filters out useful data points, and gives the output to the next layer. This is known as forward propagation. A neural network without an activation function is essentially just a linear regression model. Activation functions are mainly used to introduce non-linearities into the network.

1. **Liniar**: o/p is same as the recieved i/p. Practically, no point in using it.
2. **Binary Step**: It is on or off. But vertical slopes dont work well with calculus. Derivatives are needed for backpropagation. Hence we prefer other options like ReLU.
3. **Softmax** is a function used for classification using probability, for several given input values. Can produce only 1 label as ouput, hence it is mainly used in the final layer of neural networks.
4. **Sigmoid**: While softmax is used for multi-class classification problems, sigmoid function is used for binay classification problems. It changes slowly for high/low values, this is known as "Vanishing Gradient" problem. Solution is to use 'Tanh' instead of signmoid. RNNs do well with Tanh. o/p of singmoid is probability in range of [0,1], while for tanh its [-1,1].
5. **ReLU**: Rectified Liniar Unit. "Dying ReLU problem": when inputs <=0, we have a liniar function. Solution is to use **Leaky ReLU** that introduces a negative slope below 0. Next improved version is **Paramtetric ReLu**, where the slope in negative part is also learned via backpropagation.


## Hyperparameters for tuning DL algorithm

**Learning Rate**: As part of gradient descent, we start at a random point and sample different solutions (weights) to minimise some cost function. How far apart these samples are - is known as learning rate. Small learning rate may take too long to find the optimal solution, and a large learning rate can lead to overshooting the optimal solution.

**Batch size**: Applying differential at every point on loss function is not possible. One way is SGD (Stochatic Gradient descent) that picks some points along the curve, and apply differential. Even better approach is applying differentials on batches. A Batch-size is how many training samples used within each epoch. Small batch-size can wiggle its way out of local minima, while large batch sizes can converge on a wrong solution at random. Hence batch size should be kept small. Just as with learning rate, small batch size may take too long to find the optimal solution, and a large batch size can lead to overshooting the optimal solution.

**Epoch**: No. of iterations algorithm is run for. At each iteration, algorithm tries to reduce the specified **loss/cost function** by backpropagating and adjusting the weights (eg. of loss function = cross_entropy with probability output in range [0,1], and mean square error loss for regression models).

**Optimization Functions**: Used to speed up gradient descent, by speeding up when on a slope, and slowing down when reaching a bottom. **Adam** is a popular choice of optimising function.

## Regularisation

To prevent overfitting. With thousands of weights to tune, overfitting is a problem. Dropout and early stopping are 2 common techniques for regularisation:

1. **Dropout** = Ignore x% of neurons at each stage.
2. **Early-Stopping** = Stop processing input data once performance starts dropping.

## TensorFlow
Library developed by Google used to construct artificial neural networks. Tensorflow can work on any platform, even on a mobile phone. And can also be used to distribute work across GPUs.

Tensorflow is basically used to construct graphs, and then execute those graphs. This feature makes this library useful for deep learning as well (DL was not the goal when the library was built initially).

A **tensor** is an array of values, used to configure the tensorflow execution. Getting these hyperparameters right is mostly what decides the success of DL model. Most of the times, trial and error help find the right solution.

Tensorflow provides matrix multiplication that can be used to mimic a Perceptron (see images).

Note that neural networks can work when the input data is normalized. scikit_learn's StandardScalar can do this for you. 

## Keras

Higher level API for deep learning on top of TensorFlow, available in Tensorflow 1.9+. It integrates well with scikit_learn as well. See the given examples in this project, for the same problem, the code when using Keras is way smaller than using TensorFlow directly.

## CNN - Convolutional Neural Networks

When you want to process data that doesn't neatly align into columns92D data like images). Eg. Finding features within images (eg. stop sign on a road), sentiment analysis etc. CNNs work with overlapping layers of neurons that respond to a particular aspect of data, and feed the output to the next layer (convolution) which process increasingly complex aspect of the data. That's how the visual cortex of the brain works. For eg. an image of a road with stop sign, first set of neurons will process that it is an image, then the next layer will identify that there is a road, the next layer will identify that it has a sign, and then the last layer will process the design/color/shape/text of the sign to say that it is a 'STOP' sign. CNNs are very much resource intensive (CPU, RAM, GPU), but give very high accuracy. Hence used for areas like self driving cars where accuracy is of paramount importance. Getting training data, as well as saving it for CNN is also very hard (think of self driving cars sending real time data).

To do CNN with Keras, see the images folder, and the given python notebook.

## RNN - Recurrent Neural Networks

Used for time series data, ie when you want to predict future behavior based on past data. eg. Stock trades, self driving cars etc. Memory of past data needs to be maintained.

**Memory cell**: Output of one neuron is fed back to the same neuron as well. So over time, past behaviour of neuron influences present behaviour of the neuron.

This backpropagation can be truncated through time by limiting the number of steps going back in.

For RNN topologies, see the images folder.

**LSTM Cell**: Long-Short term memory cell => States from earlier time steps get diluted over time (eg. early words of a sentence can get diluted by the end of a sentence when learning a sentence structure). LSTM solves this problem by maintaining separate short-term and long-term states. 

**GRU cells** are an optimized version of LSTM cells.

Just like CNN, RNN are also resource heavy, and you need good machines to run them.



## References

Play around with below link to see how neural network works to solve a problem:

https://playground.tensorflow.org/
