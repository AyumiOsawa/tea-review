import pandas as pd

def load_data(n: int):
    df = pd.read_csv(
                "reviews.csv",
                dtype={'date_added': str})
    df['date_added'] = pd.to_datetime(df['date_added'], format='%Y%m%d')
    df['flavour'] = df['flavour'].apply(lambda string: string.split('&'))
    return df