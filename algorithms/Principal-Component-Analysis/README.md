# PCA- Principal Component Analysis

If you have multiple features in your model, then visualising all of them becomes difficult. Human brain can understand upto 3 dimensions and when plotting graphs, 2-D is the best option. Hence use PCA to reduce the features before fitting into our model. PCA itself works on unsupervised ML principles when making sense of the features before reducing them.

Before applying PCA, you may also consider scaling the feature values. For eg., a set of ages, and a set of salaries will have completely different scale of values. Hence they must be scaled so that they become comparable before applying PCA, else the PCA will ignore small age values as compared to much larger salary values. See the eg. python notebook for more details.