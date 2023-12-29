#!/usr/bin/env python3

import smtplib
import email.message
import mimetypes
import os.path


def generate_email(sender, recipient, subject, body, att_path):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    att_filename = os.path.basename(att_path)
    mime_type, _ = mimetypes.guess_type(att_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    try:
        with open(att_path, 'rb') as at:
            message.add_attachment(at.read(),
                                    maintype = mime_type,
                                    subtype = mime_subtype,
                                    filename = att_filename)
        return message
    except FileNotFoundError:
        return 'Error: File not found'
    except Exception as e:
        return f'Error attaching file: {e}'


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


def generate_error_report(sender, recipient, subject, body):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message