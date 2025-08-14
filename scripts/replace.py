import os
import re

# Directory where the YAML files are located
directory = './'  # Replace with your folder path

# Regular expression pattern to match '../' and replace it with 'modules/'
pattern = re.compile(r'\.\./')

def replace_relative_with_modules(file_path):
    """
    Replace '../' with 'modules/' in a given YAML file.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace all instances of '../' with 'modules/'
    updated_content = pattern.sub('Modules/', content)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

def update_all_files(directory):
    """
    Update all YAML files in the given directory.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                replace_relative_with_modules(file_path)
                print(f"Updated: {file_path}")

if __name__ == "__main__":
    update_all_files(directory)
    print("All files have been updated.")

