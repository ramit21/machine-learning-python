# machine-learning-python

## Liniar Regression

It's a type of Supervised Regression ML model.

target is linearly (directly or inversely) related to the features.

i.e. target = ax + by + c

How much the target is related to a feature (x or y as above) is determined by 
their coefficients (a and b respectively).

A negative coefficient would mean inverse relation with the feature.

Linear regression algorithm works by minimizing the least squares error to fit the data into the model.

r-squared is used to identify how well linear regression has worked. Ranges from 0-1. 0 is bad, means none of variance has been captured, whereas 1 means all of the variance has been captured.

You can also use polynomial regression, but a higher degree can lead to overfitting. A model that is built on an overfitted data will do a terrible job at prediciting values.

------------------------

See App vs website eg. where we plot the avg spending (target value) against all other features, and note the coeffiecients to decide which features contribute more to the earnings (target value)
