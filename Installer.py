import os
from tkinter import filedialog
import requests
import keyboard

def connection_available():
    try:
        response = requests.get("https://www.google.com", timeout = 5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False

def download_file(url, save_path):
    try:
        response = requests.get(url, stream = True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Downloaded")
    except requests.RequestException:
        print("Failed to download", url, "\n\tPress 'r' to retry or any other key to exit")
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'r':
                download_file(url, save_path)
            else:
                exit()

while not connection_available():
    print("No internet connection:\n\tPress 'r' to retry or any other key to exit")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'r':
            pass
        else:
            exit()

path = filedialog.askdirectory(title = "Select directory")
while not path:
    print("No path selected:\n\tPress 'r' to retry or any other key to exit")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'r':
            path = filedialog.askdirectory(title = "Select directory")
        else:
            exit()
folder_path = os.path.join(path, "sWeather")
os.makedirs(folder_path, exist_ok = True)

download_list = [
    {"sWeather.exe" : r"https://github.com/KssK111/sWeather/raw/refs/heads/main/All%20Needed%20Files/sWeather.exe"},
    {"settings.ini" : r"https://github.com/KssK111/sWeather/raw/refs/heads/main/All%20Needed%20Files/settings.ini"}
]
for file in download_list:
    for name, url in file.items():
        path = os.path.join(folder_path, name)
        print("Downloading", name)
        download_file(url, path)