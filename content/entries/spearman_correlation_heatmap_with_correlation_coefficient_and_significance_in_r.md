Title: Spearman Correlation Heatmap with Correlation Coefficient and Significance in R
Date: 2014-06-23
Tags: "scientific writing", "R"
Slug: spearman_correlation_heatmap_with_correlation_coefficient_and_significance_in_r
Author: Hinrich B. Winther
Summary: This is a template for future articles.
Modified: 
Modified: 
Status: draft



![Figure 1: ](/images/R/spearman_correlation_heatmap_mtcars.svg)

In a recent paper [@citation] we included data from a survey we conducted. During the publication process, one of the reviewers asked for a more in depth statistical analysis of the data set. He explicitly expressed an interest in correlating the variables in order to spot any interesting correlations. This posed a number of problems:

  1. The data set has 35 variables. This translates into a huge correlation matrix.
  
  2. There are many ways to correlate variables. In my field the [Pearson product-moment correlation coefficient (Pearson's r)][Pearson] and the [Spearman's rank correlation coefficient (Spearman's rho)][Spearman] are the most common ones. Which one should I choose and why?
  
  3. Correlations by themselves are not very useful. You, most likely, want to have information about the statistical significance of the correlation.
  
  4. A correlation is a dimensionless quantity. When can it be regarded as a strong or weak correlation?


### Choosing a Correlation Algorythm

As most papers in my field use either Pearson's r or Spearman's rho I began my research there. As it turns out, there are two types of algorithms: parametric and non-parametric. Parametric algorithms depend on some assumptions about the data set. In case of Pearson's r you need to know about the distribution, scaling and dependency of the variables of the data set.

Spearman's rho, on the other hand, is a non-parametric algorithm. It compares two ranked variables of either [ordinal, interval or ratio][Level of measurement] type and describes how well they can be described using a monotonic function. No further assumptions on the data set are necessary which is handy if you do not know too much about the distribution of your data.


### The Data Set

For the sake of demonstration we will use the [mtcars][mtcars] data set, provided by the stats package. It consists of 11 variables with 32 observations:

|                    |  mpg| cyl|  disp|  hp| drat|    wt|  qsec| vs| am| gear| carb|
|:-------------------|----:|---:|-----:|---:|----:|-----:|-----:|--:|--:|----:|----:|
|Mazda RX4           | 21.0|   6| 160.0| 110| 3.90| 2.620| 16.46|  0|  1|    4|    4|
|Mazda RX4 Wag       | 21.0|   6| 160.0| 110| 3.90| 2.875| 17.02|  0|  1|    4|    4|
|Datsun 710          | 22.8|   4| 108.0|  93| 3.85| 2.320| 18.61|  1|  1|    4|    1|
|Hornet 4 Drive      | 21.4|   6| 258.0| 110| 3.08| 3.215| 19.44|  1|  0|    3|    1|
|Hornet Sportabout   | 18.7|   8| 360.0| 175| 3.15| 3.440| 17.02|  0|  0|    3|    2|

Table 1: The first five (of 32) observations of the mtcars data set.


| axis  | description                              |
|:------|:-----------------------------------------|
|mpg    | Miles/(US) gallon                        |
|cyl    | Number of cylinders                      |
|disp   | Displacement (cu.in.)                    |
|hp     | Gross horsepower                         |
|drat   | Rear axle ratio                          |
|wt     | Weight (lb/1000)                         |
|qsec   | 1/4 mile time                            |
|vs     | V/S                                      |
|am     | Transmission (0 = automatic, 1 = manual) |
|gear   | Number of forward gears                  |
|carb   | Number of carburetors                    |

Table 2: Description of the variable labels of the mtcars data set.


### Let's get it on!

ggplot2 is being used for plotting, Hmisc to create a correlation matrix, reshape2 to meld the dataframe as well as stats to provide the mtcars data set:

```R
library(ggplot2)
library(reshape2)
library(Hmisc)
library(stats)
```




  > rcorr Computes a matrix of Pearson's r or Spearman's rho rank correlation coefficients for all possible pairs of columns of a matrix. Missing values are deleted in pairs rather than deleting all rows of x having any missing variables. Ranks are computed using efficient algorithms, using midranks for ties.  
  -- R Documentation / rcorr {Hmisc}

The Hmisc package for R provides the rcorr function.

```R
library(Hmisc)

d <- read.csv('data/data.csv')

cor(d, use='pairwise.complete.obs')
```


References
----------

[Pearson]: http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
[Spearman]: http://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
[Level of measurement]: http://en.wikipedia.org/wiki/Level_of_measurement
[mtcars]: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html
