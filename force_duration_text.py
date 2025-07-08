for csv_path in [
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\train.csv",
    r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data\valid.csv"
]:
    with open(csv_path, 'r') as f:
        lines = f.readlines()
    # Replace .0 at the end of each line (for duration column)
    new_lines = []
    for line in lines:
        # Only replace if line is not the header
        if line.strip().endswith('.0'):
            line = line.rstrip()
            line = line[:-2] + '\n'  # Remove .0 and keep newline
        new_lines.append(line)
    with open(csv_path, 'w') as f:
        f.writelines(new_lines)
print("FORCED 'duration' column to be int (no .0) in train.csv and valid.csv (text mode)")