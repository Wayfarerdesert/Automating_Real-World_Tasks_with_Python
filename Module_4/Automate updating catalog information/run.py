#!/usr/bin/env python3
import os
import requests

url = "http://34.125.33.8/fruits/"
desc_folder = "supplier-data/descriptions"
img_folder = "supplier-data/images"


def analyse_description_file(txt_path, img_folder):
    try:
        img_file = os.path.basename(txt_path).split('.')[0] + '.jpeg'
        img_path = os.path.join(img_folder, img_file)

        print(f"Processing file: {txt_path}")

        if os.path.exists(img_path):
            if img_file in os.listdir(img_folder):
                with open(txt_path, 'r') as d:
                    lines = d.readlines()

                if len(lines) >= 3:
                    desc_dict = {
                        "name": lines[0].strip(),
                        "weight": int(lines[1].split()[0]),
                        "description": ''.join(lines[2:]).strip(),
                        "image_name": img_file
                    }

                    print(f'Processed {txt_path}: {desc_dict}')
                    return desc_dict

                else:
                    print(f"Error: Insufficient lines in {txt_path}. Expected at least 4 lines.")
                    return None
            else:
                print(f"Image file not found in img_folder: {img_file}")
                return None
        else:
            print(f"Image file not found: {img_path}")
            return None

    except Exception as e:
        print(f'Error processing {txt_path}: {e}')
        return None


def description_files(desc_folder):
    description_data = []
    # id_counter = 1
    files = os.listdir(desc_folder)

    for txt_file in files:
        txt_path = os.path.join(desc_folder, txt_file)
        if os.path.isfile(txt_path) and txt_file.endswith('.txt'):
            description = analyse_description_file(txt_path, img_folder)
            if description:
                description_data.append(description)
                # id_counter += 1
    print(description_data)
    return description_data


description = description_files(desc_folder)

for d in description:
    try:
        print(f"Sending data: {d}")
        r = requests.post(url, json=d)
        if r.status_code == 201:
            print("Description sent successfully!", r.status_code)
        else:
            print("Failed to send description. Status code:", r.status_code)
    except Exception as e:
        print(f"Exception occurred: {e}")






############################################################################################################


# ORIGINAL
def analyse_description_file(txt_path, img_folder):
    try:
        img_file = txt_path.split('.')[0] + '.jpeg'
        img_path = os.path.join(img_folder, img_file)

        print(f"Processing file: {txt_path}")

        if os.path.exists(img_path):
            with open(txt_path, 'r') as d:
                lines = d.readlines()

            if len(lines) >= 3:
                desc_dict = {
                    # "id" : id_counter,
                    "name" : lines[0].strip(),
                    "weight" : int(lines[1].split()[0]),
                    "description" : ''.join(lines[2:]).strip(),
                    "image_name" : img_name
                }
                print(f'Processed {txt_path}: {desc_dict}')
                return desc_dict

        else:
            print(f"Error: Insufficient lines in {txt_path}. Expected at least 4 lines.")
            return None
    except Exception as e:
        print(f'Error proccessing {txt_path}: {e}')
        return None




# EJEMPLO 1
def analyse_description_file(txt_path, img_folder):
    try:
        img_file = os.path.basename(txt_path).split('.')[0] + '.jpeg'
        img_path = os.path.join(img_folder, img_file)

        print(f"Processing file: {txt_path}")

        if os.path.exists(img_path):
            found_image = None
            for root, dirs, files in os.walk(img_folder):
                for file in files:
                    if file == img_file:
                        found_image = file
                        break
                if found_image:
                    break

            if found_image:
                with open(txt_path, 'r') as d:
                    lines = d.readlines()

                if len(lines) >= 3:
                    desc_dict = {
                        "name": lines[0].strip(),
                        "weight": int(lines[1].split()[0]),
                        "description": ''.join(lines[2:]).strip(),
                        "image_name": found_image
                    }

                    print(f'Processed {txt_path}: {desc_dict}')
                    return desc_dict

                else:
                    print(f"Error: Insufficient lines in {txt_path}. Expected at least 4 lines.")
                    return None
            else:
                print(f"Image file not found in img_folder: {img_file}")
                return None
        else:
            print(f"Image file not found: {img_path}")
            return None

    except Exception as e:
        print(f'Error processing {txt_path}: {e}')
        return None