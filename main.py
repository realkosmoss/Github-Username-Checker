import requests
import random
import string
import time
import platform

if platform.system() == "Windows":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Kosmos Username Checker - Checked: 0")

def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def check_website(url, username):
    response = requests.get(url)
    
    if response.status_code >= 400:
        print("Good", url)
        with open("available_usernames.txt", "a") as file:
            file.write(username + "\n")
    else:
        print("Already taken", url)
    if response.status_code == 429:
        print("Error 429 Rate Limited", url)
        time.sleep(5)

base_url = "https://github.com"

checked = 0
while True:
    checked += 1
    random_string = generate_random_string(random.randint(3, 4))
    website_url = f"{base_url}/{random_string}"
    check_website(website_url, random_string)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Kosmos Username Checker - Checked: {checked}")
    time.sleep(0.5)
