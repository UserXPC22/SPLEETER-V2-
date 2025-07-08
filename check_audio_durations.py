import pandas as pd
import soundfile as sf

csv_path = r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\train.csv"
df = pd.read_csv(csv_path)
for idx, row in df.iterrows():
    try:
        f = row['mixture_path']
        info = sf.info(f)
        duration = info.frames / info.samplerate
        if duration < 30:
            print(f"File {f} is only {duration:.2f} seconds long!")
    except Exception as e:
        print(f"Error reading {row['mixture_path']}: {e}")

print("Done checking train.csv. Now checking valid.csv...")

csv_path = r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\valid.csv"
df = pd.read_csv(csv_path)
for idx, row in df.iterrows():
    try:
        f = row['mixture_path']
        info = sf.info(f)
        duration = info.frames / info.samplerate
        if duration < 30:
            print(f"File {f} is only {duration:.2f} seconds long!")
    except Exception as e:
        print(f"Error reading {row['mixture_path']}: {e}")

print("Done checking valid.csv.")
