import pandas as pd
import soundfile as sf
import os

MIN_DURATION = 30  # seconds, change if needed

csv_files = [
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\train.csv",
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\valid.csv"
]

for csv_path in csv_files:
    print(f"Processing {csv_path} ...")
    df = pd.read_csv(csv_path)
    keep_rows = []
    for idx, row in df.iterrows():
        mix_path = row['mixture_path']
        if not os.path.exists(mix_path):
            print(f"  Skipping missing file: {mix_path}")
            continue
        try:
            info = sf.info(mix_path)
            duration = info.frames / info.samplerate
            if duration >= MIN_DURATION:
                keep_rows.append(row)
            else:
                print(f"  Removing {mix_path} (only {duration:.2f} seconds)")
        except Exception as e:
            print(f"  Error reading {mix_path}: {e}")
    new_df = pd.DataFrame(keep_rows)
    new_df.to_csv(csv_path, index=False)
    print(f"  Saved filtered CSV with {len(new_df)} rows.\n")

print("Done filtering short audio files from CSVs.")