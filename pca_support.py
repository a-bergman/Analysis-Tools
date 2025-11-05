# Imports
import numpy                 as np
import matplotlib.pyplot     as plt
import cuml.decomposition    as cude
import sklearn.decomposition as skde

"""

The docstrings for each graph contain the following:

- parameters  : values which must be entered, some of which have defaults
- description : what each function does
- returns     : the output of each function

The parameters section of each docstring is set up as:

parameter : definition : type : default or possible values (if applicable)

Each function is designed to output n number of graphs where n > 1, but can output a single graph.
The only function which is not designed for multiple outputs is the KDE function which only outputs a single graph of two columns.
"""

"""
The default versions rely on sklearn which should already be installed on your machine,

The GPU version of these functions require that you have CUML installed locally and
that you have access to a GPU for acceleration.

As of 2025-11-05 I don't have access to a GPU, so this will be used in Google Colab.

"""

# TO DO: I'd like to implement calc_n_comp
#        directly into the graphing functions

########## Calculating # of Components For PCA ##########

# Calculating the number of components for PCA
def calc_n_comp(train_data,threshold=0.90):
    """
    Parameters:
    -----------
    train_data : the X_train data set for model training : df  :      :
    threshold  : the amount of variance to be described  : int : 0.90 :

    Description:
    ------------
    This function calculates and prints the number of components needed to explain the threshold amount of variance

    Returns:
    --------
    A statement containing the number of components
    """
    # Fitting PCA to the trianing data
    pca=skde.PCA().fit(train_data)
    # Extracting and printing the components for the threshold
    # This defaults to 0.90/90%
    cum_var=np.cumsum(pca.explained_variance_ratio_)
    n_comp=np.argmax(cum_var>=threshold)+1
    print(f"\n The number of components that explain {threshold*100}% of variance is: {n_comp}.")


# Calculating the number of components for PCA - GPU version
def calc_n_comp_gpu(train_data,threshold=0.90):
    """
    Parameters:
    -----------
    train_data : the X_train data set for model training : df  :      :
    threshold  : the amount of variance to be described  : int : 0.90 :

    Description:
    ------------
    This function calculates and prints the number of components needed to explain the threshold amount of variance

    Returns:
    --------
    A statement containing the number of components
    """
    # Fitting PCA to the trianing data
    pca=cude.PCA().fit(train_data)
    # Extracting and printing the components for the threshold
    # This defaults to 0.90/90%
    cum_var=np.cumsum(pca.explained_variance_ratio_)
    n_comp=np.argmax(cum_var>=threshold)+1
    print(f"\n The number of components that explain {threshold*100}% of variance is: {n_comp}.")

########## Plotting The Explained Variance Ratio For PCA ##########

# Plotting explained variance
def plot_pca(train_data,n_comp,dim=(15,5),var_line_color="#1F77B4",v_line_color="#B45D1F",line_width=4):
    """
    Parameters:
    -----------
    train_data     : the X_train data set for model training     : df    :         :
    n_comp         : the number of principal components          : int   :         :
    dim            : the dimensions of the graph                 : tuple : (15,5)  :
    var_line_color : *hex* color of the explained variance line  : str   : #1F77B4 :
    v_line_color   : *hex* color of the vertical line for n_comp : str   : #B45D1F :
    line_width     : width of the two lines                      : int   : 4       :

    Description:
    ------------
    This function plots the explained variance derived from PCA and a vertical line representing the number of
    components being included.

    Returns:
    --------
    A single graph depicting the explained variance ratio derived from PCA
    """
    # Fitting PCA to the training data
    pca = skde.PCA().fit(train_data)
    # Setting up the figure and plotting the explained_variance_ratio
    plt.figure(figsize=dim,facecolor="white")
    plt.plot(np.cumsum(pca.explained_variance_ratio_),color=var_line_color,linewidth=line_width)
    # Plotting the number of components we'll be using
    plt.axvline(x=n_comp,color=v_line_color,linewidth=line_width)
    # Adding labels and formatting axes
    plt.xlabel("# Components")
    plt.ylabel("Cumulative Explained Variance %")
    plt.xticks(size=14)
    plt.yticks(ticks=np.arange(0,1.1,0.1),size=14)
    plt.show()

# Plotting explained variance - GPU version
def plot_pca_gpu(train_data,n_comp,dim=(15,5),var_line_color="#1F77B4",v_line_color="#B45D1F",line_width=4):
    """
    Parameters:
    -----------
    train_data     : the X_train data set for model training     : df    :         :
    n_comp         : the number of principal components          : int   :         :
    dim            : the dimensions of the graph                 : tuple : (15,5)  :
    var_line_color : *hex* color of the explained variance line  : str   : #1F77B4 :
    v_line_color   : *hex* color of the vertical line for n_comp : str   : #B45D1F :
    line_width     : width of the two lines                      : int   : 4       :

    Description:
    ------------
    This function plots the explained variance derived from PCA and a vertical line representing the number of
    components being included.

    This function is designed for use with a GPU using CUML for GPU support.

    Returns:
    --------
    A single graph depicting the explained variance ratio derived from PCA
    """
    # Fitting PCA to the training data
    pca = cude.PCA().fit(train_data)
    plt.figure(figsize=dim,facecolor="white")
    # Setting up the figure and plotting the explained_variance_ratio
    plt.plot(np.cumsum(pca.explained_variance_ratio_),color=var_line_color,linewidth=line_width)
     # Plotting the number of components we'll be using
    plt.axvline(x=n_comp,color=v_line_color,linewidth=line_width)
    # Adding labels and formatting axes
    plt.xlabel("# Components")
    plt.ylabel("Cumulative Explained Variance %")
    plt.xticks(size=14)
    plt.yticks(ticks=np.arange(0,1.1,0.1),size=14)
    plt.show()