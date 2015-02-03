Title: QuickTip: Utilizing Machine Learning Methods to Identify Important Variables
Date: 2015-02-03
Tags: "scientific writing", "R", "QuickTip"
Slug: machine_learning_methods_to_identify_important_variables
Authors: Hinrich B. Winther
#Status: draft
#Summary: 
#Modified: 

> Machine Learning is the field of scientific study that concentrates on induction algorithms and on other algorithms that can be said to “learn.” [@_glossary_1998]

In order to identify important variables in a multivariate dataset one can utilize machine learning methods. There are many different machine learning algorithms for different tasks. One common task is to decide if a feature vector belongs to a certain class. This can be done with a random forest [@breiman_random_2001] classifier. In order to do so, one has to train the classifier with training data first. Then the classifier can be used to predict the class of other feature vectors. For demonstration purposes we will use the [iris data set]. The following R code loads the "randomForest" library and trains a classifier (forest) with the iris data set. The "Species" column is set as the training label.


```R
> library(randomForest)
> forest = randomForest(Species~., data=iris, importance=TRUE)
> 
> forest

Call:
 randomForest(formula = Species ~ ., data = iris, importance = TRUE) 
               Type of random forest: classification
                     Number of trees: 500
No. of variables tried at each split: 2

        OOB estimate of  error rate: 4.67%
Confusion matrix:
           setosa versicolor virginica class.error
setosa         50          0         0        0.00
versicolor      0         47         3        0.06
virginica       0          4        46        0.08
```


In this example the classifier achieves an out-of-bag (oob) error rate of 4.67%. There is no need for other tests, such as cross-validation, to get an unbiased estimate of the test set error as each tree is created with a different bootstrap sample [@breiman_random_2001].

The classifier saves information on feature importance ("importance=TRUE"). We can use this information in order to identify potentially import variables in the data set. The following R code extracts this information from the classifier and visualizes the data using ggplot2.


```R
> library(ggplot2)
> forest.importance = as.data.frame(importance(forest, scale=FALSE))
> forest.importance = forest.importance[,1:(ncol(forest.importance)-2)]
> forest.importance$mean = rowMeans(forest.importance)
>
> forest.importance
```


| feature     | setosa| versicolor| virginica|  mean|
|:------------|------:|----------:|---------:|-----:|
|Sepal.Length |  0.031|      0.025|     0.046| 0.034|
|Sepal.Width  |  0.008|      0.003|     0.011| 0.007|
|Petal.Length |  0.349|      0.322|     0.324| 0.332|
|Petal.Width  |  0.305|      0.289|     0.267| 0.287|

: Table 1: Feature importance table with calculated mean column.



```R
ggplot(forest.importance, aes(x=row.names(forest.importance), y=mean)) +
  ylab('mean relative feature importance') +
  xlab('feature') +
  geom_bar(stat='identity')
```

![Figure 1: Mean relative feature importance learned by a random forest classifier on the iris data set.]({filename}/images/R/ml_mean_relative_feature_importance.svg)



References
----------

[iris data set]: https://stat.ethz.ch/R-manual/R-patched/library/datasets/html/iris.html
