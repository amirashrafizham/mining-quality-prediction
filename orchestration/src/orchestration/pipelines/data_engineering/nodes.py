"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.3
"""

import pandas as pd


# Convert date column to datetime
def convert_to_datetime(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d %H:%M:%S")
    return df


# Convert other columns to float
def convert_to_float(df: pd.DataFrame) -> pd.DataFrame:
    df.set_index("date", inplace=True)
    # Convert ',' to '.' and convert to float
    for col in df.columns:
        df[col] = df[col].str.replace(",", ".").astype(float)
    print(df.dtypes)
    return df
