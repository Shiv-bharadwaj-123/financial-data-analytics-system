import pandas as pd
import os
import sqlite3

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

def preprocess_data(df):
    # Sort by date
    df = df.sort_values(by='date')

    # Create month column
    df['month'] = df['date'].dt.month

    # Create day index (for ML models)
    df['day_index'] = range(len(df))

    return df

def save_to_sql(df):
    conn = sqlite3.connect("finance.db")

    df.to_sql("transactions", conn, if_exists="replace", index=False)

    conn.close()