import os
import zipfile

def zip_subfolders(base_path, start_index, end_index):
    """
    Compresses subfolders in a specified range within a base directory.
    
    Args:
    base_path (str): The path to the directory containing the subfolders.
    start_index (int): The starting index of subfolders to compress.
    end_index (int): The ending index of subfolders to compress.
    """
    # Iterate through the range of indices
    for i in range(start_index, end_index + 1):
        folder_name = f"PT{str(i).zfill(4)}"
        folder_path = os.path.join(base_path, folder_name)
        
        # Check if the folder exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # Define the path for the output zip file
            zip_file_path = os.path.join(base_path, f"{folder_name}.zip")
            
            # Create the zip file
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        # Create the full path to the file
                        file_path = os.path.join(root, file)
                        # Add file to the zip file
                        zipf.write(file_path, os.path.relpath(file_path, start=folder_path))
            print(f"Folder {folder_name} has been zipped as {zip_file_path}")
        else:
            print(f"Folder {folder_name} does not exist or is not a directory.")

# Example usage:
base_directory = r"H:\CCSI\PlanningModule\Brachy Projects\1. CIHR MDBC Collaboration\Prostate Patients\Prostate Patients (Matt 2022-2020)"
start_idx = 161  # Starting index of patient folders
end_idx = 251  # Ending index of patient folders

zip_subfolders(base_directory, start_idx, end_idx)
