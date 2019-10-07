import pandas        as pd
from sklearn.metrics import confusion_matrix, r2_score

###

def r2_adj(X, y_true, y_predicted):
    r2     = r2_score(y_true, y_predicted)
    r2_adj = 1 - ((1 - r2) * (len(y) - 1)) / (len(y) - len(X.columns)) - 1
    return r2_adj

def gen_confusion_matrix(y, y_preds, columns, index):
    cm     = confusion_matrix(y, y_preds)
    matrix = pd.DataFrame(cm, columns = columns, index   = columns)
    return matrix

def specificity(y, y_pred):
    cm          = confusion_matrix(y, y_pred)  
    specificity = cm[0,0] / (cm[0,0] + cm[0,1])
    return specificity