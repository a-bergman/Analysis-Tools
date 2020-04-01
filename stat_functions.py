"""

This module contains functions that render statistics and corresponding p-values in dataframes.

"""

#  Standard Imports
import numpy  as pd
import pandas as pd

# Stastical Imports
from mlxtend.evaluate                     import mcnemar_table
from scipy.stats                          import pearsonr, pointbiserialr
from scipy.stats                          import chi2_contingency
from statsmodels.stats.contingency_tables import mcnemar

"""

The docstrings for each function contain the following:

- parameters  : values which must be entered, some of which have defaults
- description : what each function does
- returns     : the output of each function

The parameters section of each docstring is set up as:

parameter : definition : type : possible values (if applicable)

These functions are designed to build off of what is available in already sci-kit learn: 
either to add a metric that does not exist or to improve something does already exist.

"""

# TO DO: Add a 5X2 CV t-test
  
# Numeric - Numeric Data

def pearsonr_dataframe(df, x, y, columns, alpha = 0.05):
    """
    Parameters:
    -----------
    df      : dataframe source of data                     : DataFrame : :
    x       : column to find correlations against          : str       : :
    y       : list of columns to be correlated against x   : str       : :
    columns : list of columns to be named in the dataframe : str       : :
    p       : p-value threshold for significance           : int       : :

    Description:
    ------------
    Generates a list of Pearson's r correlation coefficients and accompanying p-values for two numeric variables.

    Null Hypothesis:
    ----------------
    There is no correlation between two numeric variables

    Returns:
    --------
    A dataframe with three columns: the float Pearson's r coefficient (a float from -1 to 1), the corresponding p-value, and the significance of the
    p-value.  The coefficient and p-value are both rounded to 5 decimal placs.
    """
    # Generating a list of the coefficients & rounding them to 5 decimal places
    r_coef = [round(pearsonr(x = df[x], y = df[i])[0],5) for i in y]
    # Generating a list of the p-values & rounding them to 5 decimal places
    r_pval = [round(pearsonr(x = df[x], y = df[i])[1],5) for i in y]
    # Indicating if each p-value is significant based on the input alpha value
    pval_sig = ["True" if i < alpha else "False" for i in r_pval]
    # Generating the df of the values
    pr_df = pd.DataFrame([r_coef, r_pval, pval_sig], index = ["Coefficient", "P-Value", "Significant"], columns = columns).T
    return pr_df

# Numeric - Binary Data

def pointbiserialr_dataframe(df, x, y, columns, alpha = 0.05):
    """
    Parameters:
    -----------
    df      : the dataframe source of data                 : DataFrame : :
    x       : column with binary data                      : str       : :
    y       : list of columns with numeric data            : str       : :
    columns : list of columns to be named in the dataframe : str       : :
    p       : p-value threshold for signifiance            : int       : :

    Description:
    ------------
    Generates a list of point-biserial r coefficients and accompanying p-values for a **binary** variable and numeric variables.
    This correlation test assumes that the binary variable is _naturally_ binary _not_ artificially binary, i.e pass/fail.

    Null Hypothesis:
    ----------------
    There variables are independant.

    Returns:
    --------
    A dataframe with three columns: the float point-biserial r coefficient (a float from -1 to 1), the corresponding p-value, and the significance
    of the p-value.  Both the coefficient and p-value are rounded to 5 decimal places.
    """
    # Generating a list of the coefficients & rounding them to 5 decimal places
    pbr_coef = [round(pointbiserialr(x = df[x], y = df[i])[0],5) for i in y]
    # Generating a list of the p-values & rounding them to 5 decimal places
    pbr_pval = [round(pointbiserialr(x = df[x], y = df[i])[1],5) for i in y]
    # Indicating if each p-value is significant based on the input alpha value
    pval_sig = ["True" if i < alpha else "False" for i in pbr_pval]
    # Generating the df of the values
    pbr_dataframe = pd.DataFrame([pbr_coef, pbr_pval, pval_sig], index = ["Coefficient.", "P-Value", "Significant"], columns = columns).T
    return pbr_dataframe

# Categorical - Categorical Data

