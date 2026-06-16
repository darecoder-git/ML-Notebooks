# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

# print("Path to dataset files:", path)

import os
import shutil
import kagglehub

# 1. Download to default cache
downloaded_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

# 2. Define your target destination
destination_folder = "/Users/purkayastha7/Desktop/Codes/SQL_INTERPRETER/data/raw"

# 3. Move the files
if os.path.exists(destination_folder):
    shutil.move(downloaded_path, destination_folder)
    print(f"Files successfully moved to: {destination_folder}")
else:
    print("Destination folder already exists.")
