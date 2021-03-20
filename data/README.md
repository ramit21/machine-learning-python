# Data

Machine learning is mainly about understanding the data. One has to spend most of the time to understand and clean the data than applying machine learning algorithms on top of it.

## EDA
An important part of Data Science is getting to know your data, this is done by Exploratory Data Analysis. EDA gives us insights into data by the means of different statistical and visualisation techniques. Python libraries seaborn & matplotlib help in doing EDA. 


## Types of data

1. **Numerical**: Discrete values. eg stock prices, age, time to do X etc.
2. **Categorical**: eg. Gender, Yes/No (0/1). Numbers used here are only for categorisation, and dont have any mathematical meaning.
3. **Ordinal**: Data in order. It's basically a categorical data that has mathermatical meaning as well. Eg. Rank of students, 1,2,3,4,5; or movie ratings etc.

--------
Few Questions:

**Q.** When is median prefered over mean?

**A.** When we have outliers (eg. a billionare among the salary of middle class population) in the data that skews the mean towards one end.

**Q.** When to use mode?

**A.** For discrete data, and not for continuous data. Mode basically finds out frequency of all data points, and returns the one with maximum frequency.

**Q.** How to fill missing data in your data set?

**A.** This is called as 'imputing' missing data. You can use mean of that feature. In case of outliers, either drop them, or use median in place of mean. But this won't cover co-relation of the column with other columns (if there exists one). So consider using Ml itself to prepare data for ML! Consider using liniar regression or K means clustering. But this won't help with categorical data. For the latter, use DL. 

-------

**Standard Deviation**: Sigma: Square root of Vairance. It signifies how much of an outlier a data point is from the mean. Data points that lie more than one standard deviation from the mean can be considered unusual.

**Variance**: Sigma square: Average of squared differences from the mean. It measures how much spread the data has. The square here is used to increase the effect of values away from mean, and also to nullify negative values of (x - mean).

Population variance = sum(x - mean)^2/N

Sample Variance = sum(x - mean)^2/(N-1)

------

**Probability Distribution Function:** Probability of one data point on a continious data is very very small. Hence we use probability distribution function for ranges of data.

**Probability Mass Function:** Probabilities of discrete data. eg. Poisson Distribution (plot success and failures under different parameters). Another example is Binomial distribution, which plots yes/no probabilities like flipping a coin over multiple trials. Bernoulli distribution is a special case of binomial with a single trial (n=1)

**Probability Density Function:** A function that represents continuous probability distribution.

Normal distribution is an example of probability density function. It's a bell curve centered around the mean.Values beyond 1 std deviation are considered outliers.


------

**Moments:** Quantitative measures about the shape of probability density function.

1st Moment = Mean

2nd Momemnt = Variance

3rd Moment = Skew = how lopsided a distribution is. A +ve skew would mean that data stretched towards right side.

4th Moment = Kurtosis = how sharp the peak of the distribution is.

--------

**Covariance and Correlation** are used to see how 2 features are related to each other. Covariance of 0 means no relation at all, -ve value means inverse relation. Larger the value, larger the relation. Correlation on the other hand lies in the range of [-1, 1].

-------

**Sampling**

It is the process used in statistical analysis in which a predetermined number of observations are taken from a larger population. The methodology used to sample from a larger population depends on the type of analysis being performed but may include simple random sampling or systematic sampling.

Why do sampling? 
1. the features that are in minority can get lost as noise in the entire data set.
2. Processing the entire dataset can be difficult.

-----
**Some terms:**

**K-fold Cross Validation**: Supervised learning technique, where you split data into 1 test set, and k-1 train sets. You apply your model on the k-1 train tests and the compare the result of each with the 1 test set. This is done to avoid overfitting.

**Bias and Variance**: Bias is how far removed the mean of your predicted values is from the "real" answer. Variance is how scattered your predicted values are from the "real" answer. Low bias and low variance is preferred.

High bias, low variance can lead to underfitting (think of liniar model)

High variance, low bias can lead to overfitting (think of polynomial model)

Another example is KNN, where as value of k increases, bias increases, variance decreases.

A single decision tree is prone to overfitting - high variance. But a random forest decreases that variance.

Error= pow(Bias,2) + Vairance. Final goal is to reduce overall error, and not chose lower bias over vairance or vice versa.

**Unbalanced data:** When one type of data is present in larger proportion as compared to the other data. Particularly important for use cases like fraud detection, where the no. of fraud cases is very rare. Solution to the problem is:
1. **Oversampling:** Duplicate samples from the minority class (SMOTE - Synthetic Minority over sampling TEchnique: Use KNN for better results than just creating naive copies).
2. **Undersampling:** Reduce the samples from the majority class.

**Binning:** Categorization technique where data is clubbed into ranges and then given ordinal no. Eg. binning the range of ages (1-10, 11-20, ..etc).

**Transforming**: Apply some function to make data more usable for the model. Eg. aaply log on an exponential data.


-------

### Data warehousing

Few relavant terms:

**Data Warehouse:** is a large central database that contains information from many sources. Queried via SQL or tools like Tableau. Feeding continous data, normalisation and scaling are some of the challenges with data warehouse.

**Data Mart:** A data mart is a simple form of a data warehouse focused on a specific functional area or subject matter and contains copies of a subset of data in the data warehouse. For example, you can have specific data marts for each division in your organization or segment data marts based on regions. You can build data marts from a large data warehouse, operational stores, or a hybrid of the two. Data marts are simple to design, build, and administer. However, because data marts are focused on specific functional areas, querying across functional areas can become complex because of the data distribution. 

**Data Lake:** can have unstructured data, whereas Data warehouse is highly structured data.

**ETL vs ELT**: Extract Transform Load vs Extract Load Transform. ETL may not be possible with big data, as the transform step can become problematic. So ELT basically means, that you load all data and then apply transform on it. For ELT systems, you may use distributed DBs (like hive or nosql) instead of traditional Oracle DB. And then use the power of Hadoop to transform the data in-place.


### Evaluating a model

**RMSE** Root mean squared error gives the accuracy measurement.

**Confusion Matrix**: Matrix that shows probailities of true positives, true negatives, false positives and false negatives. For eg. if you are running an experiment on vaccine testing, you would want a very very low score of false postivies; while in a fraud detection, you would want a very low score of false negatives.

In a good model, the main diagonal (true positive/true negatives) should have most of the probabilities.
```
|              |Actual Yes   | Actual No  |
|Predicted Yes |TP           | FP         |
|Predicted No  |FN           | TN         |
```
(TP: True Positives, FN: False Negatives, FP: False Positives, TN: True Negatives)

**Classifier metrics** (derived from confusion matrix):

1. **Recall** = TP/ (TP+FN)

aka Sensitivity/Completeness/possitivity rate. Good choice of metric when you care a lot about false negatives.

2. **Precision** = TP/(TP+FP)
aka correct Positives. Good choice of metric when you care a lot about false positives.  

3. **Specificity** = TN/(TN+FP). aka True Negative Rate. 

4. **F1 Score** = 2 X (Precision X Recall) / (Precision + Recall)

Harmonic mean of precision and recall. Use it when you care about both precision and recall.

5. **ROC Curve** = Receiver Operating Characteristic Curve = plot of true +ve rate (recall) vs false +ve rate at various threshold settings. The more the curve is bent towards upper left corner, the better. Ideal data would be a dot in the upper left corner.

6. **AUC** = Area under the curve = area under the ROC curve.AUC of 0.5 means useless model, and 1 means perfect. Commonly used metric for comparing classifiers.