def chisquared_dataframe(df, x, y, columns, alpha = 0.05):
    """
    Parameters:
    -----------
    df      : dataframe source of data : DataFrame             : DataFrame : :
    x       : name of categorical variable to be correlated to : str       : :
    y       : list of categorical variables to correlated to x : str       : :
    columns : list of columns to be named in the dataframe     : str       : :
    p       : p-value threshold for significance               : int       : :

    Description:
    ------------
    Generates a list of chi squared statistics, corresponding p-values, and degrees of freedom for pairs of categorical variables.

    Null Hypothesis:
    ----------------
    The variables are independant.
    
    Returns:
    --------
    A dataframe with four columns, the chi squared statistic (a float from 0 to +∞), the accompanying p-value, signifiance of the p-value,
    and the degrees of freedom. The statistic and p-value are rounded to 5 decimal places.
    """
    # Setting empty variables for the `for` loop
    chi2_coefs = []
    chi2_pvals = []
    chi2_dofs  = []
    # Looping through every value in `y`
    for col in y:
        # Generating a contingency table for the chi-squared
        ct = pd.crosstab(df[x], df[col])
        # Calculating the chi-squared
        chi2 = chi2_contingency(ct)
        # Appending & rounding each empty variable with data from the chi-squared
        chi2_coefs.append(round(chi2[0],5))
        chi2_pvals.append(round(chi2[1],5))
        chi2_dofs.append(round(chi2[2],5))
    # Indicating if each p-value is significant based on the input alpha value
    pval_sig = ["True" if i < alpha else "False" for i in chi2_pvals]
    # Generating a df based on the values
    chi2_df = pd.DataFrame([chi2_coefs, chi2_pvals, pval_sig, chi2_dofs], index = ["Statistic", "P Value", "Significant", "DOF"], columns = columns).T
    return chi2_df

def mcnemars_dataframe(y_true, preds_1, preds_2, index, columns):
    """
    Parameters:
    -----------
    y_true  : the actual values                                      : Series :
    preds_1 : the first classification model to be compared          : Series :
    preds_2 : the second classification mdoel to be compared         : Series :
    index   : list of index labels for the dataframe                 : str    :
    columns : list of column labels for the dataframe                : str    :

    Description:
    ------------
    Generates a contingency for a McNemar's test.

    Returns:
    --------
    A dataframe containing the correct and incorrect predictions for 2 models which allows for the calculation of McNemar's chi-squared statistic.
    """
    # Generating a contingency table for the two models
    tb = mcnemar_table(y_target = y_true, y_model1 = preds_1, y_model2 = preds_2)
    # Generating a df out of the contingency table
    mcnemars_dataframe = pd.DataFrame(tb, index = index, columns = columns)
    return mcnemars_dataframe

def mcnemars_test(a, b, alpha = 0.05, exact = False):
    """
    Parameters:
    -----------
    a     : the first classification model                                    : Series : :
    b     : the second classification model                                   : Series : :
    alpha : the value used to judge significance                              : float  : :
    exact : whether or not to use a binomial distribution to find the p-value : Bool   : :

    Description:
    ------------
    Generates McNemar's chi-squared statistic, the associated p-value, and an interpretation of the p-value for two classification model

    Null Hypothesis:
    ----------------
    The two classifiers are identical, i.e. the disagreement is the same.

    Returns:
    --------
    A dataframe containing McNemar's chi-squared statistic, the associated p-value, and the p-values interpretation.

    """
    # We need a len>25 to be able to use `exact = False`
    if len(a) > 25 and len(b) > 25:
        # Generating a contingency table out of the two models
        ct = pd.crosstab(a,b)
        # Calculating the McNemar's score
        result = mcnemar(ct, exact = exact)
        # Rounding the statistic & p-value to 5 decimal places
        stat = round(result.statistic,3)
        pval = round(result.pvalue,5)
        # Indicating if the p-value is significant based on the input alpha value
        pval_sig = "True" if pval < alpha else "False"
        # Generating a df of the three values
        mcnemar_df = pd.DataFrame([stat, pval, pval_sig], index = ["Statistic", "P-Value", "Interpretation"], columns = ["Values"]).T 
        return mcnemar_df
    # Telling the user to set `exact = True` if there are <25 values
    else:
        print("If the number of values is <25, please set `Exact = True`.")