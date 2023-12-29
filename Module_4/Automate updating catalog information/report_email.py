#!/usr/bin/env python3

import os
import datetime
import reports
import emails


desc_folder = "supplier-data/descriptions"

def generate_report():
    files = os.listdir(desc_folder)

    report = ''

    for f in files:
        if f.endswith('.txt'):
            with open(os.path.join(desc_folder, f), 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                report_name = f"name: {name}\n"
                report_weight = f"weight: {weight}\n"
                report += '<br/>' + report_name + '<br/>'+ report_weight + '<br/>'
    return report

def main():
    attachment = "/tmp/processed.pdf"
    date = datetime.date.today().strftime("%B %d, %Y")
    title = f"Processed Update on {date}"
    paragraph = generate_report()
    reports.generate_report(attachment, title, paragraph)

    # Send the PDF report as an email attachment
    sender = "automation@example.com"
    recipient = "username@example.com" #REPLACE USERNAME HERE
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = attachment

    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)

    # # Send report through email
    # err_subject = ""
    # err_body = "Please check your system and resolve the issue as soon as possible."

    # case = ''

    # if case == 'CPU usage is over 80%':
    #     err_subject = 'Error: CPU usage is over 80%'
    # elif case == 'Available disk space is lower than 20%':
    #     err_subject = 'Error - Available disk space is less than 20%'
    # elif case == 'available memory is less than 500MB':
    #     err_subject = 'Error: Available memory is less than 500MB'
    # elif case == 'hostname "localhost" cannot be resolved to "127.0.0.1"':
    #     err_subject = 'Error: Hostname "localhost" cannot be resolved to "127.0.0.1"'


    # err_message = emails.generate_error_report(sender, recipient, err_subject, err_body)
    # emails.send_email(err_message)


if __name__ == "__main__":
    main()











############################################################################################################
# ORIGINAL
def generate_report():
    files = os.listdir(desc_folder)

    report = ""

    for f in files:
        if f.endswith('.txt'):
            with open(os.path.join(desc_folder, f), 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                report += f"name: {name}\nweight: {weight}\n\n"
    return report




def generate_report():
    files = os.listdir(desc_folder)

    report = ''

    for f in files:
        if f.endswith('.txt'):
            with open(os.path.join(desc_folder, f), 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                report_name = f"name: {name}\n"
                report_weight = f"weight: {weight}\n"
                report += '<br/>' + report_name + '<br/>'+ report_weight + '<br/>'
    return report


'<br/>'

names=[]
weights=[]
for file in os.listdir(desc_folder):
    with open(path + file) as f:
        for ln in f:
            line = ln.strip()
            if len(line) <= 10 and len(line) > 0 and 'lb' not in line:
                fruit_name='name: ' + line
                names.append(fruit_name)
            if 'lbs' in line:
                fruit_weight='weight: ' + line
                weights.append(fruit_name)

summary=''
for name, weight in zip(names, weight):
    summary += name
