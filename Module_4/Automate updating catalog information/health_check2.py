#!/usr/bin/env python3

import shutil
import psutil
import socket
import time
import emails
import os

sender = "automation@example.com"
recipient = "username@example.com" #REPLACE USERNAME HERE
body = "Please check your system and resolve the issue as soon as possible."

def disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20
    subject = 'Error: CPU usage is over 80%'

def cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > 80

def mem_usage():
    mem = psutil.virtual_memory()

    THRESHOLD = 500 * 1024 * 1024
    if mem.available <  THRESHOLD:
        print('available memory is less than 500MB')
        return True
    return False


def check_hostname():
    try:
        ip = socket.gethostname('localhost')
        if ip != '127.0.0.1':
            print('Error: Hostname "localhost" cannot be resolved to 127.0.0.1')
            return True
    except socket.error:
        print('hostname "localhost" cannot be resolved to "127.0.0.1"')
        return True
    return False



while True:
    if disk_usage("/"):
        print('CPU usage is over 80%')

    if cpu_usage():
        print('Available disk space is lower than 20%')

    if mem_usage():
        pass  # Error already reported within the function

    if check_hostname():  # Check hostname resolution
        pass  # Error already reported within the function

    time.sleep(60)

