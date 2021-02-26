# machine-learning-python

AI/ML is no longer an aspirational technology but a necessity. As per Gartner, 75% of all companies trying to implement ML will operationalize their uses cases by 2024.

Various ML algoritmhs have been covered under the algorithms folder of this POC. These are Jupyter notebooks. Run Anaconda -> Jupyter -> select the .ipynb. 

Jupyter shortcuts:
1. ctrl+Enter: runs the set of commands
2. alt+Enter: runs the set of commands, and inserts a new box below for the next set of commands.

## Artificial Intelligence vs Machine Learning vs Deep Learning

AI: Incorporating human-like decision making intelligence to machines. Mainly used in 1950-80 era, and used decision trees and if-then-else analysis.

ML: Subset of AI. Empowering computer systems with the ability to “learn”. Introduced in 1980, used algorithms and regression analysis.

DL: Subset of ML. Introduced in 2010. DL algorithms are roughly inspired by the information processing patterns found in the human brain. Large quantity of data is continuously fed to Neural networks which then tries to learn from the data and compare with its understanding of data fed so far.

AI/ML vs Analytics: AI/ML is for predicting values and future, while analytics is only on present state data. Analytics is to make sense of data before feeding it to ML algorithms.

### ML Ecosystem:

1. **Supervised Learning**: Task driven. classification/Regression. This approach works if we have a data set that includes the target values (the values we wish to predict). We try to learn a function that correctly predict the target values from the other features. We split the data into train and test data. Predicted values are then compared with test data to find error.

eg. Weather forecast, Market forecast, Population growth prediction, Diagnostics, Image procesisng etc. 

2. **Unsupervised Learning**: means we have a dataset but there is no target to be predicted. Rather, machine learns by finding structures in the data. 2 types:

2.1. Clustering (eg. density estimation, shopping history categorisation, noise reduction) 

2.2. Association (eg. people who buy A, also buy B)

3. **Reinforced Learning**: is a setting where we have a sequential decision problem. Making a decision now influences what decisions we can make in the future. eg. Realtime decisions, Robot navigation, Self driving cars, Game AI.

### Supervised ML Models:
1. **Regression**: is used to predict continuous values. 
Example: I have a house with W rooms, X bathrooms, Y square-footage and Z lot-size. Based on other houses in the area that have recently sold, how much (dollar amount) can I sell my house for? 
2. **Classification**: is used to predict which class a data point is part of (discrete value).  
Example: I have an unknown fruit that is yellow in color, 5.5 inches long, diameter of an inch, and density of X. What fruit is this? I would use classification for this kind of problem to classify it as a banana (as opposed to an apple or orange). 

### 7 Steps of Machine learning

1. Gather data
2. **Data preperation** (sampling, fill missing values, drop columns, select relavant features - use PCA if the need be, scaling, convert categorial string data into numeric data, find and remove outliers and erroneuous data)
3. Choose a model
4. Train
5. Evaluation
6. Paramater tuning
7. Prediction

See ml.py example covering above steps in details.

### ML in Python

Python has an amazing ecosystem of libraries that make machine learning easy to get started with: Scikit-learn, Pandas, and Matplotlib libraries.

**Pickle** library is used to serialize a tried and tested model (which can then be saved as a binary file) for later use. For eg, see algorithms->Random forest -> Iris problem. You can then expose your trained model via REST calls which the client can invoke to predict values using the model.

**sklearn.metrics** provides confusion_matrix and classification_report to evaluate the model.

**sklearn.datasets** provides sample data sets to try various analysis and ML algorithms.

**nltk** for natural language processing.

**MatplotLib and Seaborn** are used for plotting various graphs for analyzing the data. Seaborn is basically a wrapper on top of Matplotlib that helps create matplotlib graphs with more aesthetic appeal, and also provides some more graph types. (See data folder for crash course python notebooks on both)

**PCA**(Principal Component Analysis): If you have multiple features in your model, then visualising all of them becomes difficult. Human brain can understand upto 3 dimensions and when plotting graphs, 2-D is the best option. Hence use PCA to reduce the features before fitting into our model. PCA itself works on unsupervised ML principles when making sense of the features before reducing them.

### References
https://sundog-education.com/machine-learning/
https://www.geeksforgeeks.org/machine-learning/
https://www.dataquest.io/blog/machine-learning-python/  
https://towardsdatascience.com/the-7-steps-of-machine-learning-2877d7e5548e  
https://www.forbes.com/sites/bernardmarr/2016/12/08/what-is-the-difference-between-deep-learning-machine-learning-and-ai/#13473ee326cf

