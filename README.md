# Easy Graphing

A basic wrapper for Seaborn that has functions to create graphs and control their appearance.

-----

# Motivation

When performing EDA in a Jupyter notebook, I found myself making the same types of graphs over and over.  I wondered how I could make it easier for myself to plot these graphs and how I could make the functions more dynamic.

-----

# Dependencies

For these functions to run properly, you should have the following installed:

- Seaborn
- Matplotlib.pyplot
- Numpy
- Scikit-learn

-----

# Contents

There are two sets of graphs included in the .py file: graphs for EDA and graphs for model evaluation.

For EDA:

| Plot Type     | Numeric Data | Categorical Data | Description                                                       |
|:--------------|:------------:|:----------------:|:------------------------------------------------------------------|
| Bar Plots     |              | ✓                | Takes a numeric variable and plots the corresponding measure of central tendency for a categorical column |
| Box Plots     | ✓            | ✓               | Plots a box & whiskers plot for a numeric variable                 |
| Count Plots   | ✓            | ✓               | Counts how many times a category appears in a categorical variable |
| Heat Maps     | ✓            |                  | Creates a heat map of numeric variable correlations               |
| Histograms    | ✓            |                  | Plots histograms for a continuous variable                        |                      
| KDE Plots     | ✓            |                  | Plots a kernel density estimate for a numeric variable            |
| Scatter Plots | ✓            |                  | Plots two numeric variables against each other                    |
| Violin Plots  | ✓            | ✓               | Plots a density estimate on top of a box plot                     |

For Model Evaluation:

| Plot Type      | Numeric Data | Categorical Data | Description                                        |
|:---------------|:------------:|:----------------:|:---------------------------------------------------|
| Residual Plots | ✓            |                  | Plots regression residuals on the true values      |
| ROC Curves     |              | ✓                | Plots an ROC curve with a AUROC score in the title |

-----

# Contributions

Pull requests are welcome, but for any major issues please open an issue first to discuss what needs to be changed.

-----

# Road Map

- Plotly scientific and statistical functions
- Bokeh Interactive functions

-----

# Project Status

Work is ongoing and I add or modify code as needed. 