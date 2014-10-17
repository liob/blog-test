Title: Spearman Correlation Heatmap with Correlation Coefficient and Significance Levels in R
Date: 2014-10-17
Tags: "scientific writing", "R"
Slug: spearman_correlation_heatmap_with_correlation_coefficient_and_significance_in_r
Authors: Hinrich B. Winther
#Summary: 
Modified: 
Status: draft


![Figure 1: Spearman correlation heatmap with correlation coefficient and significance levels based on the mtcars data set.]({filename}/images/R/spearman_correlation_heatmap_mtcars.svg)

In a recent paper we included data from a survey we conducted. During the publication process, one of the reviewers asked for a more in depth statistical analysis of the data set. He (she?) explicitly expressed a special interest in correlating the variables of the survey in order to spot any interesting correlations. This posed a number of problems:

  1. The data set has 35 variables. This translates into a huge correlation matrix.
  
  2. There are many ways to correlate variables. In my field the [Pearson product-moment correlation coefficient (Pearson's r)][Pearson] and the [Spearman's rank correlation coefficient (Spearman's rho)][Spearman] are the most common ones. Which one should I choose and why?
  
  3. Correlations by themselves are not very useful. You, most likely, want to have at least some information about the statistical significance of the correlation.


### The Data Set

For the sake of demonstration we will use the [mtcars] data set, provided by the [stats] package. The data set includes 11 variables with 32 observations, hence rendering the task a bit more manageable.

|                    |  mpg| cyl|  disp|  hp| drat|    wt|  qsec| vs| am| gear| carb|
|:-------------------|----:|---:|-----:|---:|----:|-----:|-----:|--:|--:|----:|----:|
|Mazda RX4           | 21.0|   6| 160.0| 110| 3.90| 2.620| 16.46|  0|  1|    4|    4|
|Mazda RX4 Wag       | 21.0|   6| 160.0| 110| 3.90| 2.875| 17.02|  0|  1|    4|    4|
|Datsun 710          | 22.8|   4| 108.0|  93| 3.85| 2.320| 18.61|  1|  1|    4|    1|
|Hornet 4 Drive      | 21.4|   6| 258.0| 110| 3.08| 3.215| 19.44|  1|  0|    3|    1|
|Hornet Sportabout   | 18.7|   8| 360.0| 175| 3.15| 3.440| 17.02|  0|  0|    3|    2|

: Table 1: The first five (of 32) observations of the mtcars data set.


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

: Table 2: Description of the variable labels of the mtcars data set.


### Choosing a Suitable Correlation Algorithm

As most papers in my field use either Pearson's r or Spearman's rho I began my research there. As it turns out, there are two types of algorithms: parametric and non-parametric. Parametric algorithms depend on some assumptions about the data set. In case of Pearson's r you need to know about the distribution, scaling and dependency of the variables of the data set.

Spearman's rho, on the other hand, is a non-parametric algorithm. It compares two ranked variables of either [ordinal, interval or ratio][Level of measurement] type and describes how well they can be described using a monotonic function. No further assumptions on the data set are necessary which is handy if you do not know too much about the distribution of your data.


### Let's get it on!

[R], a statistical computing programming language, is being used for the statistical analysis with some additional libraries: [ggplot2] for plotting, [Hmisc] to create a correlation matrix, [reshape2] to meld the dataframe as well as [stats] to provide the [mtcars] data set.

```R
library(ggplot2)
library(reshape2)
library(Hmisc)
library(stats)
```

The first thing is to calculate the correlation of the individual variables to another. As we have our data already in a dataframe, merely a call of the rcorr function of the Hmisc library is necessary. This creates a new list with two entries: ”r” the correlation coefficients and ”P” the significance levels.

  > rcorr Computes a matrix of Pearson's r or Spearman's rho rank correlation coefficients for all possible pairs of columns of a matrix. Missing values are deleted in pairs rather than deleting all rows of x having any missing variables. Ranks are computed using efficient algorithms, using midranks for ties.  
  -- R Documentation / rcorr {Hmisc}

```R
d <- mtcars
cormatrix = rcorr(as.matrix(d), type='spearman')
```

|     |   mpg|   cyl|  disp|    hp|  drat|    wt|  qsec|    vs|    am|  gear|  carb|
|:----|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
|mpg  |  1.00| -0.91| -0.91| -0.89|  0.65| -0.89|  0.47|  0.71|  0.56|  0.54| -0.66|
|cyl  | -0.91|  1.00|  0.93|  0.90| -0.68|  0.86| -0.57| -0.81| -0.52| -0.56|  0.58|
|disp | -0.91|  0.93|  1.00|  0.85| -0.68|  0.90| -0.46| -0.72| -0.62| -0.59|  0.54|
|hp   | -0.89|  0.90|  0.85|  1.00| -0.52|  0.77| -0.67| -0.75| -0.36| -0.33|  0.73|
|drat |  0.65| -0.68| -0.68| -0.52|  1.00| -0.75|  0.09|  0.45|  0.69|  0.74| -0.13|
|wt   | -0.89|  0.86|  0.90|  0.77| -0.75|  1.00| -0.23| -0.59| -0.74| -0.68|  0.50|
|qsec |  0.47| -0.57| -0.46| -0.67|  0.09| -0.23|  1.00|  0.79| -0.20| -0.15| -0.66|
|vs   |  0.71| -0.81| -0.72| -0.75|  0.45| -0.59|  0.79|  1.00|  0.17|  0.28| -0.63|
|am   |  0.56| -0.52| -0.62| -0.36|  0.69| -0.74| -0.20|  0.17|  1.00|  0.81| -0.06|
|gear |  0.54| -0.56| -0.59| -0.33|  0.74| -0.68| -0.15|  0.28|  0.81|  1.00|  0.11|
|carb | -0.66|  0.58|  0.54|  0.73| -0.13|  0.50| -0.66| -0.63| -0.06|  0.11|  1.00|

: Table 3: Resulting correlation matrix - correlation coefficients (cormatrix$r)


|     |  mpg|  cyl| disp|   hp| drat|   wt| qsec|   vs|   am| gear| carb|
|:----|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
|mpg  |   NA| 0.00| 0.00| 0.00| 0.00| 0.00| 0.01| 0.00| 0.00| 0.00| 0.00|
|cyl  | 0.00|   NA| 0.00| 0.00| 0.00| 0.00| 0.00| 0.00| 0.00| 0.00| 0.00|
|disp | 0.00| 0.00|   NA| 0.00| 0.00| 0.00| 0.01| 0.00| 0.00| 0.00| 0.00|
|hp   | 0.00| 0.00| 0.00|   NA| 0.00| 0.00| 0.00| 0.00| 0.04| 0.06| 0.00|
|drat | 0.00| 0.00| 0.00| 0.00|   NA| 0.00| 0.62| 0.01| 0.00| 0.00| 0.49|
|wt   | 0.00| 0.00| 0.00| 0.00| 0.00|   NA| 0.21| 0.00| 0.00| 0.00| 0.00|
|qsec | 0.01| 0.00| 0.01| 0.00| 0.62| 0.21|   NA| 0.00| 0.26| 0.42| 0.00|
|vs   | 0.00| 0.00| 0.00| 0.00| 0.01| 0.00| 0.00|   NA| 0.36| 0.12| 0.00|
|am   | 0.00| 0.00| 0.00| 0.04| 0.00| 0.00| 0.26| 0.36|   NA| 0.00| 0.73|
|gear | 0.00| 0.00| 0.00| 0.06| 0.00| 0.00| 0.42| 0.12| 0.00|   NA| 0.53|
|carb | 0.00| 0.00| 0.00| 0.00| 0.49| 0.00| 0.00| 0.00| 0.73| 0.53|   NA|

: Table 4: Resulting correlation matrix - significance levels (cormatrix$P)

The correlation coefficients can be plotted using a heatmap representation. [ggplot2] provides the [geom_tile] geometric object for this purpose. In order to plot the correlation matrix we need to [meld][Melt] the dataframe first.

```R
cordata = melt(cormatrix$r)
ggplot(cordata, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile() + xlab("") + ylab("")
```

![Figure 2: Spearman correlation heatmap based on the mtcars data set. No information about significance levels is included]({filename}/images/R/spearman_correlation_heatmap_mtcars_bare.svg)

Figure 2 shows the resulting Heatmap, plotted by ggplot2. However, some key data is missing. There is no information about the significance levels nor does the plot include the numeric values of Spearman's rho. In order to efficiently use the little space per tile, I wrote a little function ("abbreviateSTR") which abbreviates the values. The resulting strings are stored in a label column. This column can then be plotted onto the corrosponding tile. To further enhance the distinction between significant (P > 0.05) and insignificant correlations, a red, semi transparent, ”X” is being overlaid onto insignificant tiles. The resulting plot is shown in figure 1.


### Conclusion

By using the non-parametric Spearman algorithm it is possible to create a preliminary overview of the correlations within a data set. This information can be plotted utilizing a heatmap representation in conjunction with significance levels as well as numeric values of Spearman's rho. The resulting plot is a comprehensible representation of the data set, which allows quick identification of significant correlations.

Looking at the heatmap, one could get the impression that the gross horsepower has a strong negative correlation (r ≈ -0.89, P < 0.01) with the gasoline consumption. Who would have thought?


### Complete R Script

```R
#!/usr/bin/env Rscript

library(ggplot2)
library(reshape2)
library(Hmisc)
library(stats)

abbreviateSTR <- function(value, prefix){  # format string more concisely
  lst = c()
  for (item in value) {
    if (is.nan(item) || is.na(item)) { # if item is NaN return empty string
      lst <- c(lst, '')
      next
    }
    item <- round(item, 2) # round to two digits
    if (item == 0) { # if rounding results in 0 clarify
      item = '<.01'
    }
    item <- as.character(item)
    item <- sub("(^[0])+", "", item)    # remove leading 0: 0.05 -> .05
    item <- sub("(^-[0])+", "-", item)  # remove leading -0: -0.05 -> -.05
    lst <- c(lst, paste(prefix, item, sep = ""))
  }
  return(lst)
}

d <- mtcars

cormatrix = rcorr(as.matrix(d), type='spearman')
cordata = melt(cormatrix$r)
cordata$labelr = abbreviateSTR(melt(cormatrix$r)$value, 'r')
cordata$labelP = abbreviateSTR(melt(cormatrix$P)$value, 'P')
cordata$label = paste(cordata$labelr, "\n", 
                      cordata$labelP, sep = "")
cordata$strike = ""
cordata$strike[cormatrix$P > 0.05] = "X"

txtsize <- par('din')[2] / 2
ggplot(cordata, aes(x=Var1, y=Var2, fill=value)) + geom_tile() + 
  theme(axis.text.x = element_text(angle=90, hjust=TRUE)) +
  xlab("") + ylab("") + 
  geom_text(label=cordata$label, size=txtsize) + 
  geom_text(label=cordata$strike, size=txtsize * 4, color="red", alpha=0.4)
```



[geom_tile]: http://docs.ggplot2.org/current/geom_tile.html
[ggplot2]: http://ggplot2.org
[Hmisc]: http://biostat.mc.vanderbilt.edu/wiki/Main/Hmisc
[Melt]: http://www.wekaleamstudios.co.uk/posts/melt/
[Pearson]: http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
[R]: http://www.r-project.org
[reshape2]: https://github.com/hadley/reshape
[Spearman]: http://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
[stats]: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/00Index.html
[Level of measurement]: http://en.wikipedia.org/wiki/Level_of_measurement
[mtcars]: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html
