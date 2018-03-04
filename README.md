# machine-learning-python

## Demo for machine learning using Python

Machine learning is a field that uses algorithms to learn from data and make predictions. 
Practically, this means that we can feed data into an algorithm, and use it to make predictions about what might happen
in the future. This has a vast range of applications, from self-driving cars and sattelites/rockets sent on mission,
 to stock price prediction etc.  

Python has an amazing ecosystem of libraries that make machine learning easy to get started with. 
We'll be using the excellent Scikit-learn, Pandas, and Matplotlib libraries in this POC.

### 7 Steps of Machine learning

1. Gather data
2. Data preperation
3. Choose a model
4. Train
5. Evaluation
6. Paramater tuning
7. Prediction

### ML Excercise:

The dataset (games.csv) is from BoardGameGeek(https://www.boardgamegeek.com/), and contains data on 80000 board games.  

The dataset contains several data points about each board game. Here's a list of the interesting ones:  
* name -- name of the board game.  
* playingtime -- the playing time (given by the manufacturer).  
* minplaytime -- the minimum playing time (given by the manufacturer).  
* maxplaytime -- the maximum playing time (given by the manufacturer).  
* minage -- the minimum recommended age to play.  
* users_rated -- the number of users who rated the game.  
* average_rating -- the average rating given to the game by users. (0-10)  
* total_weights -- Number of weights given by users. Weight is a subjective measure that is made up by BoardGameGeek. It's how "deep" or involved a game is.  

ml.py script does the following things on this data:  
* Read the data using Pandas.  
* Plot our target variables to identify noise and accordingly clean our data.  
* Find correlation of other columns wrt the target column.  
* Pick predictor columns from above correlation.  
* Split data into train and test set.  
* Predict target value using a regression algorithm.  
* And finally compute the error between actual values and the predicted values.  


### References

https://www.dataquest.io/blog/machine-learning-python/  
https://towardsdatascience.com/the-7-steps-of-machine-learning-2877d7e5548e  
https://www.forbes.com/sites/bernardmarr/2016/12/08/what-is-the-difference-between-deep-learning-machine-learning-and-ai/#13473ee326cf

