# machine-learning-python

## kNN - k Nearest Neighbours

Supervised Algortihm used for both Classifiction and Regression, but mainly for Classification.

Given some training vectors (features), kNN identifies k nearest neighbours of given vector C (whos class needs to be identified), regardless of labels. It then assigns the class that is in majority among the k neighbours as the class of C. 

When used as Regression algorithm, it finds K closest points to a sample and return the average value.

Euclidean Distance [ sqrt((pow(x1-x2),2), (pow(y1-y2),2))] is used to find the nearest distance from the target (x1,y1)

Always choose an odd value of k to avoid ambuigity among equal no. of neighbouring classes.

Optimal value of k can be found using the elbow method: plot the error rates against the chosen k values(for some range say 1-40), and choose the k after which the variation in the error stabilizes.

sklearn provides StandardScaler which can be used to scale the features before applying KNN on them.

Example use case: Recommending products (similar products or frequently brought together) on eComm website, videos on Netflix etc.

------------
See the example on how we plot the error rates for different values of k (elbow method) and choose the optimal value of k for our model.


## References
https://www.youtube.com/watch?v=UqYde-LULfs
https://www.youtube.com/watch?v=6kZ-OPLNcgE
https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/

