import os
import shutil
import random

# === Configuration ===
SOURCE_DATASET_DIR = r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\combined_dataset"
DEST_DIR = r"C:\Xavier Paul (School Works)\Computer Science\3rd year\THESIS\spleeter\data"
TRAIN_DIR = os.path.join(DEST_DIR, "train")
VAL_DIR = os.path.join(DEST_DIR, "validation")
TRAIN_RATIO = 0.8

# === Script Start ===
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VAL_DIR, exist_ok=True)

all_folders = [f for f in os.listdir(SOURCE_DATASET_DIR) if os.path.isdir(os.path.join(SOURCE_DATASET_DIR, f))]
random.shuffle(all_folders)
split_index = int(len(all_folders) * TRAIN_RATIO)
train_folders = all_folders[:split_index]
val_folders = all_folders[split_index:]

# Copy train data
for folder in train_folders:
    src = os.path.join(SOURCE_DATASET_DIR, folder)
    dst = os.path.join(TRAIN_DIR, folder)
    shutil.copytree(src, dst)
    print(f"📁 Copied to train: {folder}")

# Copy validation data
for folder in val_folders:
    src = os.path.join(SOURCE_DATASET_DIR, folder)
    dst = os.path.join(VAL_DIR, folder)
    shutil.copytree(src, dst)
    print(f"📁 Copied to validation: {folder}")

print("\n✅ Dataset split complete!")
