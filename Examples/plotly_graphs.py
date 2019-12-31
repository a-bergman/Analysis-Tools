# Imports

import plotly.io         as pio
import plotly.express    as pex
import plotly.graph_objs as go
import numpy             as np
import pandas            as pd

# Setting basic graph appearance
pio.templates.default = "simple_white"

# Color schema

"""
Default scolor is "rgb(31,119,180)"

It's compliment is "rgb(180,93,31)"
It's split compliments are "rgb(180,168,31)" and "rgb(180,31,43)"
It's triadic colors are "rgb(118,180,31)" and "rgb(180,31,118)"
It's tetradic colors are "rgb(180,93,31)", "rgb(93,31,180)", and "rgb(118,180,31)"

[This](https://www.sessions.edu/color-calculator/) was used to determine the rgb values.
"""

# Docstring layout

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

# Numeric Data

def histogram(df, x, width, height, bins, title, xlabel, ticks, hue = None, color = ["rgb(31,119,180)"], ytitle = 0.95, ylabel = "Count"):
    """
    Parameters:
    -----------
    df     : dataframe source of data       : dataframe :      :
    x      : dataframe column to be graphed : str       :      :
    width  : width of the graph             : int       :      :
    height : height of the graph            : int       :      :
    bins   : number of bins to be generated : int       :      :
    title  : title of the graph             : str       :      :
    xlabel : label for the x axis           : str       :      :
    ticks  : ticks for the x axis           : np.arange :      :
    hue    : column to split the data on    : str       : None : 
    color  : list of the histogram color    : str       :      :
    ytitle : height of title above graph    : float     :      :
    ylabel : label for the y axis           : str       :      :

    Description:
    ------------
    Plots a histogram of a single dataframe column.  If `hue` is included, a second or more colors *must* be included.
    See the default colors listed above for inspiration.

    Returns:
    -------
    A single histogram with the input dimensions and number of bins
    """
    fig = pex.histogram(df, x = x, color = hue, width = width, height = height, color_discrete_sequence = color, nbins = bins, hover_data = df.columns)
    fig.update_layout(title = dict(text    = title, y = ytitle, x = 0.5, yanchor = "top", xanchor = "center"),
                      xaxis_title = xlabel, yaxis_title = ylabel, font = dict(size = 18))
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = ticks)
    fig.update_yaxes(title_font = dict(size = 16), tickfont = dict(size = 14))
    fig.show()

def histogram_2d(x, y, df, title, xlabel, ylabel, xticks, yticks, ytitle = 0.9, width = 1000, height = 550, colorscale = "RdBu"):
    """
    Parameters:
    -----------
    x          : the column to be plotted on the x-axis        : str       : :
    y          : the column to be plotted on the y-axis        : str       : :
    df         : dataframe source of data                      : dataframe : :
    title      : title for the graph                           : str       : :
    xlabel     : label for the x-axis                          : str       : :
    ylabel     : label for the y-axis                          : str       : :
    xticks     : tick range for the x-axis                     : np.arange : :
    yticks     : tick range for the y-axis                     : np.arange : :
    ytitle     : how high above the plot to place the title    : float     : :
    width      : width of the plot                             : int       : :
    height     : height of the plot                            : int       : :
    colorscale : color scale to map overlapping of data points : str       : :

    Description:
    ------------
    Plots two continuous columns against each other and shows overlapping points with a color scale and gives the user greater customization over the plot.

    Returns:
    --------
    Creates a single two-dimensional histogram with the input dimensions.
    """
    fig = go.Figure(go.Histogram2d(x = df[x],y = df[y],colorscale = colorscale))
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, xanchor = "center", yanchor = "top"),
                      xaxis_title = xlabel, yaxis_title = ylabel, width = width, height = height)
    fig.update_xaxes(tickvals = xticks, title_font = dict(size = 18),tickfont = dict(size = 14))
    fig.update_yaxes(tickvals = yticks, title_font = dict(size = 18),tickfont = dict(size = 14))
    fig.show()

