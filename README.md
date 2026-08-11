# 📁 Smart Download Folder Organizer

A simple Python automation tool that automatically organizes files in your Downloads folder based on their file extensions.

Instead of manually sorting downloaded files, this application identifies the file type and moves it into the appropriate category folder.

## ✨ Features

- 📄 Automatically organizes documents
- 🖼️ Organizes images
- 🎬 Organizes videos
- 🎵 Organizes audio files
- 📦 Organizes archive files
- 💻 Organizes application files
- 📁 Automatically creates required folders
- 🔤 Handles file extensions without case-sensitivity
- ⚡ Simple and lightweight
- 🐍 Built entirely with Python standard libraries

## 📂 Example

Before running the organizer:

```text
Downloads/
├── invoice.pdf
├── resume.docx
├── photo.jpg
├── vacation.png
├── movie.mp4
├── song.mp3
├── project.zip
└── setup.exe

After running the organizer:

Downloads/
├── Documents/
│   ├── invoice.pdf
│   └── resume.docx
│
├── Images/
│   ├── photo.jpg
│   └── vacation.png
│
├── Videos/
│   └── movie.mp4
│
├── Audio/
│   └── song.mp3
│
├── Archives/
│   └── project.zip
│
└── Applications/
    └── setup.exe
🛠️ Technologies Used
Python 3
pathlib
shutil

No external Python packages are required.

🚀 Getting Started
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/smart-download-organizer.git
2. Navigate to the project
cd smart-download-organizer
3. Run the application
python organizer.py

On Windows, you can also use:

py organizer.py
⚙️ How It Works

The application performs the following steps:

Downloads Folder
       ↓
Read Files
       ↓
Get File Extension
       ↓
Identify Category
       ↓
Create Destination Folder
       ↓
Move File

The application uses a dictionary to determine where each file type should be moved.

Example:

file_categories = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mp3": "Audio",
    ".zip": "Archives",
    ".exe": "Applications"
}
📁 Project Structure
smart-download-organizer/
│
├── organizer.py
├── README.md
└── .gitignore
