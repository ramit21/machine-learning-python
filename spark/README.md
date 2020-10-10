# Apache-Spark

When the data set is huge, a ML algorithm running on a single machine may not be a efficient solution. Add to it the fact the numpy can handle data only upto a limit, and doesn't support scaling either. In comes spark to the rescue. Spark under the hood distributes processing among the cluster of machines, hence you can apply ML on large datasets. 

## Installation (macos) and Execution

1. > brew install apache-spark

2. Create a log4j.properties file via

> cd /usr/local/Cellar/apache-spark/2.0.0/libexec/conf (substitute 2.0.0 for the version actually installed)

> cp log4j.properties.template log4j.properties

3. Edit the log4j.properties file and change the log level from INFO to ERROR on log4j.rootCategory.

4. To test installation, open terminal on a folder that contains some data file, and run the following commands:

```
> pyspark

Now you should get a >>> prompt. Next:

>>> rdd = sc.textFile("sometext file name")
>>> rdd.count()   # this will give you count of no. of lines in that file.
>>> quit()        # to quit the spark prompt
```

5. Run the sample .py codes inside the spark folder, using the following commands
```
> spark-submit SparkDecisionTree.py
> spark-submit SparkKMeans.py
> spark-submit TF-IDF.py
```

## What is Spark?

Spark is a fast and general engine for large-scale data processing. It is a scalable solution, where a cluster manager coordinates executor cache tasks. It is much faster than Hadoop MapReduce. Spark supports Python, Java and Scala as programming languages. 

Components of Spark:

1. Spark Streaming: Process data in real time.
2. Spark SQL: Treat data as SQL database and issue SQL queries.
3. GraphX: Treat data as a graph (think like a graph database)
4. **MLLib**: For machine learning. All ML features supported like feature extraction, liniar/logistic regression, Support Vector Machines, PCA, K-Means, Decision Trees, basic statistics like correlation and variance, Recommendations using **Alternating Least Squares**. MLLib also provides special data types like Vector (dense and sparse), LabeledPoint, Rating.

Spark shell creates a "sc" object, which you can use in the code to create a context from underlying hive-db, JDBC, Cassandra, Elasticsearch, flat-files etc.

**RDD**: Resilient Distributed Dataset. It is the fundamental object used in spark to load and transform data. RDD transformations include map, flatmap, filter, distinct, sample, union, subtract etc. RDD actions include collect, count, countByValue, take, reduce, top etc. Many RDD methods accept lambda functions as a parameter. Spark does lazy evaluation, ie. it performs computations only when some action method is called.   

Spark also provides dataframes, which are kind of next level of RDDs with more functionalities. While RDDs contain unstructured data, dataframes have defined schema. For most of the use cases, RDDs are good enough to be used, and should be the first priority.




