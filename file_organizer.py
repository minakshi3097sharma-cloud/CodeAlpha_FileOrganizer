import os
import shutil

# File categories with extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Code_Files": [".py", ".html", ".css", ".js", ".java", ".cpp", ".c"],
    "Compressed": [".zip", ".rar", ".7z"],
    "Others": []
}

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder path does not exist!")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            category = get_category(file_extension)

            category_folder = os.path.join(folder_path, category)
            create_folder(category_folder)

            destination = os.path.join(category_folder, filename)

            if os.path.exists(destination):
                name, ext = os.path.splitext(filename)
                destination = os.path.join(category_folder, name + "_copy" + ext)

            shutil.move(file_path, destination)
            files_moved += 1
            print(f"Moved: {filename} → {category}")

    print("\nFile organization completed!")
    print(f"Total files moved: {files_moved}")

def main():
    print("===== Automatic File Organizer =====")
    folder_path = input("Enter folder path to organize: ")

    organize_files(folder_path)

if __name__ == "__main__":
    main()
