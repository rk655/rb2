import os
import requests
import time
import socket

CLIENT_FILE = "data/Found.txt"
CENTRAL_SERVER = "http://192.168.1.106:8080/check"  # Replace with actual IP
COMMAND = "alarm 71 comp1 Win is not empty"
INTERVAL = 300  # 5 minutes

def is_file_nonempty(path):
    return os.path.exists(path) and os.path.getsize(path) > 0

def get_hostname():
    return socket.gethostname()

while True:
    if is_file_nonempty(CLIENT_FILE):
        payload = {
            "host": get_hostname(),
            "command": COMMAND
        }
        try:
            requests.post(CENTRAL_SERVER, json=payload, timeout=5)
        except requests.RequestException:
            print("Failed to contact central server.")
        break
    time.sleep(INTERVAL)
