import pandas        as pd
from sklearn.metrics import confusion_matrix, r2_score

###

# Regression Metrics

def r2_adj(X, y_true, y_predicted):
    """Calculates an adjusted R^2 score which is scaled to the number of features in the model: the R^2 score is often inflated by a large number of features."""
    r2     = r2_score(y_true, y_predicted)
    r2_adj = 1 - ((1 - r2) * (len(y) - 1)) / (len(y) - len(X.columns)) - 1
    return r2_adj

# Classification Metrics

def gen_confusion_matrix(y, y_preds, columns, index):
    """An improvement on the standard SKLearn confusion matrix which returns a Pandasd dataframe and includes labels."""
    cm     = confusion_matrix(y, y_preds)
    matrix = pd.DataFrame(cm, columns = columns, index   = columns)
    return matrix

def specificity(y, y_pred):
    """Evaluates the number of true negatives out of all negatives.  This score is not available in SKLearn."""
    cm          = confusion_matrix(y, y_pred)  
    specificity = cm[0,0] / (cm[0,0] + cm[0,1])
    return specificity