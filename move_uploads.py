import os
import shutil
import sys

def move_media_files(source_folder):
    """
    Moves JPG and MP4 files from the given folder to
    a sibling folder with the same name + '-upload'.
    """

    source_folder = os.path.abspath(source_folder)

    parent_dir = os.path.dirname(source_folder)
    folder_name = os.path.basename(source_folder)

    # Create sibling folder: FolderName-upload
    upload_folder = os.path.join(parent_dir, folder_name + "-upload")
    os.makedirs(upload_folder, exist_ok=True)

    extensions = {".jpg", ".jpeg", ".mp4"}

    for file in os.listdir(source_folder):
        file_lower = file.lower()

        if any(file_lower.endswith(ext) for ext in extensions):
            src = os.path.join(source_folder, file)
            dst = os.path.join(upload_folder, file)
            print(f"Moving: {src} -> {dst}")
            shutil.move(src, dst)

    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 move_uploads.py /path/to/folder")
        sys.exit(1)

    folder_path = sys.argv[1]
    move_media_files(folder_path)