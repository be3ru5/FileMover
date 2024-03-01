#!/usr/bin/python3

import os
import shutil

def files_move(source, dest, extensions):
    for source_folder in source:
        files = os.listdir(source_folder)       
        for file in files:
            _, file_extension = os.path.splitext(file)
            if file_extension.lower() in extensions:
                source_path = os.path.join(source_folder, file)
                destination_path = os.path.join(dest, file)
                shutil.move(source_path, destination_path)
                print(f"[*] Moved '{file}' from '{source_folder}' to '{dest}'.")

if __name__ == "__main__":
    source = ["C:\\Users\\lalit\\OneDrive\\Desktop", "C:\\Users\\lalit\\Downloads"]
    dest = "C:\\Users\\lalit\\OneDrive\\Documents\\tmp"
    extensions = [".pdf", ".txt", ".docx", ".xlsx", ".ppt"] 

    files_move(source, dest, extensions)
