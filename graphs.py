# Imports 

import seaborn           as sns
import numpy             as np
import matplotlib.pyplot as plt
from sklearn.metrics     import roc_auc_score

#####

"""Setting the basic appearance for the graphs"""

sns.set(style = "white", palette = "deep")

#####

def histograms(columns, df, titles, labels, ylabel, ticks, row, col):
    """Creates histograms for continuous data"""
    count = 0
    fig   = plt.figure(figsize = (14,7), facecolor = "white")
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        plt.title(f"Distribution Of {titles[c]}", size = 18)
        sns.distplot(df[column], color = "black", kde = False)
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def boxplots(columns, df, titles, labels, ticks, row, col):
    """Creates boxplots for continuous data"""
    count = 0
    fig   = plt.figure(figsize = (14,7, facecolor = "white"))
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        plt.title(f"{titles[c]}", size = 18)
        sns.boxplot(df[column])
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def regressionplots(columns, y, df, titles, labels, ylabel, ticks, row, col, mark, ci = None):
    """Creates regression plots for continuous data."""
    count = 0
    fig   = plt.figure(figsize = (14,7), facecolor = "white")
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        plt.title(f"{titles[c]}", size = 18)
        sns.regplot(x = column, y = y, data = df, fit_reg = True,  marker = mark, color = "black", line_kws = {"color": "red"}, ci = ci)
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(ticks = ticks[c], size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def countplots(columns, df, titles, labels, ylabel, row, col):
    """Creates a count plot for categorical data.  This type of plot explicityly counts the categories in a dataframe column."""
    fig   = plt.figure(figsize = (20,30), facecolor = "white")
    count = 0
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        title = titles[c]
        plt.title(f"{title}", size = 18)
        sns.countplot(df[column])
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def barplots(df, x, y, labels, ylabel, titles, row, col):
    """Generates barplots for categorical data"""
    fig   = plt.figure(figsize = (20,30), facecolor = "white")
    count = 0
    for c, column in enumerate(columns):
        count += 1
        ax    = fig.add_subplot(row, col, count)
        title = titles[c]
        plt.title(f"{title}", size = 18)
        sns.barplot(x = x, y = y, data = df)
        plt.xlabel(f"{labels[c]}", size = 16)
        plt.ylabel(f"{ylabel}", size = 16)
        plt.xticks(size = 14)
        plt.yticks(size = 14)
    plt.tight_layout()
    plt.show();

#####

def heatmap(df, columns, title, vmin, vmax):
    """Creates a heatmap for dataframe columns.  The visualization includes a a correlation bar for, annotations, and is not mirrored."""
    plt.figure(figsize = (16,8), facecolor = "white")
    plt.title(f"title", size = 18)
    corr = df[columns].corr()
    mask = np.zeros_like(corr)                                                                                
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        sns.heatmap(corr, cmap = "RdBu", mask = mask, vmin = vmin, vmax = vmax, annot = True)
    plt.xticks(size = 14)
    plt.yticks(size = 14);

#####  The ROC curve code was modified from code written by Matt Brems during our lesson on classification metrics.

def roc_curve(model_prob, X_test, y_test, y_pred, title, roc_color = "darkorange", baseline_color = ):
    """Creates a ROC-AUC curve with the AUROC score included in the title."""
        model_prob    = [i[0] for i in model_prob.predict_proba(X_test)]
        model_pred_df = pd.DataFrame({"true_values": y_test, "pred_probs": model_prob})
    thresholds = np.linspace(0, 1, 500) 
    def true_positive_rate(df, true_col, pred_prob_col, threshold):
        true_positive  = df[(df[true_col] == 1) & (df[pred_prob_col] >= threshold)].shape[0]
        false_negative = df[(df[true_col] == 1) & (df[pred_prob_col] < threshold)].shape[0]
        return true_positive / (true_positive + false_negative)
    def false_positive_rate(df, true_col, pred_prob_col, threshold):
        true_negative  = df[(df[true_col] == 0) & (df[pred_prob_col] <= threshold)].shape[0]
        false_positive = df[(df[true_col] == 0) & (df[pred_prob_col] > threshold)].shape[0]
        return 1 - (true_negative / (true_negative + false_positive))
    tpr_values = [true_positive_rate(model_pred_df, "true_values", "pred_probs", prob) for prob in thresholds]
    fpr_values = [false_positive_rate(model_pred_df, "true_values", "pred_probs", prob) for prob in thresholds]
    plt.figure(figsize   = (13,7), facecolor = "white")
    plt.plot(fpr_values, tpr_values, color = roc_color, label = "ROC Curve")
    plt.plot(np.linspace(0, 1, 500), np.linspace(0, 1, 500), color = baseline_color, label = "Baseline")
    rocauc_score = round(roc_auc_score(y_test, y_preds), 5)
    plt.title(f"{title} With A Score of {}", fontsize = 18)
    plt.ylabel("Sensitivity", size = 16)
    plt.xlabel("1 - Specificity", size = 16)
    plt.xticks(size = 14)
    plt.yticks(size = 14)
    plt.legend(bbox_to_anchor = (1.04, 1), loc = "upper left", fontsize = 16)
    plt.tight_layout()