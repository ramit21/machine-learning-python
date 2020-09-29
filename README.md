# machine-learning-python

## Artificial Intelligence vs Machine Learning vs Deep Learning

AI: Incorporating human intelligence to machines.

ML: Subset of AI. Empowering computer systems with the ability to “learn”.

DL: Subset of ML. DL algorithms are roughly inspired by the information processing patterns found in the human brain. Large quantity of data is continuously fed to Neural networks which then tries to learn from the data and compare with its understanding of data fed so far.

### ML Ecosystem:
1. **Supervised Learning**: Task driven. classification/Regression. This approach works if we have a data set that includes the target values (the values we wish to predict). We try to learn a function that correctly predict the target values from the other features,. eg. Weather forecast, Market forecast, Population growth prediction, Diagnostics, Image procesisng etc.
2. **Unsupervised Learning**: means we have a dataset but there is no target to be predicted. Rather, machine learns by finding structures in the data. Classification: 
2.1. Clustering (eg. density estimation, shopping history categorisation, noise reduction) and 
2.2. Association (eg. people who buy A, also buy B).
3. **Reinforced Learning**: is a setting where we have a sequential decision problem. Making a decision now influences what decisions we can make in the future. eg. Realtime decisions, Robot navigation, Self driving cars, Game AI.

### Supervised ML Models:
1. **Regression**: is used to predict continuous values. 
Example: I have a house with W rooms, X bathrooms, Y square-footage and Z lot-size. Based on other houses in the area that have recently sold, how much (dollar amount) can I sell my house for? 
2. **Classification**: is used to predict which class a data point is part of (discrete value).  
Example: I have an unknown fruit that is yellow in color, 5.5 inches long, diameter of an inch, and density of X. What fruit is this? I would use classification for this kind of problem to classify it as a banana (as opposed to an apple or orange). 

### 7 Steps of Machine learning

1. Gather data
2. Data preperation
3. Choose a model
4. Train
5. Evaluation
6. Paramater tuning
7. Prediction

See ml.py example covering above steps in details.

### Sampling 
It is the process used in statistical analysis in which a predetermined number of observations are taken from a larger population. The methodology used to sample from a larger population depends on the type of analysis being performed but may include simple random sampling or systematic sampling.

Why do sampling? 
1. the features that are in minority can get lost as noise in the entire data set.
2. Processing the entire dataset can be difficult.


### ML in Python

Python has an amazing ecosystem of libraries that make machine learning easy to get started with: Scikit-learn, Pandas, and Matplotlib libraries.

Pickle library is used to serialize a tried and tested model (which can then be saved as a binary file) for later use.

sklearn.metrics provides confusion_matrix and classification_report to evaluate the model.

sklearn.datasets provides sample data sets to try various analysis and ML algorithms.

MatplotLib and Seaborn (built on top of Matplotlib)are used for plotting various graphsfor analyzing the data.

Various ML algoritmhs have been covered under the algorithms folder of this POC. These are Jupyter notebooks. Run Anaconda -> Jupyter -> select the .ipynb. Jupyter shortcuts:

1. ctrl+Enter: runs teh set of commands
2. alt+enterL runs teh set of commands, and inserts a new box below for the next set of commands.

### References
https://www.geeksforgeeks.org/machine-learning/
https://www.dataquest.io/blog/machine-learning-python/  
https://towardsdatascience.com/the-7-steps-of-machine-learning-2877d7e5548e  
https://www.forbes.com/sites/bernardmarr/2016/12/08/what-is-the-difference-between-deep-learning-machine-learning-and-ai/#13473ee326cf

