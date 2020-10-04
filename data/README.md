# Data

Machine learning is mainly about understanding the data. One has to spend most of the time to understand and clean the data than applying machine learning algorithms on top of it.

## Types of data

1. **Numerical**: Discrete values. eg stock prices, age, time to do X etc.
2. **Categorical**: eg. Gender, Yes/No (0/1). Numbers used here are only for categorisation, and dont have any mathermatical meaning.
3. **Ordinal**: Data in order. It's basically a categorical data that has mathermatical meaning as well. Eg. Rank of students, 1,2,3,4,5; or movie ratings etc.

--------

**Q.** When is median prefered over mean?
**A.** When we have outliers (eg. a billionare among the salary of middle class population) in the data that skews the mean towards one end.

**Q.** When to use mode?
**A.** For discrete data, and not for continuous data.

-------

**Variance**: Sigma square: Average of squared differences from the mean. It measures how much spread the data has.

**Standard Deviation**: Sigma: Square root of Vairance. It signifies how much of an outlier a data point is from the mean. Data points that lie more than one standard deviation from the mean can be considered unusual.

------

**Probability Distribution Function:** Probability of one data on a continious data is very very small. Hence we use probability distribution function for ranges of data.

**Probability Mass Function:** Probabilities of discrete data.

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

**K-fold Cross Validation**: Supervised learning technique, where you split data into 1 test set, and k-1 train sets. You apply your model on the k-1 train tests and the compare the result of each with the 1 test set.

-----

### Data warehousing

Few relavant terms:

**Data Warehouse:** is a large central database that contains information from many sources. Queried via SQL or tools like Tableau. Feeding continous data, normalisation and scaling are some of the challenges with data warehouse.

**Data Mart:** A data mart is a simple form of a data warehouse focused on a specific functional area or subject matter and contains copies of a subset of data in the data warehouse. For example, you can have specific data marts for each division in your organization or segment data marts based on regions. You can build data marts from a large data warehouse, operational stores, or a hybrid of the two. Data marts are simple to design, build, and administer. However, because data marts are focused on specific functional areas, querying across functional areas can become complex because of the data distribution. 

**Data Lake:** can have unstructured data, whereas Data wahrehouse is highly structured data.

**ETL vs ELT**: Extract Transform Load vs Extract Load Transform. ETL may not be possible with big data, as the transform step can become problematic. So ELT basically means, that you load all data and then apply transform on it. For ELT systems, you may use distributed DBs (like hive or nosql) instead of traditional Oracle DB. And then use the power of Hadoop to transform the data in-place.




