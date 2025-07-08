import pandas as pd

for csv_path in [
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\train.csv",
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\valid.csv"
]:
    df = pd.read_csv(csv_path)
    # Convert duration to int, then to string, then back to int to ensure no .0
    df['duration'] = df['duration'].apply(lambda x: int(float(x)))
    # Save with no index and no float formatting
    df.to_csv(csv_path, index=False, float_format='%.0f')
print("FORCED 'duration' column to be int (no .0) in train.csv and valid.csv")
