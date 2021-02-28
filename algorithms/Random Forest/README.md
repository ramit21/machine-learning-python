# machine-learning-python

## Random Forest

Type of Supervised Classification (RandomForestClassifier)/ Regression(RandomForestRegressor).

Multiple decision trees are created as part of training. The output of these decesion trees which is in majority (for the given input) decides which tree will be selected as the final decision.

A simple decision tree works on Greedy algorithm, ie at every step it takes a decision that reduces entropy. But decision trees can lead to overfitting. That's where random forests help by creating multiple decision trees and then vote on the final outcome. This combining of results and then voting for final answer is an example of **ensemble learning**. The input data for each decision tree is randomly resampled, this is known as **bagging or aggregating**.

Use cases: Remote sensing, acquiring images of earth surface, Object detection, XBox Kinect.

Q. Why use Random forest? 

Ans. It's meant to work on large set of data, hence produces accurate results. It prevents over-fitting. It helps estimate missing data.


Q. Key advantages of linear models over tree-based ones? 

Ans. 
1. They can extrapolate (e.g. if labels are between 1-5 in train set, tree based model will never predict 10, but linear will)
2. could be used for anomaly detection because of extrapolation.
3. interpretability (yes, tree based models have feature importance, but it's only a proxy, weights in linear model are better)
4. need less data to get good results
5. have strong online learning implementations (Vowpal Wabbit), which is crucial to work with giant datasets with a lot of features (e.g. texts)
6. Random Forest has more probability of overfitting.

## Decision Tree important terms
**Entropy** : It's the measure of randomness or unpredictability in the dataset.

**Information Gain**: It's the measure of decrease in entropy after the dataset is split.

**Leaf Node**: Leaf node carries the classification or the decision.

**Decision Node**: Decision node has 2 or more branches.

**Root Node**: Top most decision node.

## Graphviz
Install graphviz on the system to visualise decision trees.
```
brew install graphviz
```

## XGBoost

eXtreme Gradient boosting trees: It is most effective classification/regression algorithm.

Tree based ensemble learning algorithm based on regularized boosting of attributes (not bagging as with Random forest), which prevents overfitting. Parallel processing. Generally results in deeper, but optimized trees.

Must be installed before use:
```
brew install xgboost
```
It is not just meant for Python, but also has interfaces for others like JVM, R etc, and also has its own CLI.

The hyperparameters must be carefully passed to XGBoost, as these decide how XGBoost algorithm will work. 

## References
https://www.youtube.com/watch?v=eM4uJ6XGnSM

