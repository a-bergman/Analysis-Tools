# Imports 

import seaborn           as sns
import numpy             as np
import matplotlib.pyplot as plt
from sklearn.metrics     import roc_auc_score

#####

# Setting the basic appearance for the graphs

sns.set(style = "white", palette = "deep")

#####

def histograms(df, columns, titles, labels, ylabel, ticks, dim, row, col):
    """
    Parameters:
    -----------
    df      : the dataframe source of data               
    columns : list of columns to be plotted, strings
    titles  : list of titles for each plot, strings  
    labels  : list of x-labels for each plot, strings       
    label   : the y-label for each plot, string
    ticks   : the list of ranges for each plot's x-ticks, range
    dim     : dimensions of each plot, tuple
    row     : how many rows will be generated, int
    col     : how many columns will be generated, int

    Description:
    ------------
    Plots histograms for columns containing continuous data in a Pandas dataframe and gives the user greater customization for each plot.

    Returns:
    --------
    Creates n number of histograms arranged by the input rows and columns.

    """
    count = 0
    fig   = plt.figure(figsize = dim, facecolor = "white")
    for c, column in enumerate(columns):
        count += 1
        ax = fig.add_subplot(row, col, count)
        plt.title(f"Distribution Of {titles[c]}", size = 18)
        sns.distplot(df[column], color = "black", kde = False)
        plt.axvline(df[column].mean(), color = "red")
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def boxplots(df, columns, titles, labels, ticks, dim, row, col):
    """
    Parameters:
    -----------
    df      : dataframe source of the data
    columns : list of the columns to be plotted, strings
    titles  : list of titles for each plot, strings
    ticks   : list of ranges for the x-ticks, ranges
    dim     : dimensions of each plot, tuple
    row     : how many rows will be generated
    col     : how many columns will be generated

    Description:
    ------------
    Plots boxplots for columns containing continuous data in a Pandas dataframe and gives the user greater customization for each plot.

    Returns:
    --------
    Creates n number of boxplots arranged by the input rows and columns.
        
    """
    count = 0
    fig   = plt.figure(figsize = dim, facecolor = "white")
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        plt.title(f"{titles[c]}", size = 18)
        sns.boxplot(df[column])
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def regressionplots(df, columns, y, titles, labels, ylabel, ticks, dim, row, col, mark = "*", color = "black", kws = {"color": "red"}, ci = None):
    """
    Parameters:
    -----------
    df      : dataframe source of data
    columns : the list of columns to be plotted, strings
    y       : the column against which the columns are plotted, string
    titles  : list of the titles for each plot, strings
    ylabel  : the title of the y-axis, string
    ticks   : list of ranges of x-ticks for each plot, ranges
    dim     : dimensions of each plot, tuple
    row     : how many rows will be generated, int
    col     : how many columns will be generated, int
    mark    : what character the markers will be
    color   : what color the markers are, str
    kws     : what color the regression line is, dictionary
    ci      : whether or not to plot a confidence interval, Boolean

    Description:
    ------------
    Plots a scatter plot for each column of continuous data in a Pandas dataframe with a regression line 
    and allows the user to have greater control of the appearance of each graph.

    Returns:
    --------
    Creates n number of regression plots arranged by the input rows and columns.
    
    """
    count = 0
    fig   = plt.figure(figsize = dim, facecolor = "white")
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        plt.title(f"{titles[c]}", size = 18)
        sns.regplot(x = column, y = y, data = df, fit_reg = True,  marker = mark, color = color, line_kws = kws, ci = ci)
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def countplots(df, columns, titles, labels, ylabel, dim, row, col):
    """
    Parameters:
    -----------
    df      : dataframe source of data
    columns : list of the columns to be plotted, strings
    titles  : list of the titles for each plot, strings
    labels  : list of the x-labels for each plot, strings
    ylabel  : list of the ylabel for each plt, string
    dim     : dimensions of each plot, tuple
    row     : how many rows will be generated, int
    col     : how many columns will be generated, int
    
    Description:
    -------------   
    Creates a count plot for columns in a Pandas dataframe containing categorical data.  
    This type of plot explicityly counts the categories in a dataframe column.

    Returns:
    --------
    Creates n number of count plots arranged by the input rows and columns.

    """
    fig   = plt.figure(figsize = dim, facecolor = "white")
    count = 0
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        title = titles[c]
        plt.title(f"{title}", size = 18)
        sns.countplot(df[column])
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def barplots(df, x, y, labels, ylabel, titles, dim, row, col):
    """
    Parameters:
    -----------
    df     : dataframe source of data
    x      : list of the x inputs for each plot, strings
    y      : list of the y input for each plot, string
    labels : list of the x-labels for each plot, strings
    ylabel : y-label for each plot, string
    titles : list of the titles for each plot, strings
    dim    : dimensions of each plot, tuple
    row    : how many rows will be generated, int
    col    : how many columns will be generated, int

    Description:
    ------------
    Plots a bar plot for each column containing categorical data in a Pandas dataframe and allows for greater appearance control.

    Returns:
    Creates n number of barplots arranged by the input rows and columns.

    """
    fig   = plt.figure(figsize = dim, facecolor = "white")
    count = 0
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        title = titles[c]
        plt.title(f"{title}", size = 18)
        sns.barplot(x = x, y = y, data = df)
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def heatmap(df, columns, dim, title, vmin, vmax, cmap = "RdBu", annot = True):
    """
    Parameters:
    -----------
    df      : dataframe source of the data
    columns : list of the columns to be included, strings
    dim     : dimensions of the graph, tuple
    title   : title of the graph, string
    vmin    : minimum correlation value
    vmax    : maximum correlation value
    cmap    : the color scheme to be used, string
    annot   : whether or not the heat map will be annotated, Boolean
    
    Description:
    ------------
    Plots a heatmap for columns containing continuous data in a Pandas dataframe and allows for increased appearance control.
    The resulting heatmap is not mirrored

    Returns:
    --------
    A heat map displaying the correlations between n number of columns.
    
    """
    plt.figure(figsize = dim, facecolor = "white")
    plt.title(f"title", size = 18)
    corr = df[columns].corr()
    mask = np.zeros_like(corr)                                                                                
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        sns.heatmap(corr, cmap = cmap,  mask = mask, vmin = vmin, vmax = vmax, annot = annot)
    plt.xticks(size = 14)
    plt.yticks(size = 14);

