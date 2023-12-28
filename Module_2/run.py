#! /run/bin/env python3

import os
import requests

folder_path = '/data/feedback'

def analyse_feedback_data(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        if len(lines) >= 4:
            feedback_dict = {
                'id': os.path.splitext(os.path.basename(file_path))[0],
                'title' : lines[0].strip(),
                'name' : lines[1].strip(),
                'date' : lines[2].strip(),
                'feedback' : ''.join(lines[3:]).strip()
            }

            return feedback_dict
        else:
            print(f"Error: Insufficient lines in {file_path}. Expected at least 4 lines.")
            return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def feedback_files(folder_path)
    feedback_data = []
    files = os.listdir(folder_path)

    for f in files:
        file_path = os.path.join(folder_path, f)
        if os.path.isfile(file_path) and f.endswith('.txt'):
            feedback = analyse_feedback_data(file_path)
            # feedback_data[f] = feedback
            feedback_data.append(feedback)

    return feedback_data


feedback = feedback_files(folder_path)
url = 'http://34.123.128.131/feedback'

for feedback_data in feedback:
    response = requests.post(url, json=feedback_data)
    if response.status_code == 201:
        print("Feedback sent successfully!", response.status_code)
    else:
        print("Failed to send feedback. Status code:", response.status_code)
        print(feedback_data)








