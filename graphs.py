# Imports
import matplotlib.pyplot as plt
import numpy             as np
import pandas            as pd
import seaborn           as sns

# Setting the basic appearance for the graphs
sns.set_theme(style = "white", palette = "dark")

"""

The docstrings for each graph contain the following:

- parameters  : values which must be entered, some of which have defaults
- description : what each function does
- returns     : the output of each function

The parameters section of each docstring is set up as:

parameter : definition : type : possible values (if applicable)

Each function is designed to output n number of graphs where n > 1, but can output a single graph.
The only function which is not designed for multiple outputs is the KDE function which only outputs a single graph of two columns.

"""

# TO DO: Replace the deprecated `sns.displot`
#        with whatever is replacing it.

############### Numeric Graphs ###############

def histograms(df, columns, titles, labels, ylabel, ticks, dim, row, col):
    """
    Parameters:
    -----------
    df      : the dataframe source of data               : dataframe : :
    columns : list of columns to be plotted              : str       : :
    titles  : list of titles for each plot               : str       : :
    labels  : list of x-labels for each plot             : str       : :
    label   : the y-label for each plot                  : str       : :
    ticks   : the list of ranges for each plot's x-ticks : np.arange : :
    dim     : tuple of the dimensions of each plot       : int       : :
    row     : how many rows will be generated            : int       : :
    col     : how many columns will be generated         : int       : :

    Description:
    ------------
    Plots histograms for columns containing continuous data in a Pandas dataframe and gives the user greater customization for each plot.

    Returns:
    --------
    Creates n number of histograms arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize=dim, facecolor="white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row,col,count)
        # Naming the graph
        plt.title(f"Distribution Of {titles[c]}", size = 18)
        # Generating the histogram plot
        sns.distplot(df[column], color = "black", kde = False)
        # Plotting a line at the mean value of the histogram
        plt.axvline(df[column].mean(), color = "red")
        # Formatting the labels & axes
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show()

def kdeplots(df, cols, title, dim, colors, labels, xlabel, ylabel, ticks, shade = True):
    """
    Parameters:
    -----------
    df     : the dataframe source of data                   : dataframe : :
    cols   : list of the columns                            : str       : :
    title  : plot title                                     : str       : :
    dim    : tuple of the dimensions of each plot           : int       : :
    colors : list of the colors of each kde plot            : str       : :
    labels : list of thethe name of each kde                : str       : :
    xlabel : the label of the x-axis                        : str       : :
    ylabel : the label of the y-axis                        : str       : :
    ticks  : the range of the x-ticks                       : np.arange : :
    shade  : whether or not to shade the area under the kde : Bool      : :

    Description:
    ------------
    Overlays two univariate kernel density estimates on the same axis which estimate the distribution of two columns of data.

    Returns:
    --------
    A single graph with two overlaid density estimates.
    
    """
    # Setting figure size, background color, & title
    plt.figure(figsize = dim, facecolor = "white")
    plt.title(f"{title}", size = 18)
    # Graphing the two KDE plots
    sns.kdeplot(df[cols[0]], shade = shade, color = colors[0], label = labels[0])
    sns.kdeplot(df[cols[1]], shade = shade, color = colors[1], label = labels[1])
    # Formatting the labels, legend, & ticks
    plt.xlabel(f"{xlabel}", size = 16)
    plt.ylabel(f"{ylabel}", size = 16)
    plt.xticks(ticks, size = 14)
    plt.yticks(size = 14)
    plt.legend(bbox_to_anchor = (1.04, 1), loc = "upper left", fontsize = 16)
    plt.show()
    
def boxplots(df, columns, titles, labels, ticks, dim, row, col, x = None, hue = None, xlabel = None):
    """
    Parameters:
    -----------
    df      : dataframe source of the data            : dataframe :     :
    columns : list of the columns to be plotted       : str       :     :
    x       : categorical column to subdivide data by : NoneType  :     :
    titles  : list of titles for each plot            : str       :     :
    ticks   : list of ranges for the x-ticks          : np.arange :     :
    dim     : tuple of the dimensions of each plot    : int       :     :
    row     : how many rows will be generated         : int       :     :
    col     : how many columns will be generated      : int       :     :
    hue     : categorical variable to divide data by  : NoneType  :     :
    xlabel  : label for the x-axis                    : NoneType  :     :
    
    Description:
    ------------
    Plots a vertical boxplots for columns containing continuous data in a Pandas dataframe and gives the user greater customization for each plot.

    Returns:
    --------
    n number of boxplots arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize = dim, facecolor = "white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row, col, count)
        # Naming the graph
        plt.title(f"{titles[c]}", size = 18)
        # Generating the box plot
        sns.boxplot(y = column, x = x, data = df, orient = "v", hue = hue)
        # Formatting the labels & axes
        plt.xlabel(xlabel = xlabel, size = 16)
        plt.ylabel(f"{labels[c]}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(ticks[c], size = 14)
    plt.tight_layout()
    plt.show()

def violinplots(df, columns, titles, labels, ticks, dim, row, col, palette, x = None, hue = None, split = False, xlabel = None):
    """
    Parameters:
    ----------- 
    df      : dataframe source of data                       : dataframe :                   :
    columns : list of columns to be plotted                  : str       :                   :
    x       : categorical variable to divide data by         : NoneType  :                   :
    titles  : list of titles for each plot                   : str       :                   :
    labels  : list of the y-labels for each plot             : str       :                   :
    ticks   : list of ranges for the x-ticks                 : np.arange :                   :
    dim     : tuple of the dimensions of each plot           : int       :                   :
    row     : how many rows will be generated                : int       :                   :
    col     : how many columns will be generated             : int       :                   :
    palette : color palette to be used; list or str          : list/str  : "Dark2","#B45D1F" :
    hue     : categorical variable to divide the data by     : NoneType  :                   :
    split   : whether or not to split the hue onto each side : Bool      :                   :
    xlabel  : label for the x axis                           : NoneType  :                   :

    Descriptions:
    -------------
    Plots violin plots for columns containing data in a Pandas dataframe and gives the user greater customization for each plot.
    An improvement over the standard box plot in that it plots a kernel density plot of the points on the sides of each plot.

    Returns:
    --------
    n number of violin plots arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize = dim, facecolor = "white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row, col, count)
        # Naming the graph
        plt.title(f"{titles[c]}", size = 18)
        # Generating the violin plot
        sns.violinplot(y = column, x = x, data = df, hue = hue, split = split, palette = palette, orient = "v")
        # Formatting the labels, axes, & ticks
        plt.xlabel(xlabel = xlabel, size = 16)
        plt.ylabel(f"{labels[c]}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(ticks = ticks[c], size = 14)
    plt.tight_layout()
    plt.show()


def regressionplots(df, columns, y, titles, labels, ylabel, ticks, dim, row, col, mark = "*", color = "black", kws = {"color": "red"}, ci = None):
    """
    Parameters:
    -----------
    df      : dataframe source of data                         : dataframe : :
    columns : the list of columns to be plotted                : str       : :
    y       : the column against which the columns are plotted : str       : :
    titles  : list of the titles for each plot                 : str       : :
    ylabel  : the title of the y-axis                          : str       : :
    ticks   : list of ranges of x-ticks for each plot          : np.arange : :
    dim     : tuple of the dimensions of each plot             : int       : :
    row     : how many rows will be generated                  : int       : :
    col     : how many columns will be generated               : int       : :
    mark    : what character the markers will be               : str       : :
    color   : what color the markers are                       : str       : :
    kws     : what color the regression line is                : dict      : :
    ci      : whether or not to plot a confidence interval     : Bool      : :

    Description:
    ------------
    Plots a scatter plot for each column of continuous data in a Pandas dataframe with a regression line 
    and allows the user to have greater control of the appearance of each graph.

    Returns:
    --------
    n number of regression plots arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize = dim, facecolor = "white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row, col, count)
        # Naming the graph
        plt.title(f"{titles[c]}", size = 18)
        # Generating the scatter plot
        sns.regplot(x = column, y = y, data = df, fit_reg = True,  marker = mark, color = color, line_kws = kws, ci = ci)
        # Formatting the labels, axes, & ticks
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show()

def heatmap(df, columns, dim, title, vmin, vmax, cmap = "RdBu", annot = True):
    """
    Parameters:
    -----------
    df      : dataframe source of the data                  : dataframe : :
    columns : list of the columns to be included            : str       : :
    dim     : tuple of the dimensions of the graph          : int       : :
    title   : title of the graph                            : str       : :
    vmin    : minimum correlation value                     : int       : :
    vmax    : maximum correlation value                     : int       : :
    cmap    : the color scheme to be used                   : str       : :
    annot   : whether or not the heat map will be annotated : Bool      : :
    
    Description:
    ------------
    Plots a heatmap for columns containing continuous data in a Pandas dataframe and allows for increased appearance control.
    The resulting heatmap is not mirrored

    Returns:
    --------
    A heat map displaying the correlations between n number of columns.
    """
    # Setting the figure size, background color, & title
    plt.figure(figsize = dim, facecolor = "white")
    plt.title(f"{title}", size = 18)
    # Calculating Pearson's correlation using the built-in Pandas method
    corr = df[columns].corr()
    # Masking the heat-map does not mirror it: it will end up like a triangle
    mask = np.zeros_like(corr)                                                                                
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        # Graphing the heat-map
        sns.heatmap(corr, cmap = cmap,  mask = mask, vmin = vmin, vmax = vmax, annot = annot)
    # Formatting the size of the ticks
    plt.xticks(size = 14)
    plt.yticks(size = 14)
    plt.show()

############### Categorical Graphs ###############

def countplots(df, columns, titles, labels, ylabel, dim, row, col, palette, orient = "h", hue = None):
    """
    Parameters:
    -----------
    df      : dataframe source of data                    : dataframe :                   :
    columns : list of the columns to be plotted           : str       :                   :
    titles  : list of the titles for each plot            : str       :                   :
    labels  : list of the x-labels for each plot          : str       :                   :
    ylabel  : list of the ylabel for each plt             : str       :                   :
    dim     : tuple of the dimensions of each plot        : int       :                   :
    row     : how many rows will be generated             : int       :                   :
    col     : how many columns will be generated          : int       :                   :
    palette : color palette to be used; list or str       : list/str  : "Dark2","#B45D1F" :
    orient  : orientation of each plot                    : str       : "v"               :
    hue     : which column will be used for color-coding  : str       :                   :
    
    Description:
    -------------   
    Creates a count plot for columns in a Pandas dataframe containing categorical data.  
    This type of plot explicitly counts the categories in a dataframe column.

    Returns:
    --------
    n number of count plots arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize = dim, facecolor = "white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row, col, count)
        # Naming the graph
        plt.title(f"{titles[c]}", size = 18)
        # Generating the count plot
        sns.countplot(x = column, data = df, orient = orient, hue = hue, palette = palette)
        # Formatting the labels & ticks
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show()

def countplots_dt(df, columns, titles, labels, ylabel, dim, row, col, palette, orient = "h", hue = None):
    """
    Parameters:
    -----------
    df      : dataframe source of data                    : dataframe :                   :
    columns : list of the columns to be plotted           : str       :                   :
    titles  : list of the titles for each plot            : str       :                   :
    labels  : list of the x-labels for each plot          : str       :                   :
    ylabel  : list of the ylabel for each plt             : str       :                   :
    dim     : tuple of the dimensions of each plot        : int       :                   :
    row     : how many rows will be generated             : int       :                   :
    col     : how many columns will be generated          : int       :                   :
    palette : color palette to be used; list or str       : list/str  : "Dark2","#B45D1F" :
    orient  : orientation of each plot                    : str       : "v"               :
    hue     : which column will be used for color-coding  : str       :                   :
    
    Description:
    -------------   
    Creates a count plot for columns in a Pandas dataframe containing categorical data.  
    This type of plot explicitly counts the categories in a dataframe column.

    Returns:
    --------
    n number of count plots arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize = dim, facecolor = "white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row, col, count)
        # Naming the graph
        plt.title(f"{titles[c]}", size = 18)
        # Generating the count plot
        sns.countplot(x = column, data = df, orient = orient, palette = palette, hue = hue)
        # Formatting the labels & ticks
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
        x_dates = df[column].dt.strftime("%Y-%m-%d").sort_values().unique()
        ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def countplots_order(df, columns, titles, labels, ylabel, dim, row, col, palette, orient = "h", hue = None):
    """
    Parameters:
    -----------
    df      : dataframe source of data                    : dataframe :                   :
    columns : list of the columns to be plotted           : str       :                   :
    titles  : list of the titles for each plot            : str       :                   :
    labels  : list of the x-labels for each plot          : str       :                   :
    ylabel  : list of the ylabel for each plt             : str       :                   :
    dim     : tuple of the dimensions of each plot        : int       :                   :
    row     : how many rows will be generated             : int       :                   :
    col     : how many columns will be generated          : int       :                   :
    palette : color palette to be used; list or str       : list/str  : "Dark2","#B45D1F" :
    orient  : orientation of each plot                    : str       : "v"               :
    hue     : which column will be used for color-coding  : str       :                   :
    
    Description:
    -------------   
    Creates a count plot for columns in a Pandas dataframe containing categorical data sorted by category values descending.  
    This type of plot explicitly counts the categories in a dataframe column.

    Returns:
    --------
    n number of count plots arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize = dim, facecolor = "white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row, col, count)
        # Naming the graph
        plt.title(f"{titles[c]}", size = 18)
        # Generating the count plot
        sns.countplot(x = column, data = df, orient = orient, hue = hue, palette = palette, order = df[column].value_counts().index)
        # Formatting the labels & ticks
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show()

def barplots(df, columns, y, labels, ylabel, titles, dim, row, col, palette, errorbar = "ci", estimator = "mean", orient = "v", hue = None):
    """
    Parameters:
    -----------
    df        : dataframe source of data                     : dataframe :                   :
    x         : list of the x inputs for each plot           : str       :                   :
    y         : list of the y input for each plot            : str       :                   :
    labels    : list of the x-labels for each plot           : str       :                   :
    ylabel    : y-label for each plot                        : str       :                   :
    titles    : list of the titles for each plot             : strs      :                   :
    dim       : tuple of the dimensions of each plot         : int       :                   :
    row       : how many rows will be generated              : int       :                   :
    col       : how many columns will be generated           : int       :                   :
    errorbar  : method to calculate the error bar            : str       : "ci"              :
    estimator : measure of central tendency to be calculated : str       : "mean"            :
    palette   : color palette to be used; list or str        : list/str  : "Dark2","#B45D1F" :
    orient    : orientation of each bar plot                 : str       : "v"               :
    hue       : which column will be used for color-coding   : str       :                   :

    Description:
    ------------
    Plots a bar plot for each column containing categorical data in a Pandas dataframe and allows for greater appearance control.
    This type of plot takes a categorical variable and returns the mean of a corresponding numeric variable.

    Returns:
    n number of barplots arranged by the input rows and columns.
    """
    # Setting the default position in the subplot grid
    count = 0
    # Setting the size & backgroundcolor for each subplot
    fig = plt.figure(figsize = dim, facecolor = "white")
    # Looping through each column
    for c, column in enumerate(columns):
        # Setting the location for the next graph
        count += 1
        # Setting up the subplot grid
        ax = fig.add_subplot(row, col, count)
        # Naming the graph
        plt.title(f"{titles[c]}", size = 18)
        # Generating the bar graph
        sns.barplot(x = column, y = y, data = df, estimator = estimator, errorbar = errorbar, orient = orient, hue = hue, palette = palette)
        # Formatting the labels & axes
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show()

def barplot(df, x, y, title, label, ylabel, ticks, dim, palette, estimator = "mean", errorbar = "ci",hue = None):
    """
    Parameters:
    -----------
    df        : dataframe source of the data                 : dataframe :                   :
    x         : the column to be the x-axis                  : str       :                   :
    y         : the column to be the y-axis                  : str       :                   :
    title     : title of the graph                           : str       :                   :
    label     : the label of the x-axis                      : str       :                   :
    ylabel    : the label of the y-axis                      : str       :                   :
    yticks    : range for the y-ticks                        : np.arange :                   : 
    dim       : tuple of the graph dimensions                : int       :                   :
    errorbar  : method to calculate the error bar            : str       : "ci"              :
    estimator : measure of central tendency to be calculated : str       : "mean"            :
    palette   : color palette to be used; list or str        : list/str  : "Dark2","#B45D1F" :
    orient    : orientation of the graph                     : str       : "v"               :
    hue       : which column will be used for color-coding   : str       :                   :

    Description:
    ------------
    Plots a single bar chart for a categorical column in a Pandas dataframe and allows for greater appearance control.
    This type of chart takes a categorical variable and a corresponding value; it does *not* return a measure of central tendency.
    It is best suited to plotting when the x-axis would be the index of a dataframe.

    Returns:
    --------
    A single bar plot with the input dimensions.
    """
    # Setting the figure size & background color
    plt.figure(figsize = dim, facecolor = "white")
    # Graphing the barplot
    sns.barplot(x = x, y = y, data = df, hue = hue, palette = palette, estimator = estimator, errorbar = errorbar)
    # Formatting the title, labels, & ticks
    plt.title(f"{title}", size = 18)
    plt.xlabel(f"{label}", size = 16)
    plt.ylabel(f"{ylabel}", size = 16)
    plt.xticks(size = 14)
    plt.yticks(ticks = ticks, size = 14)
    plt.tight_layout()
    plt.show()