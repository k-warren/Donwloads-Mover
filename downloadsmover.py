import os
import shutil
import time as t
from plyer import notification

def move_files():

# Define the downloads directory
    downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    files_moved = []

    # Define the file types and their corresponding folders
    file_types = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav', '.ogg'],
        'Compressed': ['.zip', '.rar', '.7z'],
        'Executables': ['.exe', '.msi'],
        'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css'],
        '3D Files': ['.stl', '.obj', '.3mf'],
    }


    # Move the files to their corresponding folders
    for filename in os.listdir(downloads_dir):
        file_path = os.path.join(downloads_dir, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    if file_extension == '.py':
                        shutil.move(file_path, r"c:\Users\Kieran\Code\Python")
                        files_moved.append([file_path, r"c:\Users\Kieran\Code\Python"])
                    elif file_extension == '.java':
                        shutil.move(file_path, r"c:\Users\Kieran\Code\Java")
                        files_moved.append([file_path, r"c:\Users\Kieran\Code\Java"])
                    elif file_extension == '.cpp':
                        shutil.move(file_path, r"c:\Users\Kieran\Code\C++")
                        files_moved.append([file_path, r"c:\Users\Kieran\Code\C++"])
                    elif file_extension == '.c':
                        shutil.move(file_path, r"c:\Users\Kieran\Code\C")
                        files_moved.append([file_path, r"c:\Users\Kieran\Code\C"])
                    elif file_extension == '.js':
                        shutil.move(file_path, r"c:\Users\Kieran\Code\JavaScript")
                        files_moved.append([file_path, r"c:\Users\Kieran\Code\JavaScript"])
                    elif file_extension == '.html':
                        shutil.move(file_path, r"c:\Users\Kieran\Code\html")
                        files_moved.append([file_path, r"c:\Users\Kieran\Code\html"])
                    elif file_extension == '.css':
                        shutil.move(file_path, r"c:\Users\Kieran\Code\css")
                        files_moved.append([file_path, r"c:\Users\Kieran\Code\css"])
                    elif file_extension == '.stl':
                        shutil.move(file_path, r"c:\Users\Kieran\3D Files\stl")
                        files_moved.append([file_path, r"c:\Users\Kieran\3D Files\stl"])
                    elif file_extension == '.obj':
                        shutil.move(file_path, r"c:\Users\Kieran\3D Files\obj")
                        files_moved.append([file_path, r"c:\Users\Kieran\3D Files\obj"])
                    elif file_extension =='.3mf':
                        shutil.move(file_path, r"c:\Users\Kieran\3D Files\3mf")
                        files_moved.append([file_path, r"c:\Users\Kieran\3D Files\3mf"])
                    else:
                        shutil.move(file_path, r"c:\Users\Kieran\Other")
                        files_moved.append([file_path, r"c:\Users\Kieran\Other"])



    if len(files_moved) == 0:
        print("No files were moved")
    else:
        for file_info in files_moved:
            file_name = os.path.basename(file_info[0])  # Extract the file name from the path
            file_location = file_info[1]
            try:
                notification.notify(
                title="Downloads Moved",
                message=f"Moved {file_name} to {file_location}.",
                app_name="File Organizer",
                timeout=10
                )
                print(f"Moved {file_name} to {file_location}")
            except Exception as e:
                print(f"Notification failed: {e}")
