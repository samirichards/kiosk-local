import os
import requests
import time
import configparser

DEVICE_FILE = "/dev/kiosk"
API_ENDPOINT = "http://18.130.84.82/endpoint/add_data"
API_KEY = "your_api_key"

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config.get('CONFIG', 'API_KEY')

# Function to read from the device file
def read_device_file():
    with open(DEVICE_FILE, "r") as f:
        data = f.read()
        return data

# Function to send data to the API endpoint
def send_data_to_api(data):
    payload = {
        "api_key": API_KEY,
        "record_value": data
    }
    try:
        response = requests.post(API_ENDPOINT, json=payload)
        response.raise_for_status()
        print("Data sent successfully")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Continuously read from the device file and send data to the API endpoint
while True:
    try:
        data = read_device_file()
        if data:
            send_data_to_api(data)
    except Exception as err:
        print(f"Error occurred: {err}")
    # Sleep for 1 second before trying again
    time.sleep(1)