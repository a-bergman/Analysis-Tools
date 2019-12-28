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
    fig = go.Figure(go.Histogram2d(x = df[x], y = df[y], colorscale = colorscale))
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, xanchor = "center", yanchor = "top"),
                      xaxis_title = xlabel, yaxis_title = ylabel, width = width, height = height)
    fig.update_xaxes(tickvals = xticks, title_font = dict(size = 18),tickfont = dict(size = 14))
    fig.update_yaxes(tickvals = yticks, title_font = dict(size = 18),tickfont = dict(size = 14))
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
    ytitle   : height of the title above the plot           : int       :                             :
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