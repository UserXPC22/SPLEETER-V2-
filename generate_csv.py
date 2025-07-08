import os
import csv
import random

def collect_tracks(root_dir):
    entries = []
    for song in os.listdir(root_dir):
        song_path = os.path.join(root_dir, song)
        if not os.path.isdir(song_path):
            continue
        mixture = os.path.join(song_path, "mixture.wav")
        vocals = os.path.join(song_path, "vocals.wav")
        bass = os.path.join(song_path, "bass.wav")
        drums = os.path.join(song_path, "drums.wav")
        other = os.path.join(song_path, "other.wav")

        if all(os.path.exists(p) for p in [mixture, vocals, bass, drums, other]):
            # Save paths
            entries.append([mixture, vocals, drums, bass, other])
    return entries

# === Update these paths based on your actual folder structure ===
musdb_train_dir = r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\MUSDB18HQ\train"
sdx23_dir = r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\combined_dataset\moisesdb23_labelnoise_v1.0"
output_dir = r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data"

# Collect and combine dataset entries
all_entries = collect_tracks(musdb_train_dir) + collect_tracks(sdx23_dir)

# Shuffle and split into 80% train, 20% validation
random.shuffle(all_entries)
split_index = int(len(all_entries) * 0.8)
train_set = all_entries[:split_index]
valid_set = all_entries[split_index:]

# Function to write CSV
def write_csv(path, entries):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["mixture_path", "vocals_path", "drums_path", "bass_path", "other_path"])
        writer.writerows(entries)

# Write output CSV files
write_csv(os.path.join(output_dir, "train.csv"), train_set)
write_csv(os.path.join(output_dir, "valid.csv"), valid_set)

print(f"CSV files written successfully!")
print(f"Total samples: {len(all_entries)}")
print(f" - Training samples: {len(train_set)}")
print(f" - Validation samples: {len(valid_set)}")
