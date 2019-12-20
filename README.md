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
- Plotly

-----

# `graphs` Contents

There are two sets of graphs included in the .py file: graphs for EDA and graphs for model evaluation.

**For EDA**:

| Plot Type     | Numeric Data | Categorical Data | Description                                                       |
|:--------------|:------------:|:----------------:|:------------------------------------------------------------------|
| Bar Plots     |              | ✓                | Takes a numeric variable and plots the corresponding measure of central tendency for a categorical column |
| Box Plots     | ✓            | ✓               | Plots a box & whiskers plot for a numeric variable                 |
| Count Plots   | ✓            | ✓               | Counts how many times a category appears in a categorical variable |
| Heat Maps     | ✓            |                  | Creates a heat map of numeric variable correlations               |
| Histograms    | ✓            |                  | Plots histograms for a continuous variable                        |  
| 2D Histograms | ✓            |                  | Plots two continuous variables (best for large datasets)          |                   
| KDE Plots     | ✓            |                  | Plots a kernel density estimate for a numeric variable            |
| Scatter Plots | ✓            |                  | Plots two numeric variables against each other                    |
| Violin Plots  | ✓            | ✓               | Plots a density estimate on top of a box plot                      |

**For Model Evaluation**:

| Plot Type      | Numeric Data | Categorical Data | Description                                        |
|:---------------|:------------:|:----------------:|:---------------------------------------------------|
| Residual Plots | ✓            |                  | Plots regression residuals on the true values      |
| ROC Curves     |              | ✓                | Plots an ROC curve with a AUROC score in the title |

# `plotly_graphs` Contents

**For EDA**:

| Plot Type     | Numeric Data | Categorical Data | Description                                                       |
|:---------------|:------------:|:----------------:|:-----------------------------------------------------------------|
| 2D Histograms | ✓            |                  | Plots two continuous variables (best for large datasets)          |

**Utilities**:

| Plot Type | Numeric Data | Categorical Data | Description |
|:----------|:------------:|:----------------:|:---------------------------------------------------|
| Table     | ✓           | ✓                | Creates a table for whatever data is inputted; best for distribution      |


-----

# Contributions

Pull requests are welcome, but for any major issues please open an issue first to discuss what needs to be changed.

-----

# Road Map

- Plotly scientific & statistical functions
    - Caveat: Plotly graphs _cannot_ be displayed in GitHub, but they can be viewed in [nbviewer](https://nbviewer.jupyter.org/).
- Bokeh Interactive functions

-----

# Project Status

Work is ongoing: I add or modify code as needed.

I am working on adding more plotly functions which are housed in a new file called `plotly_graphs.py`.  While they are not ideal for use with GitHub, they are ideal for situations where you would be saving the images for use elsewhere.

# Latest Updates

12/20/2019:

- Made `hue` default for `categorical_boxplots`
- Fix `df = df` for `categorical_violinplots`
- Updated appearance of docstrings
- Made `ticks` a parameter for `barplot`