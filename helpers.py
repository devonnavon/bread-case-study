import pandas as pd

def get_date_range(df, date_column):
    max_date = df[date_column].max()
    min_date = df[date_column].min()
    return f'{min_date} to {max_date}'

