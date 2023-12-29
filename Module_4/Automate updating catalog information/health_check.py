#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import time

# set system thresholds:
max_disk_avail_perc = 20
max_cpu_usage_perc = 80
max_mem_avail_mb = 500
chk_localhost_ip = "127.0.0.1"


# def disk_usage():
#     """check if Disk usage exceeds max threshold"""
#     du = shutil.disk_usage("/")
#     max_du_perc = 100 - (du.free / du.total * 100)
#     return max_du_perc > max_disk_avail_perc

def disk_usage():
    """check if Disk usage exceeds max threshold"""
    max_disk_usage_perc = 100 - max_disk_avail_perc
    dsk_usage_perc = psutil.disk_usage("/").percent
    return dsk_usage_perc > max_disk_usage_perc

def cpu_usage():
    """check if CPU usage % exceeds max threshold"""
    usage = psutil.cpu_percent(1)
    return usage > max_cpu_usage_perc

def mem_usage():
    """check if Memory usage % exceeds max threshold"""
    one_mb = 2 ** 20
    max_mem_av = one_mb * max_mem_avail_mb
    mem_available = psutil.virtual_memory().available
    return mem_available < max_mem_av


def check_hostname():
    """check if local host name resolves to local IP"""
    localhost_ip = socket.gethostbyname('localhost')
    return localhost_ip != chk_localhost_ip


def sendAlert(alert):
    """output alert error and send email"""
    sender = "automation@example.com"
    recipient = "username@example.com" #REPLACE USERNAME HERE
    subject = alert
    body = "Please check your system and resolve the issue as soon as possible."

    try:
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)
    except Exception as e:
        print(f"Failed to send email alert: {e}")
    finally:
        print(alert)
        exit(1)


def main():
    # check system resources:
    print("checking system resources...")
    alert = None

    if disk_usage():
        alert = f'Error - Available disk space is less than {max_disk_avail_perc}%'

    elif cpu_usage():
        alert = f'Error - CPU usage is over {max_cpu_usage_perc}%'

    elif mem_usage():
        alert = f'Error - Available memory is less than {max_mem_avail_mb}MB'

    elif check_hostname():
        alert = f'Error - localhost cannot be resolved to {chk_localhost_ip}'

    # time.sleep(60)

    # alert if error raised:
    if alert:
        sendAlert(alert)
    else:
        print("system ok")


if __name__ == "__main__":
    main()

# * * * * * /usr/bin/python3 /home/student-03-c3e783d990d2/health_check.py


############################################################################################################################################################################################################################################################


# ORIGINAL

#!/usr/bin/env python3

import shutil
import psutil
import socket
import time


def disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20

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




err_message = emails.generate_error_report(sender, recipient, err_subject, err_body)
    emails.send_email(err_message)








def disk_usage():
    """check if Disk usage exceeds max threshold"""
    max_du_perc = 100 - max_disk_avail_perc
    du = shutil.disk_usage("/")
    used_percentage = (du.used / du.total) * 100
    return used_percentage > max_du_perc