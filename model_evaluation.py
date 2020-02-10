"""
This file contains two types of functions:
 - Evaluation metrics not currently found in `sklearn.metrics`
 - Summary functions that can be used to evaluate a given model on a range of metrics
 - Functions to generate plots for model evaluation, specifically the ROC curve, PR curve, and residual plots.

The functions that provide metrics not currently found in `sklearn.metrics come before the summaries.
"""
 
#  Standard Imports

import pandas            as pd
import numpy             as np
import seaborn           as sns
import matplotlib.pyplot as plt

# Statistical & Math Imports

from math import sqrt

# Classification Metrics

from sklearn.metrics import confusion_matrix, matthews_corrcoef
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.metrics import fbeta_score, balanced_accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import precision_recall_curve

# Regression Metrics

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error, mean_absolute_error

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

# Regression metrics

def adj_r2(X, y_true, y_predicted):
    """
    Parameters:
    -----------
    X           : the X variables         : np.ndarray : :
    y_true      : the true values         : np.ndarray : :
    y_predicted : the model's predictions : np.ndarray : :

    Description:
    ------------
    Calculates an adjusted R^2 score which is scaled to the number of features in the model: the R^2 score can be inflated by a large number of features.

    Returns:
    --------
    The coefficient of correlation: a float between 0 and 1.
    """
    r2 = r2_score(y_true, y_predicted)
    numerator = (1 - r2) * (len(y) - 1)
    denominator = (len(y_true) - len(X.columns)) - 1
    quotient = numerator / denominator
    r2_adj = 1 - quotient
    return r2_adj

# Classification metrics

def specificity(y_true, y_predicted):
    """
    Parameters:
    -----------
    y_true      : the true values         : np.ndarray : :
    y_predicted : the model's predictions : np.ndarray : :

    Description:
    ------------
    Calculates the percentage of correctly predicted negatives.  A confusion matrix generated and is the score (TN / TN + FP) is calculated.

    Returns:
    --------
    The specificity score: a floating point number between 0 and 1
    """
    tn,fp,tp,fn = confusion_matrix(y_true, y_pred).ravel()
    return tn / (tn + fp)

def negative_predictive_value(y_true, y_predicted):
    """
    Parameters:
    -----------
    y_true      : the true value  s       : np.ndarray : :
    y_predicted : the model's predictions : np.ndarray : :

    Description:
    ------------
    Calculates the percentage of correctly predicted negatives out of all negatives. A confusion matrix generated and is the score (TN / TN + FN) is calculated.

    Returns:
    --------
    The specificity score: a floating point number between 0 and 1
    """
    tn,fp,tp,fn = confusion_matrix(y_true, y_pred).ravel()
    return tn / (tn + fn)

# Regression summaries

def regression_summary(X, y_true, y_predicted):
    """
    Parameters:
    -----------
    X           : the X variables from the data : np.ndarray : :
    y_true      : the true y values             : np.ndarray : :
    y_predicted : the predicted y values        : np.ndarray : :

    Description:
    ------------
    Evaluates the regression model on four metrics (RMSE, MAE, Adjusted R^2, & R^2) & prints the results in a dataframe

    Returns:
    --------
    A dataframe containing the RMSE, MAE, R^2, & Adjusted R^2 for a regression model
    """
    rmse = sqrt(mean_squared_error(y, y_predicted))
    mae  = mean_absolute_error(y, y_predicted)
    r2   = r2_score(y, y_predicted)
    adjr2 = r2_adj(X, y, y_predicted)
    regression_summary = pd.DataFrame([rmse, mae, r2], index = ["RMSE", "MAE", "R2"], columns = ["Score"])
    return regression_summary

def scaled_regression_summary(y_true, y_predicted):
    """
    Parameters:
    -----------
    y_true      : the true y values             : np.ndarray : :
    y_predicted : the predicted y values        : np.ndarray : :

    Description:
    ------------
    Evaluates the regression model on three (RMSE, MAE, R^2) metrics & prints the results in a dataframe.  This does not incude the adjusted R^2 score
    because the columns from X_scaled cannot be readily extracted rendering the adjusted R^2 useless.

    Returns:
    --------
    A dataframe containing the RMSE, MAE, & R^2 for a regression model whose X variables have been scaled
    """
    rmse = sqrt(mean_squared_error(y, y_predicted))
    mae  = mean_absolute_error(y, y_predicted)
    r2   = r2_score(y, y_predicted)
    regression_summary = pd.DataFrame([rmse, mae, r2], index = ["RMSE", "MAE", "R2"], columns = ["Score"])
    return regression_summary

# Classification Summaries

"""
These are binary classification summaries since binary classification is most common.
If you would like a different summary to be added, please make a pull request or open an issue and ask for one to be made.
"""

def confusion_matrix_dataframe(y_true, y_predicted, columns, index):
    """
    Parameters:
    -----------
    y_true      : the true y values      : np.ndarray : :
    y_predicted : the predicted y values : np.ndarray : :
    columns     : column labels          : str        : :
    index       : row labels             : str :      : :
    
    Description:
    ------------
    Generates a confusion matrix through sklearn and transforms it into a Pandas dataframe.  The labels **must** be
    listed from negative to positive, i.e. [0,1]
    This can work with binary or multi-class classification.

    Returns:
    --------
    A Pandas dataframe of the sklearn's confusion_matrix.
    """
    cm = confusion_matrix(y_true, y_predicted)
    matrix = pd.DataFrame(cm, columns = columns, index = index)
    return matrix

