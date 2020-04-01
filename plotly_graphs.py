# Imports
import numpy                 as np
import pandas                as pd
import plotly.io             as pio
import plotly.express        as pex
import plotly.figure_factory as ff
import plotly.graph_objs     as go

# Setting basic graph appearance
pio.templates.default = "simple_white"

# Color schema
c_default             = ["rgb(31,119,180)"]
c_complimentary       = ["rgb(31,119,180)", "rgb(180,93,31)"]
c_split_complimentary = ["rgb(31,119,180)", "rgb(180,168,31)", "rgb(180,31,43)"]
c_triadic             = ["rgb(31,119,180)", "rgb(118,180,31)", "rgb(180,31,118)"]
c_tetradic            = ["rgb(31,119,180)", "rgb(180,93,31)", "rgb(93,31,180)", "rgb(118,180,31]"]

"""
Default scolor is "rgb(3,119,180)"

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

# TO DO: Update the `table` function

def color_scheme(c_type, scheme = "default"):
    if scheme == "default":
        if c_type == "default":
            print(f"The default color is: {c_default}.")
        elif c_type == "complimentary":
            print(f"The complimentary colors are: {c_complimentary[0]} & {c_complimentary[1]}.")
        elif c_type == "split_complimentary":
            print("The split complimentary colors are: {c_split_complimentary[0]}, {c_split_complimentary[1]}, & {c_split_complimentary[2]}.")
        elif c_type == "triadic":
            print(f"The triadic colors are: {c_triadic[0]}, {c_triadic[1]}, {c_triadic[2]}.")
        elif c_type == "tetradic":
            print(f"The tetradic colors are: {c_tetradic[0]}, {c_tetradic[1]}, {c_tetradic[2]}, & {c_tetradic[3]}")
        else:
            print("Please enter one of the following: default, complimentary, split_complimentary, triadic, or tetradic.")
    else:
        print("Please check your scheme input!")

# Numeric Data

def histogram(df, x, width, height, bins, title, xlabel, ticks, hue = None, color = ["rgb(31,119,180)"], ytitle = 0.95, ylabel = "Count"):
    """
    Parameters:
    -----------
    df     : dataframe source of data       : dataframe :     :
    x      : dataframe column to be graphed : str       :     :
    width  : width of the graph             : int       :     :
    height : height of the graph            : int       :     :
    bins   : number of bins to be generated : int       :     :
    title  : title of the graph             : str       :     :
    xlabel : label for the x axis           : str       :     :
    ticks  : ticks for the x axis           : np.arange :     :
    hue    : column to split the data on    : None      : str : 
    color  : list of the histogram color    : str       :     :
    ytitle : height of title above graph    : float     :     :
    ylabel : label for the y axis           : str       :     :

    Description:
    ------------
    Plots a histogram of a single dataframe column.  If `hue` is included, a second or more colors *must* be included.
    See the default colors listed above for inspiration.

    Returns:
    -------
    A single histogram with the input dimensions and number of bins
    """
    # Defining the basic figure
    fig = pex.histogram(df, x = x, color = hue, width = width, height = height, color_discrete_sequence = color, nbins = bins, hover_data = df.columns)
    # Adding the title & labels
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, yanchor = "top", xanchor = "center"), xaxis_title = xlabel, yaxis_title = ylabel, font = dict(size = 18))
    # Formating the x-axis
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = ticks)
    # Formating the y-axis
    fig.update_yaxes(title_font = dict(size = 16), tickfont = dict(size = 14))
    fig.show()

def double_histogram(data, names, texts, bins, title, width, height, xlabel, ticks, colors = ["rgb(31,119,180)", "rgb(180,93,31)"], mode = "overlay", ytitle = 0.9, ylabel = "Count", opacity = 0.65):
    """
    Parameters:
    ----------
    data    : list of series to be plotted                      : Series    :         :
    names   : list of the names of each histogram in the legend : str       :         :
    texts   : list of the names for hoverovers in the graph     : str       :         :
    title   : title of the graph                                : str       :         :
    width   : width of the graph                                : int       :         :
    height  : height of the graph                               : int       :         :
    xlabel  : label for the x axis                              : str       :         :
    ticks   : ticks for the x axis                              : np.arange :         :
    colors  : list of the color values for the two graphs       : str       :         :
    mode    : how the two graphs will be displayed              : str       : "stack" :
    ytitle  : how high above the graph to place the title       : float     :         :
    ylabel  : label for the x axis                              : str       :         :
    opacity : how opaque to make the two graphs                 : float     :         :

    Description:
    ------------
    Takes two dataframe columns & overlays or stacks the histograms on top of each other.

    Returns:
    --------
    A stacked or overlain histogram of two columns with input dimensions and bins.
    """
    # Setting & applying the color scheme
    layout = go.Layout(colorway = colors)
    fig = go.Figure(layout = layout)
    # Adding the first histogram & setting basic the appearance
    fig.add_trace(go.Histogram(x = data[0], name = names[0], text = texts[0], nbinsx = bins[0]))
    # Adding the second histogram & setting basic the appearance
    fig.add_trace(go.Histogram(x = data[1], name = names[1], text = texts[1], nbinsx = bins[1]))
    # Setting labels & the title
    fig.update_layout(barmode = mode, xaxis_title = xlabel, yaxis_title = ylabel, width = width, 
                      height = height, font = dict(size = 18), legend_orientation = "v", 
                      title = dict(text = title, y = ytitle, x = 0.5, xanchor = "center", yanchor = "top"),
                      legend = dict(font = dict(size = 14), bordercolor = "black", borderwidth = 1))
    fig.update_traces(opacity = opacity)
    # Formatting the x-axis
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = ticks)
    # Formatting the y-axis
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
    # Setting the basic figure appearance
    fig = go.Figure(go.Histogram2d(x = df[x], y = df[y], colorscale = colorscale, colorbar = dict(outlinewidth = 1)))
    # Adding the title & labels
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, xanchor = "center", yanchor = "top"), xaxis_title = xlabel, yaxis_title = ylabel, width = width, height = height)
    # Formatting the x-axis
    fig.update_xaxes(tickvals = xticks, title_font = dict(size = 18),tickfont = dict(size = 14))
    # Formatting the y-axis
    fig.update_yaxes(tickvals = yticks, title_font = dict(size = 18),tickfont = dict(size = 14))
    fig.show()

def box_plot(df, y, width, height, title, ylabel, ticks, x = None, color = ["rgb(31,119,180)"], notch = False, orient = "v", ytitle = 0.95):
    """
    Parameters:
    ----------
    df     : dataframe source of data                      : dataframe :     :
    y      : data to be plotted                            : str       :     :
    width  : width of the graph                            : int       :     :
    height : height of the graph                           : int       :     :
    title  : title of the graph                            : str       :     :
    ylabel : label for the y axis                          : str       :     :
    ticks  : ticks for the y axis                          : np.arange :     :
    x      : categorical column to divide the data by      : NoneType  : str :
    color  : list of RGB color(s) for the box(es)          : str       :     :
    notch  : whether or not to include a notch at the mean : Bool      :     :
    orient : orientation for the graph                     : str       : "h" :
    ytitle : height of the title above the graph           : float     :     :

    Description:
    ------------
    Plots a vertical box plot of a single numeric source of data.
    The `x` parameter will create a box-plot for each class.
    If you wish to make a horizontal one, `x` and `y` *must* be swapped along with the orientation.

    Returns:
    --------
    A single vertical histogram with the input dimensions
    
    """
    # Setting the basic figure
    fig = pex.box(df, y = y, x = x, width = width, height = height, color_discrete_sequence = color, notched = notch, orientation = orient)
    # Adding the title & labels
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, yanchor = "top", xanchor = "center"), yaxis_title = ylabel, font = dict(size = 18))
    # Formatting the x-axis
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14))
    # Formatting the y-axis
    fig.update_yaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = ticks)
    fig.show()

def violin_plot(df, y, width, height, title, ylabel, ticks, x = None, color = ["rgb(31,119,180)"], orient = "v", box = True, ytitle = 0.95):
    """
    Parameters:
    -----------
    df     : dataframe source of data                   : dataframe :     :
    y      : data to be plotted                         : str       :     :
    width  : width of the graph                         : int       :     :
    height : height of the graph                        : int       :     :
    title  : title of the graph                         : str       :     :
    ylabel : title for the y axis                       : str       :     :
    ticks  : ticks for the y axis                       : np.arange :     :
    x      : categorical variable to divide the data by : NoneType  : str :
    color  : RGB color of the graph                     : str       :     :
    orient : orientation of the graph                   : str       : "h" :
    box    : whether or not to include a boxplot        : Bool      :     :
    ytitle : height of the title above the graph        : float     :     :

    Description:
    ------------
    Plots a vertical violin plot of a single numeric source of data.
    The `x` parameter will create a violin-plot for each class.
    If you wish to make a horizontal one, `x` and `y` *must* be swapped along with the orientation.

    Returns:
    --------
    A single vertical histogram with the input dimensions
    """
    # Setting the basic figure
    fig = pex.violin(df, y = y, width = width, height = height, x = x, color_discrete_sequence = color, orientation = orient, box = True)
    # Adding the title & labels
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, yanchor = "top", xanchor = "center"), yaxis_title = ylabel, font = dict(size = 18))
    # Formatting the x-axis
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = None)
    # Formatting the y-axis
    fig.update_yaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = ticks)
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
    # Setting the basic figure
    fig = pex.scatter(df, x = x, y = y, trendline = trend, trendline_color_override = trend_color, width = width, height = height, render_mode = render)
    # Adding the title & labes
    fig.update_layout(title = dict(text = title, y = ytitle, x = 0.5, xanchor = "center", yanchor = "top"), xaxis_title = xlabel, yaxis_title = ylabel, font = dict(size = 18))
    # Formatting the x-axis
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = xticks)
    # Formatting the y-axis
    fig.update_yaxes(title_font = dict(size = 16), tickfont = dict(size = 14), tickvals = yticks)
    # Adding the line of best fit
    fig.update_traces(marker = dict(color = color))
    fig.show()

def heatmap(df, cols, labels, width, height, title, zmax = 1, zmin = -1, scale = "RdBu", ytitle = 0.9):
    """
    Parameters:
    -----------
    df     : dataframe source of data                : dataframe :    :
    cols   : list of numeric columns to be plotted   : str       :    :
    labels : list of the labels for the x and y axes : str       :    :
    width  : width of the graph                      : int       :    :
    height : height of the graph                     : int       :    :
    title  : title for the graph                     : str       :    :
    zmax   : maximum value for the color scale       : int       :    :
    zmin   : minimum value for the color scale       : int       :    :
    scale  : color scale for the correlations        : str       :    :
    ytitle : height of the title above the graph     : float     :    :

    Descriptions:
    -------------
    Plots a heat map for a number of numeric columns: it colors the squares based on the strength of their correlation & includes the
    correlation in the hover over; a color bar is included for reference.

    Returns:
    --------
    A single heat map for a given number of numeric columns with the input dimensions
    """
    # Setting the basic figure
    fig = go.Figure(data = go.Heatmap(z = df[cols].corr(), x = labels, y = labels, zmax = zmax, zmin = zmin, colorscale = scale, colorbar = dict(outlinewidth = 1)))
    # Adding the title & labels
    fig.update_layout(width = width, height = height, font = dict(size = 18), title = dict(text = title, y = ytitle, x = 0.5, yanchor = "top", xanchor = "center"))
    # Formatting the x-axis
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14))
    # Formatting the y-axis
    fig.update_yaxes(title_font = dict(size = 16), tickfont = dict(size = 14))
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
    # Setting the figure
    fig = go.Figure(data = [go.Bar(x = df[col].unique(), y = df[col].value_counts(),text = df[col].value_counts(), textposition = text_pos,width = widths, marker_color = color)])
    # Adding the title & labels
    fig.update_layout(width = width, height = height,
                      title = dict(text = "Hypertension", y = ytitle, x = 0.5, xanchor = "center", yanchor = "top"), 
                      font = dict(size = 18), xaxis_title = xlabel, yaxis_title = ylabel)
    # Formatting the x-axis
    fig.update_xaxes(title_font = dict(size = 16), tickfont = dict(size = 14))
    # Formatting the y-axis
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
    # Setting the table including the header and cells
    fig = go.Figure(data = [go.Table(header = dict(values = h_values, fill = dict(color = h_fill),line_color = "black", font = dict(color = "white", size = 16)),
                                     cells  = dict(values = c_values, fill = dict(color = c_fill),line_color = "black", font = dict(color = "black", size = 12)))])
    # I'm planning on replacing this function with one from plotly.figure_factory
    # Setting the dimensions
    fig.update_layout(width = width, height = height, margin = go.layout.Margin(l = 25, r = 25, b = 1, t = 25, pad = 0))
    fig.show()