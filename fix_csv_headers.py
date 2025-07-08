import csv

for csv_path in [
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\train.csv",
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\valid.csv"
]:
    with open(csv_path, 'r', newline='', encoding='utf-8') as infile:
        rows = list(csv.reader(infile))
    # Replace the header with the correct one
    rows[0] = [
        "mixture_path",
        "vocals_path",
        "drums_path",
        "bass_path",
        "other_path",
        "duration"
    ]
    with open(csv_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)
    print(f"Fixed header in {csv_path}")

print("All CSV headers fixed!")