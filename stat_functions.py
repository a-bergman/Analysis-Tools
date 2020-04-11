"""

This module contains functions that render statistics, corresponding p-values, & interpretations of the p-values in dataframes.

There are two sections:

- Correlation between variables
- Model comparison, i.e. are models distinct

"""

#  Standard Imports
import numpy  as np
import pandas as pd

# Stastical Imports
from mlxtend.evaluate                     import mcnemar_table, combined_ftest_5x2cv
from scipy.stats                          import pearsonr, pointbiserialr
from scipy.stats                          import chi2_contingency
from statsmodels.stats.contingency_tables import mcnemar

"""

The docstrings for each function contain the following:

- parameters      : values which must be entered, some of which are defaults
- description     : what each function does
- null hypothesis : description of what each function is testing
- returns         : the output of each function

The parameters section of each docstring is set up as:

parameter : definition : type : possible values (if applicable)

"""

############### CORRELATION BETWEEN VARIABLES ###############
  
# Numeric - Numeric Data

def pearsonr_dataframe(df, x, y, columns, alpha = 0.05):
    """
    Parameters:
    -----------
    df      : dataframe source of data                     : DataFrame : :
    x       : column to find correlations against          : str       : :
    y       : list of columns to be correlated against x   : str       : :
    columns : list of columns to be named in the dataframe : str       : :
    alpha   : p-value threshold for significance           : int       : :

    Description:
    ------------
    Generates a list of Pearson's r correlation coefficients & accompanying p-values for two numeric variables
    The r coefficients range from -1 to 1

    Null Hypothesis:
    ----------------
    There is no correlation between two numeric variables

    Returns:
    --------
    A dataframe containing Pearson's r coefficient, the corresponding p-value, & the significance of the p-value.
    The coefficient & p-value are both rounded to 5 decimal placs.
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
    alpha   : p-value threshold for signifiance            : int       : :

    Description:
    ------------
    Generates a list of point-biserial r coefficients & accompanying p-values for a **binary** variable & numeric variables.
    The point-biserial r coefficients range from -1 to 1

    Null Hypothesis:
    ----------------
    There variables are independant.

    Returns:
    --------
    A dataframe containing the point-biserial r coefficient, the corresponding p-value, & the significance of the p-value.
    """
    # Generating a list of the coefficients & rounding them to 5 decimal places
    pbr_coef = [round(pointbiserialr(x = df[x], y = df[i])[0],5) for i in y]
    # Generating a list of the p-values & rounding them to 5 decimal places
    pbr_pval = [round(pointbiserialr(x = df[x], y = df[i])[1],5) for i in y]
    # Indicating if each p-value is significant based on the input alpha value
    pval_sig = ["True" if i < alpha else "False" for i in pbr_pval]
    # Generating the df of the values
    pbr_dataframe = pd.DataFrame([pbr_coef, pbr_pval, pval_sig], index = ["Coefficient", "P-Value", "Significant"], columns = columns).T
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
    alpha   : p-value threshold for significance               : int       : :

    Description:
    ------------
    Generates a list of chi-squared statistics, corresponding p-values, & degrees of freedom for pairs of categorical variables.
    The chi-squared statistic ranges from 0 to +∞

    Null Hypothesis:
    ----------------
    The variables are independant.
    
    Returns:
    --------
    A dataframe containing the chi squared statistic, the accompanying p-value, signifiance of the p-value, & the degrees of freedom. 
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
    chi2_df = pd.DataFrame([chi2_coefs, chi2_pvals, pval_sig, chi2_dofs], index = ["Statistic", "P-Value", "Significant", "DOF"], columns = columns).T
    return chi2_df

############### MODEL COMPARISON: TESTING FOR DIFFERENCE ###############

# Classifiers

def mcnemars_dataframe(y_true, preds_1, preds_2, index, columns):
    """
    Parameters:
    -----------
    y_true  : the actual values                              : Series : :
    preds_1 : the first classification model to be compared  : Series : :
    preds_2 : the second classification mdoel to be compared : Series : :
    index   : list of index labels for the dataframe         : str    : :
    columns : list of column labels for the dataframe        : str    : :

    Description:
    ------------
    Generates a contingency table for a McNemar's test.

    Returns:
    --------
    A dataframe containing the correct & incorrect predictions for two classification models which allows for the calculation of McNemar's test statistic.
    """
    # Generating a contingency table for the two models
    tb = mcnemar_table(y_target = y_true, y_model1 = preds_1, y_model2 = preds_2)
    # Generating a df out of the contingency table
    mcnemars_dataframe = pd.DataFrame(tb, index = index, columns = columns)
    return mcnemars_dataframe

def mcnemars_test(a, b, alpha = 0.05):
    """
    Parameters:
    -----------
    a     : the first classification model       : Series : :
    b     : the second classification model      : Series : :
    alpha : the value used to judge significance : float  : :

    Description:
    ------------
    Generates McNemar's test statistic, the associated p-value, & an interpretation of the p-value for **two** classification models
    This function is independant of `mcnemars_dataframe`

    Null Hypothesis:
    ----------------
    The two models' disagreement is the same, i.e. the models are the same

    Returns:
    --------
    A dataframe containing McNemar's test statistic, the associated p-value, & the p-values' interpretation.

    """
    # Checkin the length of our models
    # If the length > 25 the p-value will be calculated normally
    if len(a) > 25 and len(b) > 25:
        exact = True
    # If the length < 25 the p-value will be calculated with a binomial distribution
    else:
        exact = False
    # Generating a contingency table out of the two models
    ct = pd.crosstab(a,b)
    # Calculating the McNemar's score
    result = mcnemar(ct, exact = exact)
    # Rounding the statistic & p-value to 3 & 5 decimal places respectively
    stat = round(result.statistic,3)
    pval = round(result.pvalue,5)
    # Indicating if the p-value is significant based on the input alpha value
    pval_sig = "True" if pval < alpha else "False"
    # Generating a df of the three values
    mcnemar_df = pd.DataFrame([stat, pval, pval_sig], index = ["Statistic", "P-Value", "Interpretation"], columns = ["Values"]).T 
    return mcnemar_df

# Regressors

def cross_validated_ftest(a, b, X, y, alpha = 0.05, metric = "neg_mean_absolute_error"):
    """
    Parameters:
    -----------
    a      : a Scikit-Learn regression model                         : model     : :
    b      : a Scikit-Learn regression model                         : model     : :
    X      : the X variable containing data features                 : DataFrame : :
    y      : the y variable containing target values                 : Series    : :
    alpha  : the value by which significance is judged               : int       : :
    metric : the metric used for calculation of the f-test statistic : str       : :

    Description:
    ------------
    Generates a 5x2 cross-validated F-test statistic, its p-value, & an interpretation of the p-value for **two** regression models.
    To view acceptable `metric` values run `sklearn.metrics.SCORERS.keys()`.

    Null Hypothesis:
    ----------------
    There are no statistical differences between two regression models

    Returns:
    --------
    A dataframe containing the F-test score, its p-value, & the p-value's interpretation
    """
    # Performing the cross-validated f-test
    # Saving the test statistic & p-value
    f_stat, pval = combined_ftest_5x2cv(estimator1 = a, estimator2 = b, X = X, y = y, scoring = metric, random_seed = 42)
    # Interpreting the significance based on the input alpha
    pval_sig = "True" if pval < alpha else "False"
    # Saving the f-test statistic, p-value, & p-value significance in a df
    ftest_df = pd.DataFrame([f_stat, pval, pval_sig], index = ["F Score", "P-Value", "Significant"], columns = ["Score"]).T
    return ftest_df