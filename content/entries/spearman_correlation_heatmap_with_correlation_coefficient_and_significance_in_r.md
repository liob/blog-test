Title: Spearman Correlation Heatmap with Correlation Coefficient and Significance in R
Date: 2014-06-23
Tags: "scientific writing"
Category: "scientific writing"
Slug: spearman_correlation_heatmap_with_correlation_coefficient_and_significance_in_r
Author: Hinrich B. Winther
Summary: This is a template for future articles.
Modified: 
Modified: 
Status: draft


In a recent paper [@citation] we included data from a survey we conducted. During the publication process, one of the reviewers asked for a more in depth statistical analysis of the data set. He explicitly expressed an interest in correlating the variables in order to spot any interesting correlations. This posed a number of problems:

  1. The data set has 35 variables. This translates into a huge correlation matrix.
  
  2. There are many ways to correlate variables. In my field the [Pearson product-moment correlation coefficient (Pearson's r)][Pearson] and the [Spearman's rank correlation coefficient (Spearman's rho)][Spearman] are the most common ones. Which one should I choose and why?
  
  3. Correlations by themself are not very useful. You, most likely, want to have information about the statistical significance of the correlation.
  
  4. A correlation is a dimensionless quantity. When can it be regarded as a strong or weak correlation?


### Choosing a Correlation Algorythm

As most papers in my field use either Pearson's r or Spearman's rho I began my research there. As it turns out, there are two types of algorythms: parametric and non-parametric. Parametric algorythms depend on some assumptions about the data set. In case of Pearson's r you need to know about the distribution, scaling and dependency of the variables of the data set.

Spearman's rho, on the other hand, is a non-parametric algorythm. It compares two ranked variables of either [ordinal, interval or ratio][Level of measurement] type and describes how well they can be described using a monotonic function. No further assumptions on the data set are necessary which is handy if you do not know too much about the distribution of your data.


### Let's get it on!

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
