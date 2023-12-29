import os

def rename_files(folder_path, pattern):
    files = os.listdir(folder_path)

    for filename in files:
        new_name = {pattern}
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print("Renamed", {filename}, "to", {new_name})
        
    

folder_to_rename = input("Enter your folder path:")

folder_new_name = input("Enter the folders new name:")

rename_files(folder_to_rename, folder_new_name) 
