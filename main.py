
from pathlib import Path
import shutil

# File extensions and their destination folders
FILE_TYPES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Documents": [".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []
}


def get_folder(extension):
    """Find the correct folder for a file extension."""
    for folder, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return folder
    return "Others"


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Error: Folder does not exist!")
        return

    moved = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        # Keep the Python project files untouched
        if file.name in ["main.py", "README.md", ".gitignore"]:
            continue

        destination_folder = folder / get_folder(file.suffix)
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file.name

        # Prevent overwriting files with the same name
        counter = 1
        while destination.exists():
            destination = destination_folder / (
                f"{file.stem}_{counter}{file.suffix}"
            )
            counter += 1

        try:
            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name} -> {destination_folder.name}")
            moved += 1

        except OSError as error:
            print(f"Could not move {file.name}: {error}")

    print(f"\nOrganization complete! {moved} files moved.")


if __name__ == "__main__":
    print("===== AUTOMATIC FILE ORGANIZER =====")
    path = input("Enter the folder path to organize: ")
    organize_files(path)
