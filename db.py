import pandas as pd

def load_data(n: int):
    return pd.read_csv("reviews.csv")