import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np


def plot_churn_summary(df, col, order=None):
    counts = df.groupby(col)['Churn'].value_counts().unstack()
    rates = df.groupby(col)['Churn'].mean()
    totals = df[col].value_counts()

    counts.columns = ['No Churn', 'Churn']

    if order is not None:
        counts = counts.loc[order]
        rates = rates.loc[order]
        totals = totals.loc[order]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    counts.plot(kind='bar', ax=axes[0])
    axes[0].set_title(f'Churn vs No Churn by {col}')
    axes[0].tick_params(axis='x', rotation=45)

    axes[1].bar(rates.index, rates.values)
    axes[1].set_title(f'Churn Rate by {col}')
    axes[1].tick_params(axis='x', rotation=45)

    axes[2].bar(totals.index, totals.values)
    axes[2].set_title(f'Total Customers by {col}')
    axes[2].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()
    
def plot_box_churn(colx, coly, df):
    sns.boxplot(x=colx, y=coly, data=df)
    plt.title(f'{coly.replace("_", " ").capitalize()} by Churn Status')
    plt.show()