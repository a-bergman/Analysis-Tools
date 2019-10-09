import pandas        as pd
from sklearn.metrics import confusion_matrix, r2_score

###

# Regression Metrics

def r2_adj(X, y, y_predicted):
    """
    Parameters:
    -----------
        X           : the X variables 
        y           : the true values
        y_predicted : model predictions

    Description:
    ------------
    Calculates an adjusted R^2 score which is scaled to the number of features in the model: the R^2 score is often inflated by a large number of features.

    Returns:
    --------
    The coefficient of correlation: a floating point number between 0 and 1.
        
    """
    r2     = r2_score(y_true, y_predicted)
    r2_adj = 1 - ((1 - r2) * (len(y) - 1)) / (len(y) - len(X.columns)) - 1
    return r2_adj

# Classification Metrics

def confusion_matrix_dataframe(y, y_predicted, columns, index):
    """
    Parameters:
    -----------
    y           : the true values
    y_predicted : model predictions
    columns     : column labels; should be [negative, positive]
    index       : row labels; should be [negative, positivee]
    
    Description:
    ------------
    Generates a confusion matrix through sklearn and transforms it into a Pandas dataframe.

    Returns:
    --------
    Returns a Pandas dataframe of the sklearn's `confusion_matrix` making it easier to read
        
    """
    cm     = confusion_matrix(y, y_predicted)
    matrix = pd.DataFrame(cm, columns = columns, index   = columns)
    return matrix

def specificity(y, y_pred):
    """
    Parameters:
    -----------
    y           : the true values
    y_predicted : model predictions

    Description:
    ------------
    Calculates the percentage of negatives that are correctly classified as being negative. A confusion matrix generated and is the score (TN / TN + FP) is calculated.

    Returns:
    --------
    The specificity score: a floating point number between 0 and 1
    
    """
    cm          = confusion_matrix(y, y_pred)  
    specificity = cm[0,0] / (cm[0,0] + cm[0,1])
    return specificity