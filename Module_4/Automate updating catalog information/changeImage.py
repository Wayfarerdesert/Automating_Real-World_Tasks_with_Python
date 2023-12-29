#!/usr/bin/env python3

from PIL import Image
import os

img_folder = "supplier-data/images"
# output_folder = "supplier-data/images"

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

if os.path.exists(img_folder):
    for i in os.listdir(img_folder):
        img_path = os.path.join(img_folder, i)
        if os.path.isfile(img_path):
            try:
                img = Image.open(img_path)
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                output_filename = f"{i.split('.')[0]}.jpeg"
                output_path = os.path.join(img_folder, output_filename)
                img.resize((600,400)).save(output_path, format="JPEG")
                print(f"Processed {i} finished sucsesfully")
            except Exception as e:
                print(f"Error processing {i}: {e}")
else:
    print(f"Folder path '{img_folder}' does not exist.")