def classification_summary(y_true, y_predicted):
    """
    Parameters:
    -----------
    y_true      : the true y values      : np.ndarray : :
    y_predicted : the predicted y values : np.ndarray : :

    Description
    -----------
    Evaluates the classifier on four metrics (recall/sensitivity, specificity, the Matthews correlation coefficient, & the AUC score) and returns the scores in
    a dataframe.  Accuracy is not included because it is not really that informative.
    """
    sen = recall_score(y, y_predicted)
    spe = specificity(y, y_predicted)
    mcc = matthews_corrcoef(y, y_predicted)
    auc = roc_auc_score(y, y_predicted)
    binary_classification_summary = pd.DataFrame([acc, sen, spe, mcc, auc], 
                                                 index = ["Sensitivity", "Specificity", "MCC", "AUROC"], 
                                                 columns = ["Scores"])
    return binary_classification_summary

# Evaluation Graphs

# Classification Models

def roc_curve(model_prob, X_test, y_test, y_predicted, title, dim, roc_color = "darkorange", baseline_color = "darkblue"):
    """
    Parameters:
    -----------
    model_prob     : the model used for prediction        :               : :
    X_test         : the X values                         : np.ndarray    : :
    y_test         : true y values                        : np.ndarray    : :
    y_predicted    : the model predictions                : np.ndarray    : :
    title          : title of the graph                   : str           : :
    dim            : tuple of the dimensions of the graph : int           : :
    roc_color      : color value of the ROC curve         : str           : :
    baseline_color : color value of the baseline          : str           : :

    Descriptions:
    -------------
    Plots a Receiver Operating Characteristic for a model and includes the AUROC score in the title.

    Returns:
    --------
    Creates a ROC graph for a given model's predictions and allows for appearance control.

    Credit:
    -------
    This code was modified from code written by Matt Brems during our lesson on classification metrics.
    """
    model_prob = [i[0] for i in model_prob.predict_proba(X_test)]
    model_pred_df = pd.DataFrame({"true_values": y_test, "pred_probs": model_prob})
    thresholds = np.linspace(0, 1, 500) 
    def true_positive_rate(df, true_col, pred_prob_col, threshold):
        true_positive = df[(df[true_col] == 1) & (df[pred_prob_col] >= threshold)].shape[0]
        false_negative = df[(df[true_col] == 1) & (df[pred_prob_col] < threshold)].shape[0]
        return true_positive / (true_positive + false_negative)
    def false_positive_rate(df, true_col, pred_prob_col, threshold):
        true_negative = df[(df[true_col] == 0) & (df[pred_prob_col] <= threshold)].shape[0]
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

def prc_curve(model_proba, y_true, y_predicted, dim, model_name, ns_line = "--", ns_color = "navy", prc_color = "darkorange"):
    """
    Parameters:
    -----------
    model_proba : probabilities generated by the model : list : np.ndarray : :
    y_true      : true y values                               : np.ndarray : :
    y_predicted : predicted y values                          : np.ndarray : :
    dim         : tuple of the graph's dimensions             : int        : :
    model_name  : name for the model used to make predictions : str        : :
    ns_line     : line style for the no skill predictor       : str        : :
    ns_color    : color for the no skill line predictor       : str        : :
    prc_color   : color for the prc curve line                : str        : : 

    Description:
    ------------
    Plots a precision-recall curve for a model and includes the average precision score in the title.

    Returns:
    --------
    Creates a  graph for a given model's predictions and allows for appearance control.
    """
    no_skill = len(y_true[y_true == 1]) / len(y_true)
    ap = average_precision_score(y_true, y_predicted)
    precision, recall, threshold = precision_recall_curve(y_true = y_true, probas_pred = np.array(model_proba[:,1]), pos_label = 1)
    plt.figure(figsize = (dim), facecolor = "white")
    plt.step([0,1], [no_skill, no_skill], label = "No Skill", linestyle = ns_line, color = ns_color)
    plt.step(recall, precision, label = "KNN", color = prc_color)
    plt.title(f"PRC For {model_name.capitalize()} With An AP Of {round(ap,2)}", size = 18)
    plt.xlabel("Recall", size = 16)
    plt.xticks(size = 14)
    plt.ylabel("Precision", size = 16)
    plt.yticks(size = 14)
    plt.legend(bbox_to_anchor = (1.04, 1), loc = "upper left", fontsize = 16)
    plt.tight_layout();

# Regression Models

def residualplots(df, columns, x, dim, titles, row, col, xlabel = "Actual", ylabel = "Predicted"):
    """
    Parameters:
    -----------
    df      : dataframe source of residuals      : dataframe : :
    columns : list of the predicted columns      : str       : :
    x       : the actual values                  : str       : :
    dim     : tuple of each plot's dimensions    : int       : :
    titles  : list of titles for each plot       : str       : :
    row     : how many rows will be generated    : int       : :
    col     : how many columns will be generated : int       : :
    xlabel  : label of the x-axis                : str       : :
    ylabel  : label of the y-axis                : str       : :

    Description:
    ------------
    This function is designed to be used with a dataframe of the residuals. 
    
    It plots the actual y-values on the x-axis and the predicted on the y-axis.

    Returns:
    --------
    n number of residual plots arranged by the rows and columns.
    """
    count = 0
    fig   = plt.figure(figsize = dim, facecolor = "white")
    for c, column in enumerate(columns):
        count += 1
        ax = fig.add_subplot(row, col, count)
        plt.title(f"{titles[c]}", size = 18)
        sns.residplot(x = x, y = column, data = df)
        plt.xlabel(f"{xlabel}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout();
    plt.show();