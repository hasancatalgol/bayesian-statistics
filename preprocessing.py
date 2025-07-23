import pandas as pd

def normalize_features(X):
    return (X - X.mean()) / X.std()
