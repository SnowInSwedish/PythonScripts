import os
import re

def rename_files(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(directory, filename)):
            # Extract relevant information from the filename using regular expressions
            match = re.search(r'(.+?) - (\d+)', filename)
            if match:
                book_name = match.group(1)
                chapter_number = match.group(2)
                
                # Construct the new filename
                new_filename = f"{book_name} - Chapter {chapter_number}.pdf"  # Modify this according to your preference
                
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed {filename} to {new_filename}")
            else:
                print(f"Skipping {filename} as it doesn't match the expected pattern")

# Provide the directory path where your manga files are stored
directory_path = "/path/to/your/manga/files"

# Call the function to rename files in the specified directory
rename_files(directory_path)
