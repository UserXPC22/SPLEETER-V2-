import pandas as pd

for csv_path in [
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\train.csv",
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\valid.csv"
]:
    df = pd.read_csv(csv_path)
    print(f"Unique duration values in {csv_path}: {df['duration'].unique()}")
    print(df['duration'].apply(type).value_counts())