import pandas as pd
import os

def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "data", "finance.csv")
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # Remove missing values
    df.dropna(inplace=True)

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    return df