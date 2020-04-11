# Easy Graphing

A basic wrapper for Seaborn that has functions to create graphs and control their appearance.

-----

## Motivation

When performing EDA in a Jupyter notebook, I found myself making the same types of graphs over and over.  I wondered how I could make it easier for myself to plot these graphs and how I could make the functions more dynamic.

-----

## Dependencies

For these functions to run properly, you should have the following installed:

- Seaborn
- Matplotlib.pyplot
- Numpy
- Scikit-learn
- Statsmodels
- [Plotly](https://plotly.com/python/)
- [Mlxtend](http://rasbt.github.io/mlxtend/)

-----

### `graphs` Contents

There are two sets of graphs included in the .py file: graphs for EDA and graphs for model evaluation.

**For EDA**:

| Plot Type         | Numeric Data | Categorical Data | Description                                                                                               |
|:------------------|:------------:|:----------------:|:----------------------------------------------------------------------------------------------------------|
| **Bar Plots**     |              | ✓                | Takes a numeric variable and plots the corresponding measure of central tendency for a categorical column |
| **Box Plots**     | ✓            | ✓               | Plots a box & whiskers plot for a numeric variable                                                         |
| **Count Plots**   | ✓            | ✓               | Counts how many times a category appears in a categorical variable                                         |
| **Heat Maps**     | ✓            |                  | Creates a heat map of numeric variable correlations                                                       |
| **Histograms**    | ✓            |                  | Plots histograms for a numeric variable                                                                   |  
| **2D Histograms** | ✓            |                  | Plots two continuous variables (best for large datasets)                                                  |  
| **KDE Plots**     | ✓            |                  | Plots a kernel density estimate for a numeric variable                                                    |
| **Scatter Plots** | ✓            |                  | Plots two numeric variables against each other                                                            |
| **Violin Plots**  | ✓            | ✓               | Plots a density estimate on top of a box plot                                                              |

-----

### `plotly_graphs` Contents

**For EDA**:

| Plot Type            | Numeric Data | Categorical Data | Description                                                      |
|:---------------------|:------------:|:----------------:|:-----------------------------------------------------------------|
| **2D Histogram**     | ✓            |                  | Plots two numeric variables (best for large datasets)            |
| **Bar Chart**        |              | ✓                | Plots the frequency of a categorical variable                    |
| **Box plot**         | ✓            |                  | Plots a box & whiskers plot for a numeric variable               |
| **Double Histogram** | ✓            |                  | Plots 2 stacked or overlain histograms                           |
| **Heatmap**          | ✓            |                  | Plots a heatmap for numeric data                                 |
| **Histogram**        | ✓            |                  | Plots a histogram for a numeric variable                         |
| **Scatter Plot**     | ✓            |                  | Plots two numeric variables against each other                   |
| **Violin Plot**      | ✓            |                  | Plots a violin plot for a numeric variable                       |

**Utilities**:

| Plot Type      | Numeric Data | Categorical Data | Description                                                         |
|:--------------|:------------:|:----------------:|:---------------------------------------------------------------------|
| **Table**     | ✓           | ✓                | Creates a table for whatever data is inputted; best for distribution  |

-----

### `model_evaluation` Contents

**Graphs**

| Plot Type                    | Numeric Data | Categorical Data | Description                                                           |
|:-----------------------------|:------------:|:----------------:|:----------------------------------------------------------------------|
| **Precision-Recall Curve**   |              | ✓                | Plots a precision-recall curve from a model's predicted probabilities |
| **ROC Curve**                |              | ✓                | Plots a ROC curve from a model's predicted probabilities              |
| **Residual Plots**           | ✓            |                  | Plots the residuals from a single or multiple model's probabilities   |


**Metrics**

| Metric                        | Classification | Regression | Description                                                      |
|:------------------------------|:--------------:|:----------:|:-----------------------------------------------------------------|
| **Adjusted R<sup>2</sup>**    |                | ✓          | The R<sup>2</sup> score adjusted for the number of features in X |
| **Negative Predictive Value** | ✓              |            | Percentage of correctly predicted negatives out of all negatives |
| **Specificity**               | ✓              |            | Percentage of correctly predicted negative predictions           |

**Summaries**

| Summary                        | Description                                                                                          |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------|
| **Classification Summary**     | Calculates the recall, specificity, Matthews correlation coefficient, and AUROC score in a dataframe |
| **Confusion Matrix Dataframe** | Converts scikit-learn's `confusion_matrix` into a dataframe                                          |
| **Regression Summary**         | Calculates the RMSE, MAE, R<sup>2</sup>, & Adjusted<sup>2</sup> in a dataframe                       |
| **Scaled Regression Summary**  | Calculates the RMSE, MAE, & R<sup>2</sup> for scaled data in a dataframe                             |

### `stat_functions` Contents

| Statistic                  | Data Type               | Description                                                                                          |
|:---------------------------|:---------------        :| :----------------------------------------------------------------------------------------------------|
| **χ<sup>2</sup>**          | Categorical-Categorical | A dataframe with the χ<sup>2</sup> stats., p-values, & degrees of freedom for 2 variables            |
| **McNemar's Test**         | Classifier - Classifier | A dataframe with McNemar's statistic, p-value, & interpretation of the p-value for 2 classifiers     |
| **McNemar's Dataframe**    | Classifier-Classifier   | A dataframe containing a contingency table for the McNemar's test                                    |
| **Pearson's r**            | Numeric-Numeric         | A dataframe containing the Pearson's r coefs., p-values, & interpretation for numeric variables      |
| **Point Biserial r**       | Binary-Numeric          | A dataframe with the point-biserial r coefs., p-values, & interpreation for numeric & binary variables |
| **Cross-Validated F-Test** | Regressor - Regressor   | A datafrmae with the 5X2 cross-validated F-score, p-value, & interpretation for **two** regressors   |


-----

## Contributions

Pull requests are welcome, but for any major issues please open an issue first to discuss what needs to be changed.

-----

## Road Map

- Bokeh Interactive functions

-----

## Project Status

Work is ongoing: I add or modify code as needed.

I am focusing on statistical functions at the moment, but I am open to adding more visualization functions as well.

## Latest Updates

**`graphs.py`**

1/17/2019:

- Moved `prc_curve`, `roc_curve`, and `residualplots` to `model_evaluation.ipynb`

**`plotly_graphs.py`**

1/2/2020:

- Added `heatmap`

**`model_evaluation.py`**

2/9/2020:

- Changed `y` to `y_true` to fix an error with `specificity` and `negative_predictive_power`

**`stat_functions.py`**

4/3/2020:

- Added `cross_validated_ftest`