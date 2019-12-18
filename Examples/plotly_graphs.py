# Imports

import plotly.io         as pio
import plotly.graph_objs as go

# Setting basic graph appearance
pio.templates.default = "simple_white"

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

# Categorical Data

# Evaluation Graphs

# Utility Functions