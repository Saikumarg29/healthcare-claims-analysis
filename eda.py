"""
Script for exploratory data analysis on healthcare claims
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_claim_type_distribution(df):
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x='ClaimType', order=df['ClaimType'].value_counts().index)
    plt.title("Claim Count by Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../visuals/claim_type_distribution.png")

def plot_monthly_claim_trends(df):
    df['Month'] = df['ClaimDate'].dt.to_period('M').astype(str)
    monthly_sum = df.groupby('Month')['ClaimAmount'].sum()
    monthly_sum.plot(kind='line', title='Monthly Claim Amounts', figsize=(10,5))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../visuals/monthly_trends.png")

if __name__ == "__main__":
    df = pd.read_csv("../data/claims_data_cleaned.csv", parse_dates=['ClaimDate'])
    plot_claim_type_distribution(df)
    plot_monthly_claim_trends(df)
