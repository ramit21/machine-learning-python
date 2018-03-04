#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 20:24:16 2018

@author: ramit21
"""
import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read in the data.
games = pandas.read_csv("games.csv")    
# Print the names of the columns in games.
print(games.columns)

# Make a histogram of all the ratings in the average_rating column.
plt.hist(games["average_rating"])

# Show the plot, and observe that there are lot of entries with 0 avg. rating
plt.show()

#Are there truly so many terrible games that were given a 0 rating? 
#Or is something else happening? We'll need to dive into the data bit more to check on this.

# Print the first row of all the games with zero scores.
# The .iloc method on dataframes allows us to index by position.
print(games[games["average_rating"] == 0].iloc[0])
# Print the first row of all the games with scores greater than 0.
print(games[games["average_rating"] > 0].iloc[0])

#This shows us that the main difference between a game with a 0 rating and a game with a rating above 0 is that the 0 rated game has no reviews. 
#The users_rated column is 0. By filtering out any board games with 0 reviews, we can remove much of the noise.

# Remove any rows without user reviews.
games = games[games["users_rated"] > 0]
# Remove any rows with missing values. As most ML algos don't work on missing values
games = games.dropna(axis=0)

#You can furhter cluster your data for analysing your data further (k-means clustering has been used below)
# Initialize the model with 2 parameters -- number of clusters and random state.
kmeans_model = KMeans(n_clusters=5, random_state=1)
# Get only the numeric columns from games.
good_columns = games._get_numeric_data()
# Fit the model using the good columns.
kmeans_model.fit(good_columns)
# Get the cluster assignments.
labels = kmeans_model.labels_

#Currently data has many columns, so we need to reduce the dimensionality of our data wihtout loosing too much information
#Using PCA: principal component analysis, we reduce data to 2 columns and then plot it

# Create a PCA model with 2 columns
pca_2 = PCA(2)
# Fit the PCA model on the numeric columns from earlier.
plot_columns = pca_2.fit_transform(good_columns)
# Make a scatter plot of each game, shaded according to cluster assignment.
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
# Show the plot.
plt.show()

#The plot shows us that there are 5 distinct clusters. 
#We could dive more into which games are in each cluster to learn more about what factors cause games to be clustered.

#Now that we want to predict average_rating, let's see what columns might be interesting for our prediction. 
#One way is to find the correlation between average_rating and each of the other columns. 

print(games.corr()["average_rating"])
#We see that the average_weight and id columns correlate best to rating. ids are presumably assigned when the game is added to the database, 
#so this likely indicates that games created later score higher in the ratings. 
#Maybe reviewers were not as nice in the early days of BoardGameGeek, or older games were of lower quality.

#Picking predictor columns:::
#We'll want to remove certain columns that aren't numeric. 
#We'll also want to remove columns that can only be computed if you already know the average rating. 
#Including these columns will destroy the purpose of the classifier, which is to predict the rating without
# any previous knowledge. Using columns that can only be computed with knowledge of the target can lead to OVERFITTING, 
# where your model is good in a training set, but doesn't generalize well to future data.
#The bayes_average_rating column appears to be derived from average_rating in some way, so let's remove it.

# Get all the columns from the dataframe.
columns = games.columns.tolist()
# Filter the columns to remove ones we don't want.
columns = [c for c in columns if c not in ["bayes_average_rating", "average_rating", "type", "name"]]

# Store the variable we'll be predicting on.
target = "average_rating"

#Splitting into train and test sets
#If your error looks surprisingly low when you're training a machine learning algorithm, you should always check to see if you're overfitting.
#In order to prevent overfitting, we'll train our algorithm on a set consisting of 80% of the data, and test it on another set consisting of 20% of the data.

# Generate the training set. Set random_state to be able to replicate results.
train = games.sample(frac=0.8, random_state=1)
# Select anything not in the training set and put it in the testing set.
test = games.loc[~games.index.isin(train.index)]
# Print the shapes of both sets.
print(train.shape)
print(test.shape)

#Fitting a linear regression:::
#Linear regression is a powerful and commonly used machine learning algorithm. 
#It predicts the target variable using linear combinations of the predictor variables. 
#Let's say we have a 2 values, 3, and 4. A linear combination would be 3 * .5 + 4 * .5. A linear combination involves multiplying each number by a constant, and adding the results.

#Linear regression works well only when the predictor variables and the target variable are linearly correlated.
# For other scnearios, some other algorithm like Random forest can be used

# Initialize the model class.
model = LinearRegression()
# Fit the model to the training data.
model.fit(train[columns], train[target])

# Generate our predictions for the test set.
predictions = model.predict(test[columns])

print(":::::: Prediction vs Target ::::::")
for p,t in zip(predictions,test[target]):
    print(p,t)

# Compute error between our test predictions and the actual values.
print(':::::: ERROR = ' + str(mean_squared_error(predictions, test[target])))

