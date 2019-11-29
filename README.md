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

| Plot Type     | Numeric Data | Categorical Data |
|:---------- ---|:------------:|:----------------:|
| Box Plots     | ✓            | ✓               |
| Count Plots   | ✓            |                  |
| Heat Maps     | ✓            |                  |
| Histograms    | ✓            |                  |
| KDE Plots     | ✓            |                  |
| Scatter Plots | ✓            |                  |
| Violin Plots  | ✓            | ✓               |

For Model Evaluation:

| Plot Type      | Numeric Data | Categorical Data |
|:---------------|:------------:|:----------------:|
| Residual Plots | ✓            |                  |
| ROC Curves     |              | ✓                |