#####  The ROC curve code was modified from code written by Matt Brems during our lesson on classification metrics.

def roc_curve(model_prob, X_test, y_test, y_predicted, title, dim, roc_color = "darkorange", baseline_color = "navyblue"):
    """
    Parameters:
    -----------
    model_prob     : the model used for prediction
    X_test         : the X values
    y_test         : true y values
    y_predicted    : the model predictions
    title          : title of the graph, string
    dim            : dimensions of the graph, tuple
    roc_color      : color value of the ROC curve, string
    baseline_color : color value of the baseline, string

    Descriptions:
    -------------
    Plots a Receiver Operating Characteristic for a model and includes the AUROC score in the title.

    Returns:
    --------
    Creates a ROC graph for a given model's predictions and allows for appearance control.
    
    """
    model_prob    = [i[0] for i in model_prob.predict_proba(X_test)]
    model_pred_df = pd.DataFrame({"true_values": y_test, "pred_probs": model_prob})
    thresholds = np.linspace(0, 1, 500) 
    def true_positive_rate(df, true_col, pred_prob_col, threshold):
        true_positive  = df[(df[true_col] == 1) & (df[pred_prob_col] >= threshold)].shape[0]
        false_negative = df[(df[true_col] == 1) & (df[pred_prob_col] < threshold)].shape[0]
        return true_positive / (true_positive + false_negative)
    def false_positive_rate(df, true_col, pred_prob_col, threshold):
        true_negative  = df[(df[true_col] == 0) & (df[pred_prob_col] <= threshold)].shape[0]
        false_positive = df[(df[true_col] == 0) & (df[pred_prob_col] > threshold)].shape[0]
        return 1 - (true_negative / (true_negative + false_positive))
    tpr_values = [true_positive_rate(model_pred_df, "true_values", "pred_probs", prob) for prob in thresholds]
    fpr_values = [false_positive_rate(model_pred_df, "true_values", "pred_probs", prob) for prob in thresholds]
    plt.figure(figsize = dim, facecolor = "white")
    plt.plot(fpr_values, tpr_values, color = roc_color, label = "ROC Curve")
    plt.plot(np.linspace(0, 1, 500), np.linspace(0, 1, 500), color = baseline_color, label = "Baseline")
    rocauc_score = round(roc_auc_score(y_test, y_predicted), 5)
    plt.title(f"{title} With A Score of {rocauc_score}", fontsize = 18)
    plt.ylabel("Sensitivity", size = 16)
    plt.xlabel("1 - Specificity", size = 16)
    plt.xticks(size = 14)
    plt.yticks(size = 14)
    plt.legend(bbox_to_anchor = (1.04, 1), loc = "upper left", fontsize = 16)
    plt.tight_layout()