from pathlib import Path
downloads = Path.home() / "Downloads"
import shutil


folders =[
    "Documents",
    "Images",
    "Videos",
    "Music",
    "Archives",
    "Applications",
    "Others"
]


for folder in folders:
    folder_path = downloads / folder
    folder_path.mkdir(exist_ok=True)

print("Folders created successfully in the Downloads directory.")



file_categories = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".xlsx": "Documents",
    
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    
    ".mp4": "Videos",
    ".mkv": "Videos",
    
    ".mp3": "Audio",
    ".wav": "Audio",
    
    ".zip": "Archives",
    ".rar": "Archives",
    
    ".exe": "Applications"
}



for file in downloads.iterdir():
    if file.is_file():
        extension = file.suffix.lower()
        if extension in file_categories:
            category = file_categories[extension]
            destination_folder = downloads / category
            destination =  destination_folder / file.name
            shutil.move(file, destination)
            print(f"Moved: {file.name} -> {destination_folder}")             








# if(downloads.exists()):
#     print("Downloads folder exists.")
# else:
#     print("Downloads folder does not exist.")


# for file in downloads.iterdir():
#     print(file.name)

# for file in downloads.iterdir():
#     if file.is_file():
#         print(file.name,"->",file.suffix)
