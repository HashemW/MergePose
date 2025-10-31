import shutil
from pathlib import Path

def flatten_dataset(source_base_dir: str, target_base_dir: str):
    """
    Reorganizes a dataset by flattening video-specific subfolders by moving files.

    From:
        dataset/train/images/video_name_1/
        dataset/train/labels/video_name_1/
        ... (and same for valid)
    To:
        new_dataset/train/images/0.jpg, 1.jpg, ...
        new_dataset/train/labels/0.txt, 1.txt, ...
        ... (and same for valid)

    Args:
        source_base_dir (str): The path to the root directory of the original dataset.
        target_base_dir (str): The path where the new, flattened dataset will be created.
    """
    source_path = Path(source_base_dir)
    target_path = Path(target_base_dir)

    if not source_path.is_dir():
        print(f"❌ Error: Source directory not found at '{source_path}'")
        return

    print(f"Source directory: {source_path.resolve()}")
    print(f"Target directory: {target_path.resolve()}")

    # Process both 'train' and 'valid' splits
    for split in ['train', 'valid']:
        print(f"\n--- Processing '{split}' split ---")

        # Define source paths for this split
        source_images_split_dir = source_path / split / 'images'
        source_labels_split_dir = source_path / split / 'labels'

        # Check if the source directory for the split exists
        if not source_images_split_dir.is_dir():
            print(f"🤷‍♀️ No 'images' directory found for '{split}' split. Skipping.")
            continue

        # Define and create the new destination directories for this split
        target_images_dir = target_path / split / 'images'
        target_labels_dir = target_path / split / 'labels'
        target_images_dir.mkdir(parents=True, exist_ok=True)
        target_labels_dir.mkdir(parents=True, exist_ok=True)

        # Counter for sequentially naming the new files within this split
        file_counter = 0

        # Get all video subdirectories from the source images folder for this split
        video_dirs = sorted([d for d in source_images_split_dir.iterdir() if d.is_dir()])

        if not video_dirs:
            print(f"⚠️ Warning: No video subdirectories found in '{source_images_split_dir}'.")
            continue

        # Iterate through each video's folder
        for video_dir in video_dirs:
            video_name = video_dir.name
            print(f"  📂 Scanning: {split}/images/{video_name}")
            
            # Define the corresponding labels directory for the current video
            current_video_labels_dir = source_labels_split_dir / video_name
            
            if not current_video_labels_dir.is_dir():
                print(f"  ⚠️ Warning: Missing labels directory for video '{video_name}'. Skipping video.")
                continue

            # Get a sorted list of image files to maintain image-label pairs
            image_files = sorted(video_dir.glob('*'))

            for img_path in image_files:
                # Assume label has the same filename stem but with a .txt extension
                label_path = current_video_labels_dir / f"{img_path.stem}.txt"

                if not label_path.exists():
                    print(f"    ⚠️ Warning: Missing label for '{img_path.name}'. Skipping file.")
                    continue

                # Define new destination paths with sequential filenames
                dest_img_path = target_images_dir / f"{file_counter}{img_path.suffix}"
                dest_label_path = target_labels_dir / f"{file_counter}.txt"

                # Move the image and its corresponding label
                shutil.move(img_path, dest_img_path)
                shutil.move(label_path, dest_label_path)

                file_counter += 1
        
        print(f"--- Finished '{split}' split. Moved {file_counter} image/label pairs. ---")

    print("\n✅ Dataset reorganization complete!")


# --- Example Usage ---
# Create dummy directories and files for testing
# (You can comment this part out and just use your real data)
# print("Setting up a dummy source dataset for demonstration...")
# source_dir = Path("source_dataset")
# (source_dir / "train/images/video_1").mkdir(parents=True, exist_ok=True)
# (source_dir / "train/labels/video_1").mkdir(parents=True, exist_ok=True)
# (source_dir / "valid/images/video_1").mkdir(parents=True, exist_ok=True)
# (source_dir / "valid/labels/video_1").mkdir(parents=True, exist_ok=True)
# (source_dir / "train/images/video_1/frame_a.jpg").touch()
# (source_dir / "train/labels/video_1/frame_a.txt").touch()
# (source_dir / "valid/images/video_1/frame_b.png").touch()
# (source_dir / "valid/labels/video_1/frame_b.txt").touch()

# Call the function
# flatten_dataset(source_base_dir="source_dataset", target_base_dir="new_flattened_dataset")

SOURCE_DIR = "/"
TARGET_DIR = "/"

flatten_dataset(SOURCE_DIR, TARGET_DIR)