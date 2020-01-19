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
- Plotly

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

**Statistics**

| Statistic              | Data Type               | Description                                                                                                     |
|:-----------------------|:-----------------------:|:----------------------------------------------------------------------------------------------------------------|
| **χ<sup>2</sup>**      | Categorical-Categorical | Creates a dataframe with the χ<sup>2</sup> stats., p-values, & degrees of freedom for two categorical variables |
| **Pearson's r**        | Numeric-Numeric         | Creates a dataframe with the Pearson's r coefs. and p-values for two numeric variables                          |
| **Point Biserial r**   | Binary-Numeric          | Creates a dataframe with the point biserial r coefs. and p-values for binary & numeric variables                |


-----

## Contributions

Pull requests are welcome, but for any major issues please open an issue first to discuss what needs to be changed.

-----

## Road Map

- Plotly scientific & statistical functions
    - Caveat: Plotly graphs _cannot_ be displayed in GitHub, but they can be viewed either in [nbviewer](https://nbviewer.jupyter.org/github/a-bergman/Easy-Graphing/blob/master/Examples/Example%20Charts.ipynb) or if Jupyter notebooks are downloaded and distributed as .html files.

- Bokeh Interactive functions

-----

## Project Status

Work is ongoing: I add or modify code as needed.

I finished building out a module of supplemental classification, regression metrics, and an improved confusion matrix.  I moved the `roc_curve`, `prc_curve`, and `residualplots` to that module.  At some point further down the line, those evaluation functions will be translated into Plotly code as well.

## Latest Updates

**`graphs.py`**

1/17/2019:

- Moved `prc_curve`, `roc_curve`, and `residualplots` to `model_evaluation.ipynb`

**`plotly_graphs.py`**

1/2/2020:

- Added `heatmap`

**`model_evaluation.py`**

1/19/2019:

- Added `pearsonr_dataframe` and updated all statistical functions to include `columns` as an argument