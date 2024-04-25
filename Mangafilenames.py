import os
import re

def extract_info(filename):
    # Extract relevant information from the filename using regular expressions
    match = re.search(r'(.+?)_(Ch|Chapter|Chap)?_?(\d+)', filename)
    if match:
        manga_name = match.group(1).replace('_', ' ')
        chapter_number = match.group(3)
        return manga_name, chapter_number
    else:
        return None, None

def rename_files(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(directory, filename)):
            manga_name, chapter_number = extract_info(filename)
            if manga_name and chapter_number:
                # Construct the new filename
                new_filename = f"{manga_name} - Chapter {chapter_number}.pdf"
                
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed {filename} to {new_filename}")
            else:
                print(f"Skipping {filename} as it doesn't match the expected pattern")
                # Prompt the user for manual input
                manga_name = input("Please enter the manga name: ")
                chapter_number = input("Please enter the chapter number: ")
                
                # Construct the new filename
                new_filename = f"{manga_name} - Chapter {chapter_number}.pdf"
                
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed {filename} to {new_filename}")

# Provide the directory path where your manga files are stored
directory_path = "/path/to/your/manga/files"

# Call the function to rename files in the specified directory
rename_files(directory_path)
