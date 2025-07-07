"""
Script to load and clean healthcare claims data
"""
import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    df['ClaimDate'] = pd.to_datetime(df['ClaimDate'])
    df['ClaimAmount'] = df['ClaimAmount'].abs()
    df = df.dropna()
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    df = load_data("../data/claims_data.csv")
    df_cleaned = clean_data(df)
    save_cleaned_data(df_cleaned, "../data/claims_data_cleaned.csv")
