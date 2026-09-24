import numpy as np
from typing import Tuple

def Gini(y):
    _, counts = np.unique(y, return_counts=True)
    total_labels = len(counts)

    probabilities = counts / total_labels

    return 1 - np.sum(probabilities ** 2)

def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    """Return the (feature_index, threshold) that minimises weighted Gini impurity."""
    n_samples, n_features= X.shape
    best_threshold = 0.0
    best_feature = 0
    best_gini_value = float('inf')

    if n_samples <= 1:
        return 0, 0.0

    for feature_idx in range(n_features):
        X_columns = X[:, feature_idx]
        thresholds = np.unique(X_columns)
        for threshold in thresholds:
            left_mask = X_columns <= threshold
            right_mask = ~left_mask
            
            y_left, y_right = y[left_mask], y[right_mask]
            n_left, n_right = len(y_left), len(y_right)
            
            if n_left == 0 or n_right == 0:
                continue
            
            gini_value = ((n_left / n_samples) * Gini(y_left)) + ((n_right / n_samples) * Gini(y_right))
            if gini_value < best_gini_value:
                best_gini_value = gini_value
                best_threshold = threshold
                best_feature = feature_idx


    return best_feature, float(best_threshold)