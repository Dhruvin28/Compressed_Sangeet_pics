import os
import json

# Specify the folder path
folder_path = './'

# Get the list of all files in the folder
file_names = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

# Create a dictionary to store the file names
files_data = {
    'files': file_names
}

# Specify the path for the output JSON file
json_file_path = 'files_list.json'

# Write the file names into the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(files_data, json_file, indent=4)

print(f"File names from {folder_path} have been saved to {json_file_path}")
