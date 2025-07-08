import pandas as pd

for csv_path in [
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\train.csv",
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\valid.csv"
]:
    df = pd.read_csv(csv_path)
    df['duration'] = 30  # or use the actual duration if you want
    df.to_csv(csv_path, index=False)
print("Added 'duration' column to train.csv and valid.csv")
