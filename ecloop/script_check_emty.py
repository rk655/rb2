#!/usr/bin/env python3
import os
import time
from wolfsoftware.pushover import Pushover

# File path to monitor
file_path = '/home/andriy/ecloop/data/found.txt'

# Initialize the Pushover instance
pushover = Pushover(user_key='ucsdgsdpdyyrf8x9dkh2q3de6vhme9', api_token='aynqnejqjoaciu4x46p1te86ys6f8w')

def is_file_empty(path):
    return os.path.getsize(path) == 0

def send_push_notification(message):
    try:
        response = pushover.send_message(message='Hello, The file pub found 71 is NOT empty!')
        print("Notification sent.")
    except Exception as e:
        print(f"Failed to send notification: {e}")

while True:
    try:
        if not is_file_empty(file_path):
            with open(file_path, 'r') as f:
                # content = f.read()
                send_push_notification(f"The file pub found 71 is NOT empty:\n\n")
                break
        # else:
            # print("File is empty. No notification sent.")
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(6000)  # Wait 20 minutes

