# machine-learning-python

## k-Means

It's a type of Unsupervised Classification ML model, used when you have unlabeled data (i.e., data without defined categories or groups). The goal of this algorithm is to find groups in the data, with the number of groups represented by the variable K. The algorithm randomly assigns each observation to a cluster, and finds the centroid of each cluster. Then, the algorithm iterates through two steps: Reassign data points to the cluster whose centroid is closest. Calculate new centroid of each cluster. These two steps are repeated till the within cluster variation cannot be reduced any further. The within cluster variation is calculated as the sum of the euclidean distance between the data points and their respective cluster centroids. Data points are clustered based on feature similarity. The results of the K-means clustering algorithm are:
1. The centroids of the K clusters, which can be used to label new data
2. Labels for the training data (each data point is assigned to a single cluster)

Optimal value of k can be found using the elbow method: plot the Avg. Within cluster distances to centroids against the chosen k values(for some range say 1-40), and choose the k after which the variation in the error stabilizes.

Example use cases: Segment by purchase history, Segment by activities on application/website/platform, Identify groups in health monitoring etc.

## References
https://www.datascience.com/blog/k-means-clustering

