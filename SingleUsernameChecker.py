import requests
import random
import string
import time
import platform

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Kosmos Username Checker")

def check_website(url, username):
    response = requests.get(url)
    
    if response.status_code >= 400:
        print(f"Username '{username}' is available on GitHub.")
    else:
        print(f"Username '{username}' is already taken on GitHub.")
    if response.status_code == 429:
        print("Error 429 Rate Limited. Waiting 5 seconds...")
        time.sleep(5)

base_url = "https://github.com"

while True:
    username_to_check = input("Enter the username to check: ")
    
    website_url = f"{base_url}/{username_to_check}"
    check_website(website_url, username_to_check)
    ctypes.windll.kernel32.SetConsoleTitleW("Kosmos Username Checker")
    
    check_another = input("Do you want to check another username? (yes/no): ")
    if check_another.lower() != "yes":
        break
