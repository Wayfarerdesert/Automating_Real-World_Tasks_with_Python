#!/usr/bin/env python3

import os
import requests

url = "http://34.125.33.8/upload/"
img_folder = "supplier-data/images"

for file in os.listdir(img_folder):
    if file.lower().endswith(".jpeg"):
        i = os.path.join(img_folder, file)
        with open(i, 'rb') as op:
            r = requests.post(url, files={'file': op})
            if r.status_code >= 200 and r.status_code <= 299:
                print(f"IMG {file} successfully uploaded", r.status_code)
            else:
                print(f"Falied to upload IMG {file}", r.status_code)