def scatter_plot(df, x, y, width, height, title, xlabel, ylabel, xticks, yticks,  trend = "ols", trend_color = "rgb(0,0,0)", render = "auto", ytitle = 0.95, color = "rgb(31,119,180)"):
    """
    Parameters:
    -----------
    df          : dataframe source of data                                     : dataframe :               :
    x           : data to be plotted on the xaxis                              : str       :               :
    y           : data to be plotted on the yaxis                              : str       :               :
    width       : width of the graph                                           : int       :               :
    height      : height of the graph                                          : int       :               :
    title       : title of the graph                                           : str       :               :
    xlabel      : title for the xaxis                                          : str       :               :
    ylabel      : title for the yaxis                                          : str       :               :
    xticks      : ticks for the xaxis                                          : np.arange :               :
    yticks      : ticks for the yaxis                                          : np.arange :               :
    trend       : method for drawing the line of best fit                      : str       : "lowess"      :
    trend_color : rgb color value for the line of best fit                     : str       :               :
    render      : method for drawing the marks; `auto` chooses the best method : str       : "svg"|"webgl" :
    ytitle      : how high above the graph to set the title                    : float     :               :
    color       : rgb color value for the markers                              : str       :               :

    Description:
    ------------
    Plots two continuous variables against each other and includes a line of best fit to help illustrate correlation.  
    It uses `trend = "ols"` for linear data and `trend = "lowess"` for non-linear data.

    Returns:
    --------
    Creates a scatter plot with a line of best fit with the input dimensions.

    """
    fig = pex.scatter(df, x = x, y = y, trendline = trend, trendline_color_override = trend_color, width = width, height = height, render_mode = render)
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, xanchor = "center", yanchor = "top"), 
                      xaxis_title = xlabel, yaxis_title = ylabel, font = dict(size = 18))
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = xticks)
    fig.update_yaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = yticks)
    fig.update_traces(marker = dict(color = color))
    fig.show()

# Categorical Data

def bar_chart(df, col, widths, width, height, title, xlabel, ticks, text_pos = "auto", color = "rgb(31,119,180)", ytitle = 0.9, ylabel = "Count"):
    """
    Parameters:
    -----------
    df       : dataframe source of data                     : dataframe :                             :
    col      : the column of categorical data to be plotted : str       :                             :
    widths   : list of the widths for each bar              : int       :                             :
    width    : width of the bar chart                       : int       :                             :
    height   : height of the bar chart                      : int       :                             :
    title    : title of the bar chart                       : str       :                             :
    xlabel   : label for the x axis                         : str       :                             :
    ticks    : ticks for the y axis                         : np.arange :                             :
    text_pos : position of the bar label                    : str       : "inside"|"outside"|"none"   :
    color    : rgb value for the color of the bars          : str       :                             :
    ytitle   : height of the title above the plot           : float     :                             :
    ylabel   : label for the y axis                         : str       :                             :

    Description:
    ------------
    Plots a single bar chart based on the categorical values & frequencies and shows the frequency on each bar; equivalent to Seaborn's `countplot`.

    Returns:
    Creates a single bar chart based off of one columns with the input height & width.
    """
    fig = go.Figure(data = [go.Bar(x = df[col].unique(), y = df[col].value_counts(),
                               text = df[col].value_counts(), textposition = text_pos,
                               width = widths, marker_color = color)])
    fig.update_layout(width = width, height = height,
                      title = dict(text = "Hypertension", y = ytitle, x = 0.5, 
                                   xanchor = "center", yanchor = "top"),
                      font = dict(size = 18), xaxis_title = xlabel, yaxis_title = ylabel)
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14))
    fig.update_yaxes(tickvals = ticks, title_font = dict(size = 16), tickfont = dict(size = 14))
    fig.show()

# Evaluation Graphs

# Utility Functions

def table(h_values, c_values, width = 300, height = 500, h_fill = ["rgb(31, 119, 180)"], c_fill = ["rgb(235,235,235)"]):
    """
    Parameters:
    -----------
    h_values : the headers for the table               : list : :
    c_values : the cell values for the table           : list : :
    width    : the width of the table                  : int  : :
    height   : the height of the table                 : int  : :
    h_fill   : list of the heading shade in rgb scheme : str  : :
    c_fill   : list of the cell shade in rgb scheme    : str  : :

    Description:
    ------------
    Creates a Plotly table with more control over the chart's appearance.  This function returns a table that is easier to distribute outside of an IDE.
    This function can handle lists of data *or* data from a Pandas dataframe: for h_vales enter df.columns with an index & for the c_values enter a list
    of dataframe slices.

    Returns:
    -------- 
    Creates a single table with input values and dimensions
    """
    fig = go.Figure(data = [go.Table(header = dict(values = h_values, fill = dict(color = h_fill),
                                                   line_color = "black", font = dict(color = "white", size = 16)),
                                     cells  = dict(values = c_values, fill = dict(color = c_fill),
                                                   line_color = "black", font = dict(color = "black", size = 12)))])
    # If anyone can figure out why there is so much space under the graph & fix it, I would be really thankful
    fig.update_layout(width = width, height = height, margin = go.layout.Margin(l = 25, r = 25, b = 1, t = 25, pad = 0))
    fig.show()